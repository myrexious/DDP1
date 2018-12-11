# Import
from tkinter import *

# Dictionary kosong
nasabah = {} # Dictionary dari daftar nasabah yang disimpan, dengan key adalah nama, dengan value adalah objek
keuntungan_bank = 0 # Menyimpan keuntungan bank
limit_saldo = { "weaboo" : 50000000,
                "riajuu" : 30000000,
                "normies" : 10000000 }
class Akun:                                                                         
    def __init__(self, pemilik, saldo, tipe_tabungan):
        self.pemilik = pemilik
        self.saldo = int(saldo)
        self.tipe_tabungan = tipe_tabungan
        self.limit_saldo = limit_saldo[tipe_tabungan]

    #Fungsi yang digunakan saat melakukan deposit
    def deposit(self, nominal):
        global keuntungan_bank
        if self.saldo + nominal > self.limit_saldo:
            kelebihan = (self.saldo+nominal)-self.limit_saldo
            keuntungan_bank += kelebihan
            self.saldo += nominal - kelebihan
            return "Transaksi Berhasil! Uang Masuk {}".format(nominal-kelebihan)
        return "Transaksi Berhasil! Uang Masuk {}".format(nominal)
        #Implementasi deposit

    #Fungsi yang digunakan saat menarik uang
    def tarik(self, nominal):
        if nominal > self.saldo:
            return "Transaksi gagal! Saldo tidak cukup!"
        else:
            self.saldo -= nominal
            return "Berhasil menarik sebesar {}".format(nominal)
        # TODO : Implementasi tarik

    def transfer(self, tujuan, nominal):
        global keuntungan_bank
        if self.saldo < nominal:
            return "Transaksi gagal! Saldo tidak cukup!"
        else:
            if tujuan.saldo + nominal <= tujuan.limit_saldo:
                tujuan.saldo += nominal
                return "Berhasil transfer sebesar {} !".format(nominal)
            else:
                kelebihan = (tujuan.saldo+nominal)-tujuan.limit_saldo
                keuntungan_bank += kelebihan
                tujuan.saldo += nominal-kelebihan
                return "Berhasil transfer sebesar {} !".format(nominal-kelebihan)
        # TODO : Implementasi transfer
        
    def hutang(self, tujuan, nominal, tipe):
        if self.tipe_tabungan == 'weaboo':
            kembalian = nominal + (0.2*nominal)
        if self.tipe_tabungan == 'riajuu':
            kembalian = nominal + (0.15*nominal)
        if self.tipe_tabungan == 'normies':
            kembalian = nominal + (0.1*nominal)
        tujuan.saldo -= nominal
        return "Uang yang harus dikembalikan {}!".format(kembalian)
        # TODO : Implementasi hutang

class Weaboo(Akun):
    bunga = 0.2
    def __init__(self, pemilik, saldo):
        super().__init__(pemilik, saldo, "weaboo")
    
    def hutangan(self, tujuan, nominal):
        tujuann = tujuan
        nominall = nominal
        super().hutang(tujuann, nominall, "weaboo")

    

class Riajuu(Akun):
    bunga = 0.15
    def __init__(self, pemilik, saldo):
        super().__init__(pemilik, saldo, "riajuu")
    
    def hutangan(self, tujuan, nominal):
        tujuann = tujuan
        nominall = nominal
        super().hutang(tujuann, nominall, "riajuu")


class Normies(Akun):
    bunga = 0.1
    def __init__(self, pemilik, saldo):
        super().__init__(pemilik, saldo, "normies")
    
    def hutangan(self, tujuan, nominal):
        tujuann = tujuan
        nominall = nominal
        super().hutang(tujuann, nominall, "normies")
    


# =================== Fungsi yang dijalankan oleh tombol ===================== #



def deposit_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk deposit ditekan
    orang1 = akun_entry.get()
    nomnom = nominal_entry.get()
    pesan['text'] = nasabah[orang1].deposit(nomnom)
    #Implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
    
