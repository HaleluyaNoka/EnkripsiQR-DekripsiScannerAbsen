import qrcode
from cryptography.fernet import Fernet
from PIL import Image

# Membuat kunci untuk dekripsi dan enkripsi
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Enkripsi Data
def generate_encrypted_qr(data, qr_filename='code1.png', key_filename='encryption_key.key'):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(encrypted_data.decode())
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(qr_filename)
    img = Image.open(qr_filename)
    img.show()

    # Menyimpan kunci enkripsi untuk dekripsi
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)

    print(f"QR code saved as '{qr_filename}' and encryption key saved as '{key_filename}'.")

# Data yang akan di enkripsi (Berupa Link Absen)
print("Pilih Link Absen Siapa?")
print("1. Haleluya Noka")
print("2. Bambang")
print("3. Budi")
print("4. Heru")
pilihan = input("Masukan input : ")

if pilihan == "1":
        generate_encrypted_qr("https://docs.google.com/forms/d/e/1FAIpQLSdLKeQyw8_8UgB585wvt-xDKKwJcjw0AKJm_iMkNdP41jbtTg/formResponse?usp=pp_url&entry.1899629078=HALELUYA+NOKA&entry.233006226=HADIR")
elif pilihan == "2":
        generate_encrypted_qr("https://docs.google.com/forms/d/e/1FAIpQLSdLKeQyw8_8UgB585wvt-xDKKwJcjw0AKJm_iMkNdP41jbtTg/formResponse?usp=pp_url&entry.1899629078=BAMBANG&entry.233006226=HADIR")
elif pilihan == "3":
        generate_encrypted_qr("https://docs.google.com/forms/d/e/1FAIpQLSdLKeQyw8_8UgB585wvt-xDKKwJcjw0AKJm_iMkNdP41jbtTg/formResponse?usp=pp_url&entry.1899629078=BUDI&entry.233006226=HADIR")
elif pilihan == "4":
       generate_encrypted_qr("https://docs.google.com/forms/d/e/1FAIpQLSdLKeQyw8_8UgB585wvt-xDKKwJcjw0AKJm_iMkNdP41jbtTg/formResponse?usp=pp_url&entry.1899629078=BUDI&entry.233006226=HADIR")
else:
       print("Pilihan diluar input!")