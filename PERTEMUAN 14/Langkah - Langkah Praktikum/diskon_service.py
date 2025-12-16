# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # pdb.set_trace()  # <-- Untuk Debugging: Tempatkan di sini (sudah dikomentari setelah debugging selesai)
        
        # code perbaikan
        jumlah_diskon = harga_awal * persentase_diskon / 100
        
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir


# --- UJI COBA (Ini adalah test case yang sudah BERHASIL) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    # Input: 1000 - 10%. Hasil yang diharapkan: 900.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")
    # Output: Hasil: 900.0 (Benar)