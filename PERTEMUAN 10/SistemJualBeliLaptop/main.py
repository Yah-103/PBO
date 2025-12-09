from models.laptop import Laptop
from models.toko import Toko
from models.pelanggan import Pelanggan

print("="*50)
print("SISTEM JUAL BELI LAPTOP SEDERHANA")
print("="*50)

toko1 = Toko("Toko Laptop Jaya")

laptop1 = Laptop("Asus ROG", 15000000)
laptop2 = Laptop("Lenovo ThinkPad", 12000000)
laptop3 = Laptop("Acer Predator", 18000000)
laptop4 = Laptop("HP Pavilion", 9000000)

toko1.tambah_laptop(laptop1)
toko1.tambah_laptop(laptop2)
toko1.tambah_laptop(laptop3)
toko1.tambah_laptop(laptop4)

toko1.tampilkan_stok()

pelanggan1 = Pelanggan("Budi")
pelanggan2 = Pelanggan("Siti")

pelanggan1.beli_laptop(toko1, laptop1)
pelanggan1.beli_laptop(toko1, laptop3)
pelanggan2.beli_laptop(toko1, laptop2)

pelanggan2.beli_laptop(toko1, laptop1)

pelanggan1.tampilkan_pembelian()
pelanggan2.tampilkan_pembelian()

toko1.tampilkan_stok()