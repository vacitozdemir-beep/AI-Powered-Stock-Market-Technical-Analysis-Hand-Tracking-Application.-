# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı etkinleştir (Linux/macOS)
source venv/bin/activate

# Sanal ortamı etkinleştir (Windows)
# .\venv\Scripts\activate

# Gerekli Kütüphaneler
mediapipe
opencv-python
yfinance
streamlit
scikit-learn
tensorflow # Veya PyTorch (LSTM modeli için)
pandas
numpy
python-dotenv

pip install -r requirements.txt

# Lütfen .env dosyasını projenin ana dizininde (AI-Powered-Stock-Market-App/) oluşturun.
# Gerekli ise, Finansal API anahtarınızı buraya girin.
# Eğer sadece yfinance kullanılıyorsa bu satır gerekli olmayabilir,
# ancak Streamlit'te ortam değişkeni okumak için yine de yararlıdır.
FINANCIAL_API_KEY="YOUR_API_KEY_HERE"

streamlit run src/app.py
