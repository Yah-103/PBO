# [IF2143] Proyek SOLID OOP Python  
## Pertemuan 12: Dokumentasi dan Version Control

### Deskripsi Proyek
Proyek ini mendemonstrasikan implementasi prinsip SOLID (SRP, OCP, dan DIP)
pada sistem validasi registrasi mata kuliah mahasiswa menggunakan abstraksi
(interface) dan dependency injection. Selain itu, proyek ini juga menambahkan
docstring dengan format **Google Style** pada setiap class dan method, serta
pencatatan aktivitas sistem menggunakan modul `logging` dengan level
`INFO` dan `WARNING`.

Sistem ini memvalidasi beberapa aturan, yaitu:
- Batas maksimum SKS
- Prasyarat mata kuliah
- Jadwal bentrok antar mata kuliah (sebagai pembuktian OCP)

---

### Struktur File
- `registrasi.py`  
  Kode utama sistem validasi registrasi mahasiswa yang telah direfaktor
  menggunakan prinsip SOLID, dilengkapi dengan docstring dan logging.
- `README.md`  
  Dokumen penjelasan proyek ini.

---

### Cara Menjalankan
1. Pastikan Python 3.x sudah terinstal di komputer.
2. Buka terminal pada folder proyek.
3. Jalankan perintah berikut:

   ```bash
   python registrasi.py

Kode dikelola menggunakan git. Lihat https://github.com/Yah-103/PBO