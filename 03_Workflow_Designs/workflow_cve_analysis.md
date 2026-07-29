# CVE Güvenlik Analiz Workflow

## Amaç

Güvenlik açıklarının otomatik toplanması, analiz edilmesi ve önceliklendirilmesi.


## Akış

NVD API

↓

Data Collector

↓

PostgreSQL Database

↓

Claude AI Analizi

↓

Risk Sınıflandırması

↓

Bildirim Sistemi


## Kullanılan Teknolojiler

- Python
- FastAPI
- PostgreSQL
- Claude API
- MCP
- Telegram Bot


## Örnek Çıktı

CVE:
CVE-2026-1234

Risk:
Yüksek

Açıklama:
Sistem üzerinde güvenlik açığı bulunmaktadır.

Öneri:
Güncelleme uygulanmalıdır.


## Faydalar

- Kritik açıkların hızlı tespiti
- Otomatik raporlama
- Güvenlik ekiplerine zaman kazandırma