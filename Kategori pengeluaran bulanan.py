# Tuliskan algoritma untuk sebuah masalah, kemudian implementasikan menjadi program python:
# 2. Penentuan kategori pengeluaran bulanan berdasarkan besarnya nominal

pengeluaran = float(input("Masukan pengeluaran selama sebulan: Rp. "))

if pengeluaran >= 3000000 :
    print("Kategori pengeluaran bulanan anda Tinggi")

elif pengeluaran >= 1500000 :
    print("Kategori pengeluaran bulanan anda Sedang")

else:
    print("Kategori pengeluaran bulanan anda Rendah")