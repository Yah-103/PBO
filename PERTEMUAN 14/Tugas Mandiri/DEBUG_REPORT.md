# DEBUG_REPORT.md

## Laporan Debug - DiskonCalculator Bug PPN 10%

### 1. Deskripsi Bug
**Bug**: PPN 10% dihitung dari harga awal, bukan dari harga setelah diskon. Ini menyebabkan pelanggan membayar PPN lebih tinggi dari yang seharusnya.

**Contoh**:
- Harga awal: Rp 1.000
- Diskon 10%: Rp 1.000 - Rp 100 = Rp 900
- **Bug**: PPN dihitung dari Rp 1.000 → PPN = Rp 100
- **Benar**: PPN seharusnya dihitung dari Rp 900 → PPN = Rp 90

**Dampak**: 
- Hasil dengan bug: Rp 900 + Rp 100 = **Rp 1.000**
- Hasil yang benar: Rp 900 + Rp 90 = **Rp 990**

---

### 2. Langkah Debugging dengan pdb

#### A. Aktivasi Debugger
File `diskon_service.py` baris 9: Aktifkan `pdb.set_trace()`

#### B. Eksekusi Program
```bash
$ python diskon_service.py
```

#### C. Penelusuran dengan pdb

**Input Test**: `hitung_diskon(1000, 10)`

**Session pdb**:
```
> /path/diskon_service.py(12)hitung_diskon()
-> jumlah_diskon = harga_awal * persentase_diskon / 100

(Pdb) n
> /path/diskon_service.py(13)hitung_diskon()
-> harga_setelah_diskon = harga_awal - jumlah_diskon

(Pdb) p harga_awal
1000

(Pdb) p persentase_diskon
10

(Pdb) p jumlah_diskon
100.0

(Pdb) n
> /path/diskon_service.py(16)hitung_diskon()
-> ppn = harga_awal * 0.10

(Pdb) p harga_setelah_diskon
900.0

(Pdb) n
> /path/diskon_service.py(17)hitung_diskon()
-> harga_akhir = harga_setelah_diskon + ppn

(Pdb) p ppn
100.0

(Pdb) p harga_awal
1000

(Pdb) n
> /path/diskon_service.py(19)hitung_diskon()
-> return harga_akhir

(Pdb) p harga_akhir
1000.0

(Pdb) c
Hasil: 1000.0
```

---

### 3. Identifikasi Akar Masalah

**Lokasi Bug**: Baris 16 di `diskon_service.py`

**Kode Bermasalah**:
```python
ppn = harga_awal * 0.10
```

**Analisis**:
- `harga_awal` = 1000
- `harga_setelah_diskon` = 900.0
- `ppn` = 1000 × 0.10 = **100.0**
- `harga_akhir` = 900.0 + 100.0 = **1000.0** 

**Kesimpulan**: PPN dihitung dari `harga_awal` padahal seharusnya dihitung dari `harga_setelah_diskon`. Ini menyebabkan pelanggan membayar PPN lebih tinggi.

---

### 4. Solusi Perbaikan

**Kode yang Diperbaiki**:
```python
ppn = harga_setelah_diskon * 0.10
harga_akhir = harga_setelah_diskon + ppn
```

**Atau lebih ringkas**:
```python
harga_akhir = harga_setelah_diskon * 1.10
```

---

### 5. Verifikasi Hasil

**Sebelum Perbaikan**:
- Input: `hitung_diskon(1000, 10)`
- Output: **1000.0** 

**Setelah Perbaikan**:
- Input: `hitung_diskon(1000, 10)`
- Output: **990.0** 

---