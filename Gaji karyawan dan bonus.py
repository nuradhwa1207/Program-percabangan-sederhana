# Contoh Masalah 1: Menghitung Gaji Karyawan dengan Bonus

# Input data
nilai_kinerja = "Baik" 
tahun_bekerja = 6 
gaji_pokok =  5000000

# Percabangan bersarang untuk menghitung bonus
if nilai_kinerja == "Baik": 
    if tahun_bekerja > 5:
        bonus = 0.1 * gaji_pokok 
    else:
        bonus = 0

elif nilai_kinerja == "Cukup": 
    if tahun_bekerja > 3: 
        bonus = 0.05 * gaji_pokok
    else: 
        bonus = 0

else:
    bonus = 0

#Hitung total gaji

total_gaji = gaji_pokok + bonus

# Output hasil
print("Gaji Pokok:", gaji_pokok)
print("Bonus:", bonus)
print("Total Gaji:", total_gaji)