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
        pass
        # TODO : Implementasi deposit

    #Fungsi yang digunakan saat menarik uang
    def tarik(self, nominal):
        pass
        # TODO : Implementasi tarik

    def transfer(self, tujuan, nominal):
        global keuntungan_bank
        pass
        # TODO : Implementasi transfer
        
    def hutang(self, tujuan, nominal, bunga):
        pass # TODO : Implementasi hutang

class Weeabo(Akun):
    def __init__(self, pemilik, saldo):
        super().__init__(pemilik, saldo, "weaboo")
        
    def hutang(self, tujuan, nominal):
        pass # TODO : Implementasi memanggil dari superclass

class Riajuu(Akun):
    def __init__(self, pemilik, saldo):
        pass # TODO : Implementasi memanggil dari superclass

    def hutang(self, penerima, nominal):
        pass # TODO : Implementasi memanggil dari superclass

class Normies(Akun):
    def __init__(self, pemilik, saldo):
        pass # TODO : Implementasi memanggil dari superclass

    def hutang(self, penerima, nominal):
        pass # TODO : Implementasi memanggil dari superclass

# =================== Fungsi yang dijalankan oleh tombol ===================== #



def deposit_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk deposit ditekan
    pass
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
    
def tarik_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk tarik ditekan
    pass
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
        
def transfer_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk transfer ditekan
    pass
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label
        
def hutang_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk hutang ditekan
    pass
    # TODO : Lakukan implementasi untuk mengambil data dari form, lalu memanggil fungsi untuk melakukan hutang, lalu mengganti label

def keuntungan_action(): #Ini adalah fungsi yang akan dipanggil saat button untuk keuntungan ditekan
    pass
    #TODO : Implementasi untuk mengganti label



# =================== Fungsi utama yang dijalankan ===================== #


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
    pass
    # TODO: Lakukan selection untuk membaca input



# ======== Inisiasi GUI ========== #

# Lakukan implementasi GUI lanjutan di 
window = Tk()
window.title("Bank Quanta")
window.minsize(400, 100)

# Membuat label
pesan = Label(window, text = 'Terbang Menuju Angkasa')
pesan.grid(row=0, column=1)

# TODO: Lakukan implementasi GUI lanjutan di sini, sepertri membuat form, membuat tombol dan action pemanggilan button

window.mainloop()
