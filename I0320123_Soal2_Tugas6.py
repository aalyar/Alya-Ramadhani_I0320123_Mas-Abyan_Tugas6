nilai = int(input("\nMasukkan jumlah data: "))

print()
data = []
jumlah = 0

for i in range(0, nilai):
    temp = int(input("Masukkan nilai ke-%d: " % (i+1)))
    data.append(temp)
    jumlah += data[i]
    rata_rata = jumlah / nilai

print("\nNilai rata-rata  = %0.2f" % rata_rata)
