# Claude CVE Analysis Prototype

Bu prototip, Claude AI kullanarak CVE kayıtlarının analiz edilmesini göstermek amacıyla hazırlanmıştır.

## Kullanılan Teknolojiler

- Python
- FastAPI
- Claude API

## Çalışma Mantığı

Kullanıcı CVE ID gönderir.

↓

Prompt hazırlanır.

↓

Claude analiz işlemi gerçekleştirir.

↓

Sonuç kullanıcıya döndürülür.

## Çalıştırma

pip install -r requirements.txt

uvicorn main:app --reload