def tarik_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk tarik ditekan
    orang1 = akun_entry.get()
    nomnom = nominal_entry.get()
    pesan['text'] = nasabah[orang1].tarik(nomnom)
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
        
def transfer_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk transfer ditekan
    orang1 = akun_entry.get()
    orang2 = tujuan_entry.get()
    orang2 = nasabah[orang2]
    nomnom = nominal_entry.get()
    pesan['text'] = nasabah[orang1].transfer(orang2, nomnom)
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
        
def hutang_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk hutang ditekan
    orang1 = akun_entry.get()
    global orang2
    orang2 = tujuan_entry.get()
    orang2 = nasabah[orang2]
    nomnom = nominal_entry.get()
    pesan['text'] = nasabah[orang1].hutang(orang2, nomnom, nasabah[orang1].__class__.bunga)
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label

def keuntungan_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk keuntungan ditekan
    pesan['text']=keuntungan_bank
    #TODO : Implementasi untuk mengganti label



# =================== Fungsi utama yang dijalankan ===================== #

def main():
    try:
        #membaca file yang telah disediakan
        read_file = open("data_nasabah.in", 'r')
    except IOError:
        #mengatasi kemungkinan Error yang terjadi saat program dijalankan
        print("File salah atau tidak ada, Silakan coba kembali. Program akan keluar")
        exit()

    #Membaca file yang digunakan dalam menjalankan program
    file = read_file.readlines()

    #Pengulangan yang digunakan untuk memisahkan tiap elemen dalam file yang digunakan
    for baris in file:
        baris = baris.split()
        jenis = baris[0]
        nama = baris[1]
        nominal = baris[2]
        if jenis.lower() == 'weaboo':
            nasabah[nama] = Weaboo(nama, nominal)
        elif jenis.lower() == 'riajuu':
            nasabah[nama] = Riajuu(nama, nominal)
        elif jenis.lower() == 'normies':
            nasabah[nama] = Normies(nama, nominal)
        else:
            print("WRONG INPUT!")
        #Selection untuk membaca input

    # ======== Inisiasi GUI ========== #

    root = Tk()
    root.title("Bank Quanta")
    root.minsize(400, 100)

    # Membuat label
    global pesan
    pesan=Label(root, text='Terbang Menuju Angkasa')
    pesan.grid(row=0, column=1)

    akun = Label(root, text='Akun')
    tujuan = Label(root, text='Tujuan')
    nominal = Label(root, text='Nominal')
    akun.grid(row=1, column=0)
    tujuan.grid(row=2, column=0)
    nominal.grid(row=3, column=0)

    #Membuat entry
    global akun_entry
    global tujuan_entry
    global nominal_entry

    akun_entry = StringVar()
    tujuan_entry = StringVar()
    nominal_entry = IntVar()    

    entry_akun = Entry(root, textvar=akun_entry)
    entry_tujuan = Entry(root, textvar=tujuan_entry)
    entry_nominal = Entry(root, textvar=nominal_entry)

    entry_akun.grid(row=1, column=1)
    entry_tujuan.grid(row=2, column=1)
    entry_nominal.grid(row=3, column=1)


    #membuat button
    button_deposit = Button(root, text="Deposit", command=deposit_action)
    button_tarik = Button(root, text="Tarik", command=tarik_action)
    button_transfer = Button(root, text="Transfer", command=transfer_action)
    button_hutang = Button(root, text="Hutang", command=hutang_action)
    button_keuntungan = Button(root, text="Keuntungan", command=keuntungan_action)

    button_deposit.grid(row=4,column=0)
    button_tarik.grid(row=4,column=1)
    button_transfer.grid(row=4,column=2)
    button_hutang.grid(row=4,column=3)
    button_keuntungan.grid(row=4,column=4)

    # TODO: Lakukan implementasi GUI lanjutan di sini, sepertri membuat form, membuat tombol dan action pemanggilan button

    root.mainloop()

if __name__=='__main__':
    main()