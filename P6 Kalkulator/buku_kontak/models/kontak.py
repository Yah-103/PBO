# models/kontak.py
class Kontak:
    """Class untuk menyimpan informasi kontak"""
    
    def __init__(self, nama, nomor_telepon):
        """
        Constructor untuk membuat objek kontak baru
        
        Args:
            nama (str): Nama kontak
            nomor_telepon (str): Nomor telepon kontak
        """
        self._nama = nama
        self._nomor_telepon = nomor_telepon
    
    @property
    def nama(self):
        """Getter untuk mendapatkan nama kontak"""
        return self._nama
    
    @nama.setter
    def nama(self, nama_baru):
        """Setter untuk mengubah nama kontak"""
        if nama_baru and nama_baru.strip():
            self._nama = nama_baru
        else:
            print("Nama tidak boleh kosong!")
    
    @property
    def nomor_telepon(self):
        """Getter untuk mendapatkan nomor telepon"""
        return self._nomor_telepon
    
    @nomor_telepon.setter
    def nomor_telepon(self, nomor_baru):
        """Setter untuk mengubah nomor telepon"""
        if nomor_baru and nomor_baru.strip():
            self._nomor_telepon = nomor_baru
        else:
            print("Nomor telepon tidak boleh kosong!")
    
    def tampilkan_info(self):
        """Method untuk menampilkan informasi kontak"""
        print(f"Nama: {self._nama}")
        print(f"Nomor Telepon: {self._nomor_telepon}")
        print("-" * 30)
    
    def __str__(self):
        """Method untuk representasi string dari objek kontak"""
        return f"{self._nama} - {self._nomor_telepon}"