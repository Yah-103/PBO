class Laptop:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        self.tersedia = True
    
    def info_laptop(self):
        status = "Tersedia" if self.tersedia else "Terjual"
        return f"Laptop {self.merk}, Harga: Rp{self.harga:,}, Status: {status}"