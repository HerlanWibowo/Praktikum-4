jawab = "y"
No = 0
Nama = []
Nim = []
NilaiTugas = []
NilaiUts = []
NilaiUas = []
NilaiAkhir = []

while (jawab == "y"):
    Nama.append(str(input("Nama : ")))
    Nim.append(int(input("Nim : ")))
    NilaiTugas.append(int(input("Nilai Tugas : ")))
    NilaiUts.append(int(input("Nilai UTS : ")))
    NilaiUas.append(int(input("Nilai UAS : ")))
    jawab = str(input("Tambah Data (y/t)?"))
    No +=1

for i in range (No) :
    NilaiAkhir.append(((NilaiTugas[i])*30/100)+((NilaiUts[i])*30/100)+((NilaiUas[i])*35/100))
    print("="*115)
    print("No \t| Nama \t| Nim \t| Nilai Tugas \t| Nilai UTS \t| Nilai UAS \t| Nilai Akhir |")
    print("="*115)

for i in range (No) :
        print(No,"\t|",Nama[i],"\t|",Nim[i],"\t|",NilaiTugas[i],"\t\t|",NilaiUts[i],"\t\t|",NilaiUas[i],"\t\t|",NilaiAkhir[i],"\t\t|");
        print("="*115)
        
