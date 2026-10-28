import os
from cryptography.fernet import Fernet

def anahtar_olustur():
    """Şifreleme için gizli bir anahtar üretir ve dosyaya kaydeder."""
    anahtar = Fernet.generate_key()
    with open("gizli.key", "wb") as key_file:
        key_file.write(anahtar)
    print("🔑 Yeni şifreleme anahtarı oluşturuldu: gizli.key")

def anahtar_yukle():
    """Önceden oluşturulan gizli anahtarı okur."""
    return open("gizli.key", "rb").read()

def dosya_sifrele(dosya_yolu):
    """Metin veya fotoğraf fark etmez, verilen dosyayı şifreler."""
    anahtar = anahtar_yukle()
    f = Fernet(anahtar)
    
    with open(dosya_yolu, "rb") as file:
        dosya_verisi = file.read()
    
    sifreli_veri = f.encrypt(dosya_verisi)
    
    yeni_dosya_adi = dosya_yolu + ".enc"
    with open(yeni_dosya_adi, "wb") as file:
        file.write(sifreli_veri)
        
    print(f"🔒 Başarıyla şifrelendi: {yeni_dosya_adi}")

def dosya_sifre_coz(sifreli_dosya_yolu):
    """Şifrelenmiş dosyanın şifresini çözer ve orijinal haline getirir."""
    anahtar = anahtar_yukle()
    f = Fernet(anahtar)
    
    with open(sifreli_dosya_yolu, "rb") as file:
        sifreli_veri = file.read()
    
    orijinal_veri = f.decrypt(sifreli_veri)
    
    orijinal_dosya_adi = sifreli_dosya_yolu.replace(".enc", "")
    with open("cozulen_" + orijinal_dosya_adi, "wb") as file:
        file.write(orijinal_veri)
        
    print(f"🔓 Şifre çözüldü: cozulen_{orijinal_dosya_adi}")

if __name__ == "__main__":
    # Anahtar yoksa otomatik oluştur
    if not os.path.exists("gizli.key"):
        anahtar_olustur()
    
    print("\n--- Veri Şifreleme Aracı ---")
    print("1. Dosya/Fotoğraf Şifrele")
    print("2. Şifreyi Çöz")
    secim = input("Seçiminiz (1 veya 2): ")
    
    if secim == "1":
        yol = input("Şifrelenecek dosyanın adı (örn: resim.jpg veya metin.txt): ")
        dosya_sifrele(yol)
    elif secim == "2":
        yol = input("Şifresi çözülecek dosyanın adı (örn: resim.jpg.enc): ")
        dosya_sifre_coz(yol)
    else:
        print("Geçersiz seçim!")
