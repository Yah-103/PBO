# Langkah 1 - Struktur Inheritance
class Bentuk:
    def gambar(self):
        raise NotImplementedError("Method gambar() harus diimplementasikan")
    
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def gambar(self):
        return f"Menggambar persegi dengan sisi {self.sisi}"

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius
    
    def gambar(self):
        return f"Menggambar lingkaran dengan radius {self.radius}"
    
# Langkah 2 - Polimorfisme dalam Aksi
bentuk_list = [
    Persegi(5),
    Lingkaran(3),
    Persegi(8)
]

for bentuk in bentuk_list:
    print(bentuk.gambar())

# Langkah 3 - Polimorfisme dengan Fungsi
def render_objek(objek):
    print(f"Rendering: {objek.gambar()}")

class Teks:
    def __init__(self, isi):
        self.isi = isi
    
    def gambar(self):
        return f"Menampilkan teks: '{self.isi}'"
    
# Menggunakan fungsi render_objek
objek_list = [
    Persegi(4),
    Lingkaran(2),
    Teks("Hello World!")
]

for obj in objek_list:
    render_objek(obj)


# Tugas Mandiri

class Notifikasi:
    """Kelas abstrak untuk semua jenis notifikasi"""
    def kirim(self, pesan):
        raise NotImplementedError("Metode kirim() harus diimplementasikan.")


class Email(Notifikasi):
    """Kelas untuk mengirim notifikasi via Email"""
    def kirim(self, pesan):
        print(f"[EMAIL] Mengirim: '{pesan}'")


class SMS(Notifikasi):
    """Kelas untuk mengirim notifikasi via SMS"""
    def kirim(self, pesan):
        print(f"[SMS] Mengirim: '{pesan}'")


class PushNotif(Notifikasi):
    """Kelas untuk mengirim notifikasi via Push Notification"""
    def kirim(self, pesan):
        print(f"[PUSH] Mengirim: '{pesan}'")

if __name__ == "__main__":
    notifikasi_list = [
        Email(),
        SMS(),
        PushNotif()
    ]
    
    pesan = "Diskon Spesial! Hanya untuk Anda!"
    
    print("=" * 60)
    print("SISTEM NOTIFIKASI MULTISALURAN")
    print("=" * 60)
    print()
    
    for notif in notifikasi_list:
        notif.kirim(pesan)
    
    print()
    print("=" * 60)
    print("Notifikasi berhasil dikirim ke semua saluran!")
    print("=" * 60)

print("\n\n--- BONUS: Menambah Kanal Baru (WhatsApp) ---\n")

class WhatsApp(Notifikasi):
    """Kelas baru untuk notifikasi WhatsApp - Mudah ditambahkan!"""
    def kirim(self, pesan):
        print(f"[WA] Mengirim: '{pesan}'")

notifikasi_list_extended = [
    Email(),
    SMS(),
    PushNotif(),
    WhatsApp()
]

print("Mengirim notifikasi dengan kanal tambahan:")
for notif in notifikasi_list_extended:
    notif.kirim(pesan)