# test_diskon_advanced.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase):
    """Test case lanjutan untuk DiskonCalculator dengan PPN."""
    
    def setUp(self):
        """Arrange: Siapkan instance calculator."""
        self.calc = DiskonCalculator()
    
    # ===== TEST CASE FLOAT (Desimal) =====
    
    def test_diskon_33_persen_pada_999(self):
        """Tes 5: Memastikan diskon 33% pada 999 menghasilkan nilai desimal yang benar."""
        # Arrange
        harga = 999
        diskon = 33
        
        # Act
        hasil = self.calc.hitung_diskon(harga, diskon)
        
        # Assert - gunakan assertAlmostEqual untuk float
        self.assertAlmostEqual(hasil, 736.263, places=2,
                             msg="Perhitungan diskon 33% pada 999 tidak akurat")
    
    
    def test_harga_awal_nol(self):
        """Tes 6 (Edge Case): Memastikan harga 0 dengan diskon apapun tetap menghasilkan 0."""
        # Arrange
        harga = 0
        diskon = 50
        
        # Expected: 0 - 0 = 0, PPN: 0 * 0.10 = 0, Total: 0
        
        # Act
        hasil = self.calc.hitung_diskon(harga, diskon)
        
        # Assert
        self.assertEqual(hasil, 0.0,
                        msg="Harga awal 0 harus menghasilkan harga akhir 0")


if __name__ == '__main__':
    unittest.main(verbosity=2)