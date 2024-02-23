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

![]([https://github.com/thedewil/InstelaMesajYedek/assets/848362/8ae0ca68-32c4-451b-88ed-34c998327db4](https://github-production-user-asset-6210df.s3.amazonaws.com/848362/307294139-8ae0ca68-32c4-451b-88ed-34c998327db4.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240223T103931Z&X-Amz-Expires=300&X-Amz-Signature=8527d910380105fc4c9faf424fe7e5841366b283e4d3334f19a64dedee466e71&X-Amz-SignedHeaders=host&actor_id=848362&key_id=0&repo_id=762207722)
5. **Mesajların Yedeklenmesi**:
    - Program, sayfa sayfa mesajlarınızı alacak ve işlem tamamlandığında aynı klasöre `instela_mesaj_yedek.html` adında, mesajlarınızı içeren bir dosya oluşturacak.

## Önemli Notlar

- Bu program, Instela'nın resmi bir uygulaması değildir. Kullanıcıların kendi mesajlarını yedeklemelerine yardımcı olmak için oluşturulmuştur.
- Program, bilgisayarınızda çalışır ve mesajlarınızı herhangi bir sunucuya göndermez. Güvenlik nedenleriyle çerez bilgilerinizi başkalarıyla paylaşmaktan kaçının, çünkü bu bilgilerle Instela hesabınıza erişilebilir.
- İndirilen mesajlarınızı güvenli bir yerde saklayın ve başkalarıyla paylaşmaktan kaçının.
