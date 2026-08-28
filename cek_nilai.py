# program cek kondisi nilai
nana  = input("nama siswa:")
nilai  = int(input("nilai ujian :"))
hadir  = input("hadir 80%? (ya/tidak): ")

# operator perbandingan 
print()
print("==HASIL CEK ===")
print("NILAI >= 75 :", nilai >= 75)
print("NILAI >= 90 :", nilai >= 90)
print("NILAI antara 75-89:",nilai >= 75 and nilai <= 89)

# operator logika
hadir_ok = hadir == "ya"
lulus    = nilai >= 75 and hadir_ok
remedial = nilai <  75 or not hadir_ok

print("LULUS        :", lulus)
print("perlu remedial:", remedial)
