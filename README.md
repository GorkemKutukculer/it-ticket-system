# 🖥️ IT Ticket Management System

Bu proje, bir kurumun (Marmara Üniversitesi Bilgi İşlem birimi) iç destek taleplerini dijital ortamda yönetmek, önceliklendirmek ve analiz etmek için geliştirilmiş uçtan uca bir **IT Yardım Masası (Helpdesk)** uygulamasıdır.

## 🚀 Öne Çıkan Özellikler
* **Talep Yönetimi:** Yeni destek talebi oluşturma, durumu güncelleme ve hatalı kayıtları silme.
* **Dinamik Dashboard:** Toplam talep sayısı, açık biletler ve çözüm oranlarını gerçek zamanlı takip etme.
* **Filtreleme:** Çalışan bazlı bilet takibi ve öncelik (Low, Medium, High, Critical) yönetimi.
* **Veri Görselleştirme:** Çözülme oranları ve bilet durumlarını görsel metriklerle izleme.

## 🛠️ Teknik Stack
* **Language:** Python 3.x
* **Framework:** Streamlit (UI & Dashboard)
* **Database:** Microsoft SQL Server (MS SQL)
* **Libraries:** `pandas`, `pyodbc`, `plotly`

## 📂 Proje Yapısı
```text
it-ticket-system/
├── src/
│   ├── app.py              # Streamlit arayüz kodları
│   └── ticket_manager.py   # Veritabanı ve OOP mantığı (Backend)
├── README.md               # Proje dokümantasyonu
└── requirements.txt        # Gerekli kütüphaneler listesi


Görseldeki mevcut README.md dosyan oldukça sade kalmış. Bosch, Mercedes veya PwC gibi kurumsal yerler, GitHub projelerinde "ne yapıldığını" anlatan dokümantasyona çok önem verir.

İşte projenin profesyonel görünmesini sağlayacak, kopyalayıp kullanabileceğin Zenginleştirilmiş README Taslağı:

Markdown
# 🖥️ IT Ticket Management System

Bu proje, bir kurumun (örneğin Marmara Üniversitesi Bilgi İşlem birimi) iç destek taleplerini dijital ortamda yönetmek, önceliklendirmek ve analiz etmek için geliştirilmiş uçtan uca bir **IT Yardım Masası (Helpdesk)** uygulamasıdır.

## 🚀 Öne Çıkan Özellikler
* **Talep Yönetimi:** Yeni destek talebi oluşturma, durumu güncelleme ve hatalı kayıtları silme.
* **Dinamik Dashboard:** Toplam talep sayısı, açık biletler ve çözüm oranlarını gerçek zamanlı takip etme.
* **Filtreleme:** Çalışan bazlı bilet takibi ve öncelik (Low, Medium, High, Critical) yönetimi.
* **Veri Görselleştirme:** Çözülme oranları ve bilet durumlarını görsel metriklerle izleme.

## 🛠️ Teknik Stack
* **Language:** Python 3.x
* **Framework:** Streamlit (UI & Dashboard)
* **Database:** Microsoft SQL Server (MS SQL)
* **Libraries:** `pandas`, `pyodbc`, `plotly`

## 📂 Proje Yapısı
```text
it-ticket-system/
├── src/
│   ├── app.py              # Streamlit arayüz kodları
│   └── ticket_manager.py   # Veritabanı ve OOP mantığı (Backend)
├── README.md               # Proje dokümantasyonu
└── requirements.txt        # Gerekli kütüphaneler listesi

⚙️ Kurulum
Projeyi bilgisayarınıza indirin:
git clone [https://github.com/GorkemKutukculer/it-ticket-system.git](https://github.com/GorkemKutukculer/it-ticket-system.git)

Gerekli kütüphaneleri yükleyin:
pip install -r requirements.txt

Uygulamayı çalıştırın:
python -m streamlit run src/app.py

📈 Neden Bu Projeyi Geliştirdim?
Yönetim Bilişim Sistemleri (YBS) öğrencisi ve Bilgi İşlem çalışanı olarak, manuel takip edilen süreçlerin verimliliği düşürdüğünü gözlemledim. Bu uygulama ile SQL veritabanı yönetimini, Python ile otomasyonu ve iş süreçlerinin (BPM) dijitalleşmesini tek bir projede birleştirmeyi hedefledim