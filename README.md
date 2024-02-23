# Instela Mesajları Yedekleyici

Instela 1 Mart 2024 itibari ile kapanıyor. Kapanmadan özel mesajlarınızı yedekleyebilmeniz için bu şekilde bir Python kodu oluşturdum.

1) Öncelikle sisteminizde Python yüklü olmalı. Şuradan yükleyebilirsiniz: https://www.python.org/downloads/

2) Daha sonra buradaki app.py dosyasını uygun bir klasöre indirin veya kaydedin.

3) Komut Satırı / Terminal açın. **app.py** dosyasının bulunduğu klasöre girin.

4) **python app.py** yazarak programı çalıştırın:
[[çalıştırma.png]]

5) Yukarıdaki gibi cookie/çerez bilgilerinizi isteyecek. 

Aşağıdaki şekilde, tarayıcınızdan ***F12**'ye basarak ve Geliştirici Konsolu kullanarak değerlerinizi bulun.

PHPSESSID=xxxx; refresh_token=xxx; şeklinde görünen iki değeri almanız yeterlidir. 
[[Cookie.mp4]]
6) Bu değerleri buraya yapıştırarak Enter'a basın.
7) Program sayfa sayfa mesajlarınızı alacak. İşlem tamamlandığında yine aynı klasörde **instela_mesaj_yedek.html** şeklinde, mesajlarınızı içeren bir dosya oluşturacak.

# Instela Mesajları Yedekleyici

Instela, 1 Mart 2024 tarihi itibariyle kapanıyor. Kapanmadan önce özel mesajlarınızı yedeklemek için aşağıdaki Python kodunu kullanabilirsiniz.

## Kullanım Talimatları

1. Öncelikle sisteminizde Python yüklü olmalı. Python'u [buradan](https://www.python.org/downloads/) indirebilirsiniz.

2. Daha sonra aşağıdaki adımları izleyin:

    - Bu [linkten](https://github.com/thedewil/InstelaMesajYedek/raw/main/app.py) `app.py` dosyasını indirin veya uygun bir klasöre kaydedin.
    
    - Komut Satırı / Terminal'i açın ve `app.py` dosyasının bulunduğu klasöre gidin.
    
    - Aşağıdaki komutu çalıştırarak programı başlatın:
    ```
    python app.py
    ```
    ![Görsel](https://github.com/thedewil/InstelaMesajYedek/raw/main/çalıştırma.png)

3. Program çalıştırıldığında, cookie/çerez bilgilerinizi isteyecek.

    - Tarayıcınızı açın ve **F12**'ye basarak Geliştirici Konsolu'nu açın.
    
    - Geliştirici Konsolu'nda, "Application" veya "Uygulama" sekmesine gidin ve "Cookies" veya "Çerezler" altında Instela web sitesinin çerezlerini bulun.
    
    - PHPSESSID=xxxx; refresh_token=xxx; şeklinde görünen iki değeri alın.
    
    - Bu değerleri programın istediği yerlere yapıştırın ve Enter'a basın.
    - ![Video](https://github.com/thedewil/InstelaMesajYedek/raw/main/Cookie.mp4)

4. Program, sayfa sayfa mesajlarınızı alacak ve işlem tamamlandığında aynı klasöre `instela_mesaj_yedek.html` adında bir dosya oluşturacak.

## Önemli Notlar

- Bu program, Instela'nın resmi bir uygulaması değildir. Sadece kullanıcıların kendi mesajlarını yedeklemelerine yardımcı olmak için oluşturulmuştur.

- Program, kendi bilgisayarınızda çalıştır ve mesajlarınızı herhangi bir sunucuya göndermez. Ancak, güvenlik nedenleriyle çerez bilgilerinizi başkalarıyla paylaşmaktan kaçının. Çerez bilgileriniz ile Instela hesabınıza erişim sağlanabilir.

- İndirilen mesajlarınızı güvenli bir yerde saklayın ve başkalarıyla paylaşmaktan kaçının.
