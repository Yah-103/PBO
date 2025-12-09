class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_beli = []
    
    def beli_laptop(self, toko, laptop):
        print(f"\n{self.nama} ingin membeli {laptop.merk}...")
        toko.jual_laptop(laptop, self)
    
    def tampilkan_pembelian(self):
        print(f"\n=== Daftar Pembelian {self.nama} ===")
        if not self.daftar_beli:
            print("Belum ada pembelian")
        else:
            total = 0
            for i, laptop in enumerate(self.daftar_beli, 1):
                print(f"{i}. {laptop.merk} - Rp{laptop.harga:,}")
                total += laptop.harga
            print(f"Total Pembelian: Rp{total:,}")