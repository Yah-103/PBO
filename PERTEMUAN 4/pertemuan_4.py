# Langkah 1 - Membuat Parent Class Character
class Character:
    def __init__(self, name, health, attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power
        print(f"{self.__name} bergabung ke dalam pertarungan!")

    def show_info(self):
        print("\n--- Character Info ---")
        print(f"Name: {self.__name}")
        print(f"Health: {self.__health}")
        print(f"Attack Power: {self.__attack_power}")

    def attack(self, target):
        print(f"{self.__name} menyerang {target.get_name()}!")
        target.take_damage(self.__attack_power)

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            print(f"{self.__name} telah dikalahkan!")
            self.__health = 0
        else:
            print(f"Health {self.__name} tersisa {self.__health}")

    def get_name(self):
        return self.__name


# Langkah 2/3 - Child Class Warrior (pakai super)
class Warrior(Character):
    def __init__(self, name, health, attack_power, armor=None):
        super().__init__(name, health, attack_power)
        self.__armor = armor
        # Cetak info armor hanya jika diberikan
        if armor is not None:
            print(f"Armor set to: {self.__armor}")


# --- Bagian Utama Program ---
print("--- Membuat Objek dari Parent Class ---")
aragorn = Character("Aragorn", 100, 15)
aragorn.show_info()

print("\n--- Membuat Objek dari Child Class ---")
# Buat Gimli (Warrior) tanpa armor dulu agar sesuai urutan output pada gambar
gimli = Warrior("Gimli", 120, 20)
gimli.show_info()

# Buktikan bahwa child class bisa menggunakan method parent
print("\n--- Pertarungan Dimulai ---")
aragorn.attack(gimli)
gimli.attack(aragorn)

# Setelah pertarungan, buat ulang Gimli dengan armor (muncul "Armor set to: 5")
gimli = Warrior("Gimli", 120, 20, 5)
gimli.show_info()

# ----------------------------------------------------------------------------------
# D. Latihan Mandiri > Studi Kasus - Sistem Klasifikasi Kendaraan
# Parent Class
class Kendaraan:
    def __init__(self, merk, tahun_produksi, warna):
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    def tampilkan_info(self):
        print("--- Info Kendaraan ---")
        print(f"Merk            : {self.__merk}")
        print(f"Tahun Produksi  : {self.__tahun_produksi}")
        print(f"Warna           : {self.__warna}")

    def nyalakan_mesin(self):
        print("Mesin kendaraan menyala.")


# Child Class: Mobil
class Mobil(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, jumlah_pintu):
        # inisialisasi atribut warisan
        super().__init__(merk, tahun_produksi, warna)
        # atribut khusus Mobil
        self.__jumlah_pintu = jumlah_pintu

    # override tampilkan_info
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jumlah Pintu    : {self.__jumlah_pintu}")

    # method spesifik mobil
    def buka_pintu_bagasi(self):
        print("Pintu bagasi dibuka.")


# Child Class: Motor
class Motor(Kendaraan):
    def __init__(self, merk, tahun_produksi, warna, kapasitas_tangki):
        # inisialisasi atribut warisan
        super().__init__(merk, tahun_produksi, warna)
        # atribut khusus Motor
        self.__kapasitas_tangki = kapasitas_tangki

    # override nyalakan_mesin
    def nyalakan_mesin(self):
        print("Brmm... Mesin motor dinyalakan dengan kick starter!")


# ===== Bagian Utama Program =====
if __name__ == "__main__":
    # a) Objek Mobil
    avanza = Mobil("Toyota Avanza", 2019, "Hitam", 5)

    # b) Objek Motor
    beat = Motor("Honda Beat", 2021, "Merah", 4.0)

    # c) Panggil semua method
    print("\n== DATA MOBIL ==")
    avanza.tampilkan_info()
    avanza.nyalakan_mesin()
    avanza.buka_pintu_bagasi()

    print("\n== DATA MOTOR ==")
    beat.tampilkan_info()
    beat.nyalakan_mesin()