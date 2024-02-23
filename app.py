import requests
import time
import pandas as pd
from datetime import datetime

# Veri saklamak için listeyi başlat
veri = []

# 'fetch_all_thread_messages' fonksiyonunu düzenleyerek tarih dizesini doğrudan ele alın
def fetch_all_thread_messages(thread_id, headers):
    print(f"Thread ID {thread_id} için tüm mesajlar getiriliyor...")
    base_url = f'https://tr.instela.com/api/v2/messages/{thread_id}'
    sayfa = 1
    sayfa_var = True
    while sayfa_var:
        detay_url = f'{base_url}?ajaxload=true&page={sayfa}'
        try:
            yanıt = requests.get(detay_url, headers=headers)
            yanıt.raise_for_status()
            veri_yanıtı = yanıt.json()
            konu_detayları = veri_yanıtı.get('thread', {})
            if konu_detayları and konu_detayları.get('messages'):
                mesajlar = konu_detayları['messages']
                for mesaj in mesajlar:
                    # Her mesajdan gönderen ve alıcı bilgilerini çıkarın
                    gönderen_kullanıcı_adı = mesaj['sender']['username'] if 'sender' in mesaj else 'Bilinmeyen'
                    alıcı_kullanıcı_adı = mesaj['receiver']['username'] if 'receiver' in mesaj else 'Bilinmeyen'
                    mesaj_metni = mesaj['message'].replace('\r', '').replace('\n', '')
                    # Tarih dizesini doğrudan biçimlendirin
                    tarih = mesaj['date'][:19].replace('T', ' ')
                    # Çıkarılan bilgileri veri listesine ekleyin
                    veri.append([thread_id, gönderen_kullanıcı_adı, alıcı_kullanıcı_adı, mesaj_metni, tarih])
                print(f"Thread ID {thread_id}, Sayfa {sayfa}: {len(mesajlar)} mesaj getirildi.")
            else:
                sayfa_var = False
                print(f"Thread ID {thread_id} için daha fazla mesaj yok.")
                break
            sayfa += 1
        except requests.exceptions.RequestException as e:
            print(f"Thread ID {thread_id} için sayfa {sayfa} detayları getirilirken hata oluştu: {e}")
            break


def fetch_threads(headers):
    base_url = 'https://tr.instela.com/api/v2/messages'
    sayfa = 1
    thread_var = True

    while thread_var:
        params = {'page': sayfa, 'ajaxload': 'true', 'noautoload': 'true'}
        try:
            yanıt = requests.get(base_url, headers=headers, params=params)
            yanıt.raise_for_status()

            veri_yanıtı = yanıt.json()

            if not veri_yanıtı['threads']:
                thread_var = False
                print("Daha fazla konu getirilemiyor.")
                break
            else:
                print(f"Sayfa {sayfa} getirildi ve {len(veri_yanıtı['threads'])} konu içeriyor.")
                for konu in veri_yanıtı['threads']:
                    fetch_all_thread_messages(konu['id'], headers)
                sayfa += 1
        except requests.exceptions.RequestException as e:
            print(f"Sayfa {sayfa} getirilirken hata: {e}")
            break

headers = {
    # Gerekli başlıkları burada belirtin
    'cookie': input("Lütfen çerez değerini buraya yapıştırın: "),
}

fetch_threads(headers)

# Toplanan verileri bir DataFrame'e dönüştür
df = pd.DataFrame(veri, columns=['KonuID', 'Gönderen', 'Alıcı', 'Mesaj', 'Tarih'])

# 'Tarih' sütununu datetime formatına çevir
df['Tarih'] = pd.to_datetime(df['Tarih'], errors='coerce', utc=True)

# Tüm yorumların Türkçe çevirisini yapın
# DataFrame'i önce 'KonuID' sonra 'Tarih' sütununa göre sırala
df = df.sort_values(by=['KonuID', 'Tarih'], ascending=[True, True])

# HTML dosyasına yazdırmak için DataFrame'i biçimlendirme kodunu değiştirin
html_dosya_yolu = 'instela_mesaj_yedek.html'
with open(html_dosya_yolu, 'w') as html_dosyası:
    # HTML içeriğini yazmaya başlayın
    html_dosyası.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Instela Mesaj Yedek</title>\n</head>\n<body>\n")

    # Tablo başlığını yazın
    html_dosyası.write("<table border='1'>\n<tr>\n<th>KonuID</th>\n<th>Gönderen</th>\n<th>Alıcı</th>\n<th>Mesaj</th>\n<th>Tarih</th>\n</tr>\n")

    # DataFrame'in her satırını biçimlendirilmiş tarih ile yazın
    for index, satır in df.iterrows():
        html_dosyası.write("<tr>\n")
        for sütun, değer in satır.items():
            if sütun == 'Tarih':
                # Tarih nesnesini doğrudan biçimlendirin
                biçimli_tarih = değer.strftime("%d.%m.%Y %H:%M:%S")
                html_dosyası.write(f"<td>{biçimli_tarih}</td>\n")
            else:
                html_dosyası.write(f"<td>{değer}</td>\n")
        html_dosyası.write("</tr>\n")

    # Tabloyu ve HTML içeriğini sonlandırın
    html_dosyası.write("</table>\n</body>\n</html>")

print(f"HTML dosyası {html_dosya_yolu} konumunda kaydedildi.")
