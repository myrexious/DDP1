# import os

def main():
    nama_file = input("Masukkan nama File: ")
    data_masukan = open(nama_file,'r')

    """ Cara membaca file boleh juga dilakukan dengan ini: """
    #data_masukan =  open(os.path.join(os.path.dirname(__file__),nama_file),'r')
    
    isi_file = [] # Membuat list untuk menampung isi dari file
    kata_utuh = "" # Untuk menampung string baru hasil penggabungan potongan - potongan
    
    for baris in data_masukan:
        isi_file.append(baris)

    X = int(isi_file[0].strip()) # Menghilangkan \n 
    Y = int(isi_file[1].strip()) # Menghilangkan \n

    if X == 0: # Kasus Pertama apabila X = 0
        print("Masukan Tidak Valid")
    else:
        Z = 1
        for i in isi_file[2:] :
            if len(i.strip()) < (Y+Z):
                kata_utuh = "Masukan Tidak Valid" # Kasus kedua, di mana panjang kata < Y+Z
                break
            else:
                kata_utuh += i[:Y+Z+1]
            Z += 1
        print(kata_utuh) # Print string baru hasil penggabungan

        # Bonus
        nama_output = nama_file[:nama_file.rfind(".")] + ".out"
        file_output = open(nama_output, 'w')
        print(kata_utuh, file=file_output)
        file_output.close()

if __name__ == "__main__":
    main()

# Jika ada yang kebingungan, bisa ditanyakan kepada asdosnya masing - masing ya!
# - RPG - (Bonus: SMA)
