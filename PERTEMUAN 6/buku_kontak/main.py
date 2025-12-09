# main.py
from models.kontak import Kontak

def main():
    """Fungsi utama program"""
    print("=" * 50)
    print("    APLIKASI BUKU KONTAK SEDERHANA")
    print("=" * 50)
    print()
    
    daftar_kontak = []
    
    # Membuat beberapa objek kontak
    print("Membuat kontak baru...")
    print("-" * 30)
    
    # Kontak 1
    kontak1 = Kontak("Patrick Star", "081234567890")
    daftar_kontak.append(kontak1)
    print(f"✓ Kontak '{kontak1.nama}' berhasil ditambahkan")
    
    # Kontak 2
    kontak2 = Kontak("Spongebob", "087765432100")
    daftar_kontak.append(kontak2)
    print(f"✓ Kontak '{kontak2.nama}' berhasil ditambahkan")
    
    # Kontak 3
    kontak3 = Kontak("Squidward", "089876543210")
    daftar_kontak.append(kontak3)
    print(f"✓ Kontak '{kontak3.nama}' berhasil ditambahkan")
    
    # Kontak 4
    kontak4 = Kontak("Mr. Crab", "081122334455")
    daftar_kontak.append(kontak4)
    print(f"✓ Kontak '{kontak4.nama}' berhasil ditambahkan")
    
    print()
    print("=" * 50)
    print("    DAFTAR KONTAK TERSIMPAN")
    print("=" * 50)
    print()
    
    for i, kontak in enumerate(daftar_kontak, 1):
        print(f"Kontak #{i}")
        kontak.tampilkan_info()
    
    print()
    print("=" * 50)
    print("    DEMONSTRASI GETTER DAN SETTER")
    print("=" * 50)
    print()
    
    print("Menggunakan getter untuk mengakses data:")
    print(f"Nama kontak pertama: {kontak1.nama}")
    print(f"Nomor telepon kontak pertama: {kontak1.nomor_telepon}")
    print()
    
    print("Menggunakan setter untuk mengubah data:")
    print(f"Nama lama: {kontak1.nama}")
    kontak1.nama = "Patrick Bintang"
    print(f"Nama baru: {kontak1.nama}")
    print()
    
    print(f"Nomor lama: {kontak1.nomor_telepon}")
    kontak1.nomor_telepon = "081999888777"
    print(f"Nomor baru: {kontak1.nomor_telepon}")
    print()
    
    print("Mencoba mengubah nama dengan nilai kosong:")
    kontak1.nama = ""
    print(f"Nama tetap: {kontak1.nama}")
    print()
    
    print("=" * 50)
    print("    DAFTAR KONTAK FINAL")
    print("=" * 50)
    print()
    
    for i, kontak in enumerate(daftar_kontak, 1):
        print(f"{i}. {kontak}")
    
    print()
    print("=" * 50)
    print("Program selesai. Terima kasih!")
    print("=" * 50)

if __name__ == "__main__":
    main()