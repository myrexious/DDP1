'''
Template untuk Lab 10 DDP 1 kelas F.

Samuel Ludwig Ian - 1806191471
'''
import tkinter as tk
from tkinter import filedialog


class BerlayarMenujuAsa:
    '''Program GUI BerlayarMenujuAsa.'''

    def __init__(self, master):
        '''Inisialisasi program GUI BerlayarMenujuAsa.'''
        self.master = master
        self.master.title("Berlayar Menuju Asa!")
        self.master.minsize(640, 128)
        self.lines = []
        self.saved_lines = []
        self.diolah = ''

        self.__init_message()
        self.__init_buttons()

    def __init_message(self):
        '''Membuat widget Message untuk teks utama.'''
        text = ("Berlayar\n"
                "Menuju\n"
                "Asa!")
        self.message = tk.Message(self.master, text='{}'.format(text), font="Helvetica 25 bold", width=300)
        self.message.grid(rowspan=5, column=2, row=0)
        # TODO: Buat sebuah widget Message sebagai instance variable.
        

    def __init_buttons(self):
        '''Membuat widget-widget Button untuk tombol-tombol.'''
        self.bukaberkas = tk.Button(self.master, text='Buka Berkas', height=2, width=10, command=self.load_file)
        self.mulai = tk.Button(self.master, text='Berikutnya', height=2, width=10, command=self.next_line)
        self.skiri = tk.Button(self.master, text='Sulap kiri!', height=2, width=10, command=self.magic_left)
        self.skanan = tk.Button(self.master, text='Sulap kanan!', height=2, width=10, command=self.magic_right)
        self.simpen = tk.Button(self.master, text='Simpan', height=2, width=10, command=self.save_current)

        self.bukaberkas.grid(row=0, column=0)
        self.mulai.grid(row=1, column=0)
        self.skiri.grid(row=2, column=0)
        self.skanan.grid(row=3, column=0)
        self.simpen.grid(row=4, column=0)
        # TODO: Buat widget-widget Button sebagai instance variables.
        # Jangan lupa untuk kaitkan command ke fungsi yang sesuai.
        

    def load_file(self):
        '''
        Meminta pengguna untuk memilih suatu berkas
        dan memuat isi berkas ke self.lines.
        '''
        file_name = filedialog.askopenfilename()
        if not file_name:                                   # Jika pengguna membatalkan dialog, langsung return.
            return None
        text_file = open(file_name, 'r', encoding="utf-8")
        self.lines = text_file.readlines()
        text_file.close()
        self.message["text"]='Berkas siap untuk dibaca'
        self.mulai['text']='MULAI!! :D'
        
        # TODO: Manfaatkan submodule filedialog untuk mendapatkan nama berkas.
        # TODO: Buka berkas dengan nama yang didapatkan, lalu ubah tulisan
        # pada tombol Selanjutnya menjadi MULAI!! :D.
        

    def next_line(self):
        '''
        Mengganti teks self.message dengan string yang ada di indeks ke-0 dari
        self.lines dan menghilangkan string tersebut dari self.lines.
        Jika self.lines sudah kosong, gunakan suatu string lain.
        '''
        self.mulai['text']='Berikutnya'
        isi= self.lines.pop(0)
        self.message['text'] = isi
        self.diolah = isi

        #self.message["text"]= 
        # TODO: Pastikan tombol bertuliskan Berikutnya.
        # TODO: Ubah nilai text milik widget Message.
        # Method apa yang bisa dimanfaatkan untuk mengambil data dari list
        # sekaligus menghilangkannya?
       

    def _magic(self, direction):
        '''
        Menggeser orde setiap karakter yang ada di teks message saat ini
        sebesar 1 ke arah yang ditentukan.
        '''
        hasil = ''
        try:
            if direction == 'left':
                for x in self.diolah:
                    hasil += chr(ord(x)-1)
            elif direction == 'right':
                for x in self.diolah:
                    hasil+= chr(ord(x)+1)
        except:
            print('Error, out of range')
            
        self.diolah = hasil
        return hasil

    def magic_left(self):
        '''
        Mengubah setiap karakter yang ada di teks message saat ini
        menjadi satu karakter sebelumnya.
        '''
        self.message['text'] = self._magic('left')
        

    def magic_right(self):
        '''
        Mengubah setiap karakter yang ada di teks message saat ini
        menjadi satu karakter sebelumnya.
        '''
        self.message['text'] = self._magic('right')
        
    def save_current(self):
        '''Menambahkan teks message saat ini ke self.saved_lines.'''
        self.saved_lines.append(self.diolah)
        # TODO BONUS: Tambahkan teks message saat ini ke list saved_lines.


def main():
        root = tk.Tk()
        userinterface = BerlayarMenujuAsa(root)
        root.mainloop()

        save = open('output.txt', 'w')
        for x in userinterface.saved_lines:
            save.write(x)
            save.write('\n')
        save.close()
    # TODO: Buat root_window dan instance dari BerlayarMenujuAsa di sini.
    # TODO BONUS: cetak apa yang ada di saved_lines ke output.txt.
    


if __name__ == '__main__':
    main()
