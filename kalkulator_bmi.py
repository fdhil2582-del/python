berat = int(input("masukan berat badan anda (kg): "))
tinggi = float (input("masukan tingi badan anda (cm): "))

BMI = berat / ((tinggi/100)**2)

if (BMI < 18,5) :
    kategori = "kurus (underweight)"
    katerangan = "perlu perlu tambah berat badan"
elif (BMI < 24.9) :
    kategori = "normal (ideal)"
    katerangan = "pertahankan gaya hidup sehat"
elif (BMI <  29.5) :
    kategori = "gemuk (Overweight)"
    katerangan = "perlu olahraga lebih"
else :
    kategori = "obesitas"
    katerangan = "konsultasi dokter"

print("nilai BMI :", BMI)
print("kategori : ", kategori)
print("keterangan:", keterangan)