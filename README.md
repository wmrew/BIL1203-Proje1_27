I. 
GİRİŞ 
Bu proje, İzmir Bakırçay Üniversitesi Bilgisayar Mühendisliği Bölümü BIL1203 dersi kapsamında 
"CipherFile" isimli dosya şifreleme uygulamasını geliştirmek amacıyla hazırlanmıştır. Projedeki temel 
amacımız, sadece derste gördüğümüz teorik bilgileri değil, gerçek bir yazılımın nasıl planlandığını ve 
kodlandığını öğrenmektir. Birinci sınıf öğrencileri olarak, metin dosyalarını şifreleyip tekrar eski haline 
getiren bir sistem kurarak veri güvenliğinin temellerini kavramayı hedefledik. 
Uygulamayı yazarken en çok "dosyayı nereye kaydedeceğiz?" kısmında zorlandık. Programın her 
bilgisayarda çalışması için kodun kullanıcı adını otomatik bulmasını sağladık. Ayrıca Sezar şifrelemesi 
yaparken harf olmayan karakterlerin (boşluk, nokta vb.) karışmaması için sadece alfabedeki harfleri 
kaydıracak bir mantık kurduk. Böylece şifrelenmiş dosyayı açtığımızda beklediğimiz gibi yer 
değiştirmiş harfleri görebildik.
-----------------------------------------------------------------------------------------------------------------------------------------------
II. 
YÖNTEM  
Yazılımımızı geliştirirken öğrenmesi keyifli ve güçlü bir dil olan Python'u tercih ettik. Kodun daha 
düzenli durması ve "hangisi arayüz, hangisi asıl işi yapan kod" karmaşası olmaması için projeyi iki ana 
dosyaya ayırdık: main.py (ekrandaki butonlar ve tasarım) ve guvenlik_motoru.py (şifreleme 
matematiksel işlemleri). 
• AES Algoritması: Dosyayı tamamen "kilitli" hale getirmek için profesyonel sistemlerde 
kullanılan AES-256 yöntemini seçtik. 
• Sezar Algoritması: Alfabedeki harfleri belirli bir sayıda kaydırarak çalışan bu klasik yöntemi, 
şifreleme mantığını basitçe görmek için ekledik. 
• Arayüz: Kullanıcının dosyayı kolayca seçebilmesi için customtkinter kütüphanesiyle modern 
bir panel tasarladık.
-----------------------------------------------------------------------------------------------------------------------------------------------
III. 
UYGULAMA GERÇEKLEŞTİRME 
Proje kapsamında tamamlanması istenen iş paketleri ve araştırma sonuçları aşağıda 
detaylandırılmıştır: 
1. Kullanılan Şifreleme Algoritmaları ve Tercih Nedenleri: Projeye dahil edilen AES-256 
algoritması, günümüzde askeri ve ticari sistemlerde kullanılan en güvenli standartlardan biridir. Sezar 
şifrelemesi ise algoritma mantığının kullanıcı tarafından çıplak gözle gözlemlenebilmesi amacıyla 
sisteme dahil edilmiştir. Her iki algoritma da kullanıcıdan alınan dinamik bir parola (anahtar) üzerinden 
türetilmektedir. 
2. Gerçek Hayattaki Uygulama Alanları: Geliştirilen sistem, yerel bilgisayarlarda saklanan hassas 
finansal kayıtlar, kişisel veriler ve proje notlarının yetkisiz erişime karşı korunmasında kritik bir rol 
oynar. Özellikle bulut depolama birimlerine (OneDrive, Google Drive vb.) yüklenmeden önce 
dosyaların şifrelenmesi, "Sıfır Güven" mimarisine katkı sağlar. 
3. Yazılım Projesi Planlama Süreci: Proje takvimine sadık kalınarak; ilk hafta gereksinim analizi, 
ikinci hafta algoritma motorunun yazımı ve arayüz birleştirmesi ile testler gerçekleştirilmiştir. 
4. GitHub ve Sürüm Kontrol Yönetimi: Proje sürecinde GitHub platformu, temel kod deposu ve 
sürüm yedekleme merkezi olarak kullanılmıştır. Kodun farklı gelişim aşamaları ana dallarda saklanmış, 
bu sayede olası kod hatalarında "geriye dönük sürüm kontrolü" sağlanmıştır. GitHub kullanımı, projenin 
açık kaynak kodlu standartlara uygunluğunu ve asenkron çalışma modelini pekiştirmiştir. 
5. Kullanıcı Arayüzü (GUI) Tasarım Prensipleri: Kullanıcıyı yormayan, modern "Soft Light" tema 
tercih edilmiştir. İşlem sırasında kullanıcının süreci takip edebilmesi için dinamik bir "İlerleme Çubuğu" 
(Progress Bar) ve "Durum Çubuğu" (Status Bar) eklenerek interaktiflik artırılmıştır. 
Final aşamasında yazılım, .docx, .txt ve .png gibi farklı dosya türleri üzerinde test edilmiştir. 
Uygulamanın en ilginç kısmı, Sezar algoritmasının byte-tabanlı şifrelemeden karakter-tabanlı 
şifrelemeye dönüştürülmesidir. Başlangıçta şifreli dosyaların içinde görülen "???" şeklindeki tanımsız 
karakterler, algoritmanın sadece standart ASCII tablosundaki harfleri (A-Z, a-z) kaydıracak şekilde 
revize edilmesiyle çözülmüştür. Bu sayede şifrelenmiş bir metin dosyası açıldığında, kullanıcının 
beklediği "yer değiştirmiş harfler" görseli başarıyla elde edilmiştir.
-----------------------------------------------------------------------------------------------------------------------------------------------
KAYNAKÇA 
Kerzner, H. (2017). Project Management: A Systems Approach to Planning, Scheduling, and 
Controlling. John Wiley & Sons. 
Stallings, W. (2017). Cryptography and Network Security: Principles and Practice. Pearson Education. 
Sweigart, A. (2018). Cracking Codes with Python: An Introduction to Building and Breaking Ciphers. 
No Starch Press. 
Cryptography Developers. (2026). Cryptography: Python Security Library Documentation. Erişim 
tarihi: 2 Mart 2026, https://cryptography.io/en/latest/. 
Schmit, T. (2026). CustomTkinter: Complex Modern GUI Library for Python. Erişim tarihi: 2 Mart 
2026, https://github.com/TomSchimansky/CustomTkinter. 
Python Software Foundation. (2026). Python Language Reference, version 3.12. 
https://www.python.org.
