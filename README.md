# 🤖 AI Destekli Borsa Analizi ve El Takibi Uygulaması (AI-Powered Stock Market Technical Analysis & Hand Tracking App)

## Giriş

Bu proje, yapay zeka (Yapay Sinir Ağları/LSTM) tabanlı **borsa teknik analizi** tahminlerini, kullanıcı dostu bir arayüz ve yenilikçi bir **el hareketleriyle kontrol** sistemiyle birleştiren çığır açan bir uygulamadır.

Kullanıcılar, analiz sonuçlarını grafikler üzerinde incelerken, kameraya yaptıkları el hareketleri (jestler) ile alım/satım sinyallerini kolayca tetikleyebilir veya arayüzde gezinebilirler.

## ✨ Temel Özellikler

* **AI Tabanlı Tahminler:** Geçmiş verilerle eğitilmiş bir **LSTM Modeli** kullanarak hisse senedi/kripto fiyatlarının gelecekteki eğilimlerini tahmin etme.
* **Canlı El Hareketiyle Kontrol (Hand Tracking):** **MediaPipe** ve **OpenCV** kütüphaneleri aracılığıyla webcam'den alınan canlı görüntü ile el iskelet yapısını takip etme ve tanımlanan jestleri algılama.
* **Teknik Analiz:** Hareketli Ortalamalar (MA), RSI, MACD gibi temel teknik göstergelerin hesaplanması ve grafiklere entegrasyonu.
* **Hızlı Kullanıcı Arayüzü:** **Streamlit** ile oluşturulmuş, hızlı ve interaktif veri görselleştirmeleri sunan kullanıcı dostu bir arayüz.
* **Ücretsiz Veri Erişimi:** **yfinance** kütüphanesi ile popüler hisse senetleri veya kripto paraların geçmiş verilerine kolayca erişim.

## 🛠️ Teknolojiler

| Kategori | Teknoloji | Amaç |
| :--- | :--- | :--- |
| **Görüntü İşleme** | `MediaPipe` & `OpenCV` | El takibi, iskelet yapısı çıkarma ve webcam yönetimi. |
| **Veri & Finans** | `yfinance` | Ücretsiz hisse senedi/kripto verisi çekme. |
| **Yapay Zeka** | `TensorFlow` / `Keras` (LSTM) | Fiyat tahmini ve model yönetimi. |
| **Arayüz (UI)** | `Streamlit` | Web tabanlı interaktif kullanıcı arayüzü oluşturma. |
| **Veri Analizi** | `Pandas`, `NumPy` | Veri manipülasyonu ve teknik gösterge hesaplamaları. |

## 🚀 Kurulum ve Çalıştırma

### 1. Ön Gereksinimler

* Python 3.x
* Webcam (El takibi için gereklidir)

### 2. Projeyi Klonlama

```bash
git clone [https://github.com/vacitozdemir-beep/AI-Powered-Stock-Market-App.git](https://github.com/acitozdemir-beep/AI-Powered-Stock-Market-App.git)
cd AI-Powered-Stock-Market-App
