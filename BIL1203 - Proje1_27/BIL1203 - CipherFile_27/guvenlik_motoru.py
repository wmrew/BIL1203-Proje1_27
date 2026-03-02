import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def _anahtar_turet(parola: str) -> bytes:
    """AES için paroladan güvenli anahtar üretir."""
    tuz = b'bakircay_muhendislik_grup27' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=tuz,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(parola.encode()))

def _sezar_anahtari_turet(parola: str) -> int:
    """Sezar için 0-25 arası kaydırma sayısı üretir."""
    return sum(ord(c) for c in parola) % 26

def dosyayi_sifrele(girdi_yolu: str, parola: str, hedef_klasor: str, algoritma: str) -> str:
    """Dosyayı seçilen yöntemle şifreler ve hedefe kaydeder."""
    with open(girdi_yolu, "rb") as f:
        orijinal_veri = f.read()
        
    os.makedirs(hedef_klasor, exist_ok=True)
    
    if algoritma == "AES":
        anahtar = _anahtar_turet(parola)
        fernet = Fernet(anahtar)
        islenen_veri = fernet.encrypt(orijinal_veri)
        uzanti = ".enc"
    else: # Sezar 
        kaydirma = _sezar_anahtari_turet(parola)
        temp = bytearray()
        for b in orijinal_veri:
            if 65 <= b <= 90: temp.append((b - 65 + kaydirma) % 26 + 65) # A-Z
            elif 97 <= b <= 122: temp.append((b - 97 + kaydirma) % 26 + 97) # a-z
            else: temp.append(b) 
        islenen_veri = bytes(temp)
        uzanti = ".sezar"

    yeni_yol = os.path.join(hedef_klasor, os.path.basename(girdi_yolu) + uzanti)
    with open(yeni_yol, "wb") as f:
        f.write(islenen_veri)
    return yeni_yol

def dosyayi_coz(girdi_yolu: str, parola: str, hedef_klasor: str, algoritma: str) -> str:
    """Şifreli dosyayı orijinal haline getirir."""
    with open(girdi_yolu, "rb") as f:
        okunan_veri = f.read()
        
    if algoritma == "AES":
        anahtar = _anahtar_turet(parola)
        fernet = Fernet(anahtar)
        cozulmus_veri = fernet.decrypt(okunan_veri)
    else: # Sezar Çözüm
        kaydirma = _sezar_anahtari_turet(parola)
        temp = bytearray()
        for b in okunan_veri:
            if 65 <= b <= 90: temp.append((b - 65 - kaydirma) % 26 + 65)
            elif 97 <= b <= 122: temp.append((b - 97 - kaydirma) % 26 + 97)
            else: temp.append(b)
        cozulmus_veri = bytes(temp)

    temiz_ad = os.path.basename(girdi_yolu).replace(".enc", "").replace(".sezar", "")
    isim, uzanti = os.path.splitext(temiz_ad)
    yeni_yol = os.path.join(hedef_klasor, f"{isim}_cozuldu{uzanti}")
    
    with open(yeni_yol, "wb") as f:
        f.write(cozulmus_veri)
    return yeni_yol