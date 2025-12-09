class Toko:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.stok_laptop = []
    
    def tambah_laptop(self, laptop):
        self.stok_laptop.append(laptop)
        print(f"Laptop {laptop.merk} berhasil ditambahkan ke {self.nama_toko}")
    
    def tampilkan_stok(self):
        print(f"\n=== Stok Laptop di {self.nama_toko} ===")
        if not self.stok_laptop:
            print("Stok kosong")
        else:
            for i, laptop in enumerate(self.stok_laptop, 1):
                print(f"{i}. {laptop.info_laptop()}")
    
    def jual_laptop(self, laptop, pelanggan):
        if laptop in self.stok_laptop and laptop.tersedia:
            laptop.tersedia = False
            pelanggan.daftar_beli.append(laptop)
            print(f"\n{pelanggan.nama} berhasil membeli {laptop.merk} seharga Rp{laptop.harga:,}")
            return True
        else:
            print(f"\nMaaf, laptop {laptop.merk} tidak tersedia")
            return False