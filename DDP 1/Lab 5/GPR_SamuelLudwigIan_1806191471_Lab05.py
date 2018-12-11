namafile = input("Nama file anda : ")
file = open(namafile, "r")


filelines = file.readlines()        #memisahkan text per line
baris = int(filelines[0])           #jml baris yg akan diolah
jmlkata = int(filelines[1])         #jml kata yg akan diolah

#output
output = namafile[:-3] + ".out"         #menentukan nama file output
filehasil = open(output, "wt")

hasil =""       #persiapan hasil


if baris != 0 and jmlkata <= len(filelines)-2:      #persyaratan agar valid
    for a in range(2, 2+baris):         #looping setiap baris dan pengolahan
        kata = filelines[a].strip()
        if (jmlkata+a-1)<=len(kata):
            output = kata[:(jmlkata+a)]
            hasil += output
        else:
            filehasil.write("Masukan Tidak Valid.") #memasukan validitas ke file
            filehasil.close()
            break
    filehasil.write(hasil)      #memasukan hasil ke file output
    filehasil.close()

else:
    filehasil.write("Masukan Tidak Valid.") #memasukan validitas ke file
    filehasil.close()


file.close()
