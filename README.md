# İstatistik ChatBot![Görüntü 22 10 2025 06 11](https://github.com/user-attachments/assets/a31720eb-22bb-4672-ba0b-9d8e71002175)


<div align="center">

*Temel İstatistiksel Kavramlar için Yapay Zeka Destekli Soru-Cevap Sistemi*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![RAG](https://img.shields.io/badge/Mimari-RAG-orange)](https://arxiv.org/abs/2005.11401)
[![MIT](https://img.shields.io/badge/İçerik-MIT%20Ders%20Notları-lightgrey)](https://mit.edu)

**Hipotez testleri hakkında akıllı sorular sorun • MIT istatistik notlarından cevaplar alın**

</div>

## Proje Hakkında

MIT ders notlarını kullanarak istatistiksel testler hakkında soruları yanıtlayan Retrieval Augmented Generation (RAG) tabanlı bir chatbot. Sistem, doğal dil sorgularını anlar ve güvenilir kaynaklardan doğru, bağlama uygun yanıtlar sağlar.

## Özellikler

- ** Akıllı Soru-Cevap**: İstatistiksel kavramlar için doğal dil anlama
- ** MIT Müfredatı**: Gerçek MIT istatistik ders notları ve çeşitli kaynaklarla desteklenmiş
- ** Anlamsal Arama**: Vektör embedding'ler ile ilgili bilgileri bulur
- ** Temiz Arayüz**: Modern, duyarlı web tasarımı
- ** Kolay Kurulum**: Tek komutla dağıtım

##  Hızlı Başlangıç

### Gereksinimler
- Python 3.8+
- pip

### Kurulum

```bash
# 1. Depoyu klonlayın
git clone https://github.com/ilgubuse/mit-statistics-chatbot.git
cd mit-statistics-chatbot

# 2. Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Uygulamayı başlatın
python app.py
```

`http://localhost:8000` adresini ziyaret ederek sohbete başlayın!

## Örnek Sorular

Şunları sorabilirsiniz:
- "T-test ve ANOVA arasındaki fark nedir?"
- "P değerleri nasıl yorumlanır?"
- "Tip 1 ve Tip 2 hataları açıklayın"
- "Parametrik ve parametrik olmayan testler ne zaman kullanılır?"
- "Hipotez testlerinin varsayımları nelerdir?"
- "Güç analizi nasıl yapılır?"
- "Örneklem büyüklüğü nasıl hesaplanır?"

## Teknik Mimari

```
Kullanıcı Sorusu → Web Arayüzü → Flask API → RAG Sistemi
                                      ↓
        Vektör Veritabanı ← Embedding'ler ← MIT Ders Notları
```

**Bileşenler:**
- **Backend**: Flask web framework
- **RAG Motoru**: LangChain + ChromaDB
- **Embedding'ler**: Sentence Transformers
- **Frontend**: HTML5, CSS3, JavaScript

## Proje Yapısı

```
mit-statistics-chatbot/
├── app.py                 # Ana uygulama
├── requirements.txt       # Bağımlılıklar
├── data/
│   └── mit_istatistik_notlari.txt  # Bilgi bankası
├── templates/
│   └── index.html        # Web arayüzü
└── README.md
```

## Kullanım Alanları

- **Öğrenciler**: Hipotez testi kavramlarını öğrenin
- **Araştırmacılar**: İstatistiksel yöntemler için hızlı referans
- **Eğitmenler**: İstatistik dersleri için asistan
- **Veri Bilimcileri**: İstatistik temellerini tazeleyin

## Geliştirme

Sistem, Retrieval Augmented Generation kullanarak:
1. MIT notlarını vektör embedding'lere dönüştürür
2. Kullanıcı sorgularında anlamsal benzerlik araması yapar
3. En ilgili bilgi parçalarını döndürür
4. Tüm cevaplar için kaynak atıfları sağlar

## Lisans

Bu proje Akbank GenAI Bootcamp kapsamında geliştirilmiştir.

## Geliştirici

**İlgü Buse Sezen**

<div align="center">

*İstatistiği yapay zeka ile erişilebilir kılmak*

</div>
