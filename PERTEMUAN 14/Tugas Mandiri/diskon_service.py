# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon dengan PPN 10%."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        
        # pdb.set_trace()  # <-- Untuk Debugging
        
        # Hitung diskon
        jumlah_diskon = harga_awal * persentase_diskon / 100
        harga_setelah_diskon = harga_awal - jumlah_diskon
        
        # Hitung PPN 10% dari harga setelah diskon
        ppn = harga_setelah_diskon * 0.10  # Benar!
        harga_akhir = harga_setelah_diskon + ppn
        
        return harga_akhir


# --- UJI COBA ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    
    # Test: 1000 dengan diskon 10%
    # Expected: (1000 - 100) + (900 * 0.10) = 900 + 90 = 990.0
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")
    print(f"Status: {'✓ PASS' if hasil == 990.0 else '✗ FAIL'}")