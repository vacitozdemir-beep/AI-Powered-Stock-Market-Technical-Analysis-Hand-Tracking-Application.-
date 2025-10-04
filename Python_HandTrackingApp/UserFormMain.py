from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QComboBox
from PyQt6.QtGui import QPixmap, QFont, QIcon, QColor, QTransform
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
import sys, subprocess, cv2, qrcode
import winsound, pyttsx3, random
from sklearn.ensemble import IsolationForest

class FingerprintLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_model()

    def initUI(self):
        self.setWindowTitle("Parmak İzi ile Giriş Ekranı")
        self.setGeometry(100, 100, 400, 550)
        self.setStyleSheet("background-color: #f0f0f0; border-radius: 12px;")

        layout = QVBoxLayout()

        # Renk Paleti ve Seçici
        self.color_palette = {
            "Açık Mavi": "#E0F7FA",
            "Açık Yeşil": "#E8F5E9",
            "Açık Sarı": "#FFFDE7",
            "Açık Kırmızı": "#FFEBEE",
            "Koyu Mavi": "#0277BD",
            "Koyu Yeşil": "#1B5E20",
            "Koyu Sarı": "#F9A825",
            "Koyu Kırmızı": "#B71C1C",
        }

        self.color_selector = QComboBox()
        self.color_selector.addItems(self.color_palette.keys())
        self.color_selector.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.color_selector.setStyleSheet("color: #000000;")
        self.color_selector.currentIndexChanged.connect(self.change_color)
        layout.addWidget(self.color_selector)

        # Başlık
        title = QLabel("Parmak İzi İle Giriş Yapınız!")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #ff4040;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Parmak İzi Görseli
        self.fingerprint_image = QLabel(self)
        pixmap = QPixmap("fingerprint.png")
        self.fingerprint_image.setPixmap(pixmap)
        self.fingerprint_image.setScaledContents(True)
        self.fingerprint_image.setFixedSize(300, 300)
        layout.addWidget(self.fingerprint_image, alignment=Qt.AlignmentFlag.AlignCenter)

        # Kullanıcı Adı ve Şifre Alanları
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Kullanıcı Adı")
        self.username.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 8px; background-color: white; border: 1px solid #ddd;")
        layout.addWidget(self.username)

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Şifre")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setStyleSheet("padding: 10px; font-size: 14px; border-radius: 8px; background-color: white; border: 1px solid #ddd;")
        layout.addWidget(self.password)

        # Parmak İzi ile Giriş Butonu
        self.fingerprint_button = QPushButton("🔒 Parmak İzi ile Giriş", self)
        self.fingerprint_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 12px; border-radius: 10px;")
        self.fingerprint_button.pressed.connect(self.on_button_press)
        self.fingerprint_button.released.connect(self.on_button_release)
        self.fingerprint_button.clicked.connect(self.authenticate)
        layout.addWidget(self.fingerprint_button)

        self.setLayout(layout)

    def load_model(self):
        self.model = IsolationForest(contamination=0.1)
        X = [[1, 2], [2, 3], [3, 4], [10, 10]]
        self.model.fit(X)

    def on_button_press(self):
        self.fingerprint_button.setStyleSheet("background-color: #388E3C; color: white; font-size: 16px; padding: 12px; border-radius: 10px;")

    def on_button_release(self):
        self.fingerprint_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 12px; border-radius: 10px;")

    def authenticate(self):
        giris_verisi = [[len(self.username.text()), len(self.password.text())]]
        anomali = self.model.predict(giris_verisi)[0]

        if anomali == -1:
            self.show_error_message("Olağandışı giriş denemesi!")
        elif self.username.text() == "admin" and self.password.text() == "1234":
            winsound.PlaySound("success.wav", winsound.SND_FILENAME)
            self.show_success_animation()
            QTimer.singleShot(1000, self.open_handtracking)
        else:
            self.show_error_message("Geçersiz giriş! Lütfen tekrar deneyin.")
            winsound.PlaySound("error.wav", winsound.SND_FILENAME)
            self.shake_window()

    def show_success_animation(self):
        # Resim sallama animasyonu
        animation = QPropertyAnimation(self.fingerprint_image, b"transform")
        animation.setDuration(500)
        animation.setKeyValueAt(0, QTransform().rotate(0))
        animation.setKeyValueAt(0.25, QTransform().rotate(10))
        animation.setKeyValueAt(0.5, QTransform().rotate(-10))
        animation.setKeyValueAt(0.75, QTransform().rotate(10))
        animation.setKeyValueAt(1, QTransform().rotate(0))
        animation.start()

        animation.finished.connect(lambda: self.show_success_message())

    def show_success_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Giriş Başarılı Uygulamaya Yönlendiriliyorsunuz!")
        msg.setWindowTitle("Başarı")
        msg.exec()

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle("Hata")
        msg.exec()

    def shake_window(self):
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(500)
        animation.setKeyValueAt(0.0, self.pos())
        animation.setKeyValueAt(0.1, self.pos() + Qt.QPoint(10, 0))
        animation.setKeyValueAt(0.2, self.pos() + Qt.QPoint(-10, 0))
        animation.setKeyValueAt(0.3, self.pos() + Qt.QPoint(10, 0))
        animation.setKeyValueAt(0.4, self.pos() + Qt.QPoint(-10, 0))
        animation.setKeyValueAt(0.5, self.pos())
        animation.start()

    def open_handtracking(self):
        self.close()
        subprocess.run(["python", "HandTrackingMain.py"])

    def change_color(self, index):
        self.setStyleSheet(f"background-color: {self.color_palette[self.color_selector.currentText()]}; border-radius: 10px;")
        self.username.setStyleSheet(f"padding: 10px; font-size: 14px; border-radius: 8px; background-color: white; border: 1px solid #ddd;")
        self.password.setStyleSheet(f"padding: 10px; font-size: 14px; border-radius: 8px; background-color: white; border: 1px solid #ddd;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FingerprintLogin()
    window.show()
    sys.exit(app.exec())
