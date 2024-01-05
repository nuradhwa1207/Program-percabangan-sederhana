# menentukan keterangan mahasiswa berdasarkan nilai ujian dan absensi,
keterangan = "Lulus" 
nilai_ujian = 70
absensi = 75

# Percabangan bersarang untuk menghitung absensi
if keterangan == "Lulus": 
    if nilai_ujian > 69:
        absensi = 15

    else:
        keterangan = "Tidak Lulus"

elif keterangan == "Tidak Lulus": 
    if nilai_ujian < 70: 
        absensi = 15
    else: 
        keterangan = "Lulus"
else:
    keterangan = "Tidak Lulus"

# Output hasil
print("Nilai Kelulusan:", keterangan)
print("Nilai Ujian:", nilai_ujian)
print("Absensi:", absensi )