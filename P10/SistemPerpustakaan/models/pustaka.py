class Pustaka:
    def __init__(self):
        self.koleksi_buku = []
    
    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)
    
    def tampilkan_koleksi(self):
        for buku in self.koleksi_buku:
            print(buku.tampilkan_info())