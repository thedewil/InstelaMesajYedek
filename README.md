# Instela Mesajları Yedekleyici

Instela, 1 Mart 2024 tarihi itibariyle kapanıyor. Kapanmadan önce özel mesajlarınızı yedeklemek için aşağıdaki Python kodunu kullanabilirsiniz.

## Kullanım Talimatları

1. **Python Kurulumu**: Sisteminizde Python yüklü olmalı. Python'u [buradan](https://www.python.org/downloads/) indirebilirsiniz.

2. **Dosya İndirme ve Hazırlık**:
    - Bu [linkten](https://github.com/thedewil/InstelaMesajYedek/raw/main/app.py) `app.py` dosyasını indirin veya uygun bir klasöre kaydedin.
    - Komut Satırı / Terminal'i açın ve `app.py` dosyasının bulunduğu klasöre gidin.

3. **Programın Çalıştırılması**:
    - Aşağıdaki komutu çalıştırarak programı başlatın:
    ```
    python app.py
    ```
    ![](https://github.com/thedewil/InstelaMesajYedek/blob/main/c%CC%A7al%C4%B1s%CC%A7t%C4%B1rma.png?raw=true)
4. **Cookie/Çerez Bilgilerinin Girilmesi**:
    - Tarayıcınızda **F12**'ye basarak Geliştirici Konsolu'nu açın.
    - "Application" veya "Uygulama" sekmesine gidin ve "Cookies" altında Instela web sitesinin çerezlerini bulun.
    - `PHPSESSID=xxxx; refresh_token=xxx;` şeklinde görünen iki değeri alın.
    - Bu değerleri programın istediği yerlere yapıştırın ve Enter'a basın.
    [![Çalıştırma Görseli](https://github.com/thedewil/InstelaMesajYedek/raw/main/çalıştırma.png)
](https://github.com/thedewil/InstelaMesajYedek/blob/main/Cookie.mp4?raw=true)

5. **Mesajların Yedeklenmesi**:
    - Program, sayfa sayfa mesajlarınızı alacak ve işlem tamamlandığında aynı klasöre `instela_mesaj_yedek.html` adında, mesajlarınızı içeren bir dosya oluşturacak.

## Önemli Notlar

- Bu program, Instela'nın resmi bir uygulaması değildir. Kullanıcıların kendi mesajlarını yedeklemelerine yardımcı olmak için oluşturulmuştur.
- Program, bilgisayarınızda çalışır ve mesajlarınızı herhangi bir sunucuya göndermez. Güvenlik nedenleriyle çerez bilgilerinizi başkalarıyla paylaşmaktan kaçının, çünkü bu bilgilerle Instela hesabınıza erişilebilir.
- İndirilen mesajlarınızı güvenli bir yerde saklayın ve başkalarıyla paylaşmaktan kaçının.
