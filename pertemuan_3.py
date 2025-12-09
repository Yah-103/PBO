# Langkah 1 - Mengenali Masalahnya
class User:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def info(self):
        print(f"Username: {self.username}, Level: {self.level}")

user_1 = User("admin_ganteng", "Super Admin")
user_1.info()

print("\nMerusak data dari luar class!")
user_1.level = 12345
user_1.username = ""
user_1.info()

# Langkah 2 - Menerapkan Atribut Privat

class User:
    def __init__(self, username, level):
        self.username = username
        self.__level = level

    def info(self):
        print(f"Username: {self.username}, Level: {self.__level}")

user_1 = User("admin_ganteng", "Super Admin")
user_1.info()

try:
    print(user_1.__username)
except AttributeError as e:
    print(f"\nError: {e}")
    print("Atribut __username tidak bisa diakses langsung!")

# Langkah 3 - Membuat Getter untuk Membaca Data

class User:
    def __init__(self, username, level):
        self.__username = username
        self.__level = level

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

user_1 = User("admin_ganteng", "Super Admin")

print("\n--- Mengakses data via Getter ---")
nama_user = user_1.get_username()
level_user = user_1.get_level()

print(f"Username dari getter: {nama_user}")
print(f"Level dari getter: {level_user}")

# Langkah 4 - Membuat Setter dengan Validasi untuk Mengubah Data

class User:
    def __init__(self, username, level):
        self.__username = ""
        self.__level = ""
        self.set_username(username)
        self.set_level(level)

    def info(self):
        print(f"Username: {self.__username}, Level: {self.__level}")

    def get_username(self):
        return self.__username

    def get_level(self):
        return self.__level

    def set_username(self, username_baru):
        if len(username_baru) > 5:
            self.__username = username_baru
            print("Username berhasil diubah.")
        else:
            print(f"Error: Username terlalu pendek! Minimal 6 karakter.")

    def set_level(self, level_baru):
        allowed_levels = ["User", "Admin", "Super Admin"]
        if level_baru in allowed_levels:
            self.__level = level_baru
            print("Level berhasil diubah.")
        else:
            print(f"Error: Level {level_baru} tidak valid!")

user_1 = User("pengguna_baru", "User")
user_1.info()

print("\n--- Mencoba mengubah data via Setter ---")
user_1.set_level("Moderator") 

print("\n--- Mencoba lagi dengan data yang valid ---")
user_1.set_username("administrator_sistem") 
user_1.set_level("Admin") 
user_1.info() 

# D. Latihan Mandiri

class Karyawan:
    def __init__(self, nama, id_karyawan, gaji):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__gaji = gaji

    def get_nama(self):
        return self.__nama

    def get_id(self):
        return self.__id_karyawan

    def get_gaji(self):
        return self.__gaji

    def set_nama(self, nama_baru):
        if nama_baru != "":
            self.__nama = nama_baru
            print("Nama berhasil diubah.")
        else:
            print("Error: Nama tidak boleh kosong!")

    def set_gaji(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji = gaji_baru
            print("Gaji berhasil diubah.")
        else:
            print("Error: Gaji harus lebih besar dari 0!")

karyawan_1 = Karyawan("Yahya", "2411102441255", 2000000)

print("\n--- Informasi Karyawan ---")
print(f"Nama: {karyawan_1.get_nama()}")
print(f"ID Karyawan: {karyawan_1.get_id()}")
print(f"Gaji: {karyawan_1.get_gaji()}")

print("\n--- Mencoba mengubah gaji menjadi negatif ---")
karyawan_1.set_gaji(-2000000)

print("\n--- Mencoba mengubah nama menjadi kosong ---")
karyawan_1.set_nama("")

print("\n--- Mengubah gaji menjadi positif yang valid ---")
karyawan_1.set_gaji(3000000)

print("\n--- Informasi Karyawan Setelah Perubahan ---")
print(f"Nama: {karyawan_1.get_nama()}")
print(f"ID Karyawan: {karyawan_1.get_id()}")
print(f"Gaji: {karyawan_1.get_gaji()}")