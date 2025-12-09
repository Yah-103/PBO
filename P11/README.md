# Refactoring Sistem Validasi Registrasi Mahasiswa  
Penerapan SRP, OCP, dan DIP (SOLID Principles)

## 1. Deskripsi Singkat
Project ini merupakan hasil refactoring dari sistem validasi registrasi mahasiswa yang awalnya menggunakan satu kelas (`ValidatorManager`) dengan banyak kondisi `if/else` untuk memvalidasi:
- Batas maksimum SKS
- Prasyarat mata kuliah

Refactoring dilakukan dengan menerapkan prinsip **SOLID**, khususnya:
- SRP (Single Responsibility Principle)
- OCP (Open/Closed Principle)
- DIP (Dependency Inversion Principle)

---

## 2. Analisis Pelanggaran pada Kode Awal

### a. Pelanggaran SRP (Single Responsibility Principle)
Pada kode awal, `ValidatorManager` memiliki lebih dari satu tanggung jawab:
- Menghitung total SKS
- Mengecek prasyarat mata kuliah
- Menentukan status validasi

Hal ini melanggar SRP karena satu kelas memiliki banyak alasan untuk berubah.

---

### b. Pelanggaran OCP (Open/Closed Principle)
Jika ingin menambahkan aturan validasi baru (misalnya validasi jadwal bentrok), maka:
- Harus menambah `if/else` baru di dalam method yang sama.
- Artinya class tidak tertutup terhadap modifikasi.

---

### c. Pelanggaran DIP (Dependency Inversion Principle)
Kode awal langsung bergantung pada detail implementasi logika:
- Tidak ada abstraksi
- Tidak ada kontrak interface
- High-level module langsung mengatur detail teknis

Ini menyebabkan kode sulit dikembangkan dan diuji.

---

## 3. Hasil Refactoring

### a. Abstraksi Validasi
Dibuat interface:

```python
class IValidationRule(ABC):
    @abstractmethod
    def validate(self, data):
        pass