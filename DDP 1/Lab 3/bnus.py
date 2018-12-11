#BilanganBasisRandom
bilangan = int(input("Bilangan yang akan dikonversi : "))
basis = int(input("Basis bilangan tersebut"))

stringhelp=""
bilStr = str(bilangan)

if basis == 0:
    print('error')
elif basis > 10:
    print('basis terlalu besar')

hasilforsum = []
x=0
pnjg = len(bilStr)

while pnjg!= 0:
    angka = int(bilStr[-(x+1)])
    hasil = angka*(basis^x)
    hasilforsum.append(hasil)
    x += 1
    pnjg -= 1
    
print(sum(hasilforsum))

