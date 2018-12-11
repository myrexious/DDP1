import tkinter as tk
from tkinter import messagebox


class Barcode(object):


    def __init__(self, master):
        self.master = master
        
        self.frametext = tk.Frame(master)
        self.frametext.pack(side=tk.TOP)
                
        '''Things in frame text'''
        self.namefile = tk.StringVar()
        self.angkainput = tk.StringVar()
        
        self.labelsave = tk.Label(self.frametext, text='Save barcode to PS file [eg: EAN13.eps]:', font=("Helvetica", 14, "bold"))
        self.entryname = tk.Entry(self.frametext, textvariable=self.namefile)
        self.labelcode = tk.Label(self.frametext, text='Enter code (first 12 decimal digits):', font=("Helvetica", 14, "bold"))
        self.entrycode = tk.Entry(self.frametext, textvariable=self.angkainput)

        self.labelsave.pack()
        self.entryname.pack()
        self.labelcode.pack()
        self.entrycode.pack()


class BarcodeImage(Barcode):


    def __init__(self, master):
        
        super().__init__(master)
        self.framebarcode = tk.Frame(master)
        self.framebarcode.pack(side=tk.BOTTOM, pady=5, padx=5)
        
        '''Things in frame barcode'''
        self.width = 450
        self.height = 450
        self.barcode = tk.Canvas(self.framebarcode, width=self.width, height=self.height, bg='white')
        self.barcode.pack(pady=5, padx=5)

        '''Binds entries'''
        self.entrycode.bind('<Return>', self.draw)
        self.entryname.bind('<Return>', self.savefile)


    def check_digit(self, number):
        digitsplit = [x for x in number]

        '''Counts the last digit'''
        ganjil = []
        genap = []

        for x in range (0, len(digitsplit), 2):
            genap.append(digitsplit[x])

        for y in range (1, len(digitsplit)+1, 2):
            ganjil.append(digitsplit[y])
        
        hasil = 0
        for n in range(6):
            hasil += int(genap[n])+(3*(int(ganjil[n])))
        
        if hasil%10 == 0:
            angkaterakhir = 0
        else:
            angkaterakhir = 10-(hasil%10)
        
        self.angka = number + str(angkaterakhir)        #Returns the original 12 number with the checksum
        return self.angka
        
    
    def savefile(self, event):
        namafile = self.namefile.get()
        namafile += '.eps'

        '''Forbidden name and characters for a filename in windows''' 
        if namafile in ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 
                    'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM0', 
                    'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 
                    'LPT8', 'LPT9', 'LPT0']:
            messagebox.showerror("Error : Filename", 'Forbidden file name')

        for n in namafile:
            if n in ['/', '\\', '?', '%', '*', ':', '|', '\"', "\'", '<', '>', '    ', ]:
                messagebox.showerror("Error : Filename", r'Filename characters should not include \ / ? % * : | " < >')

        '''Prompt the user whether to replace the file or change the filename'''
        try:
            f = open(namafile)
            f.close()
            MsgBox = tk.messagebox.askquestion ('File Already Exist','{} already exists.\nDo you want to replace it?'.format(namafile), icon = 'warning')
            if MsgBox == 'yes':
                self.barcode.update()
                self.barcode.postscript(file=namafile, height=450, width=450, colormode="color")
        except IOError:
            self.barcode.update()
            self.barcode.postscript(file=namafile, height=450, width=450, colormode="color")

        del namafile

    
    def draw(self, event):
        self.barcode.delete('all')
        digit12 = self.angkainput.get()
        
        '''Error handling'''
        try:
            temp = int(digit12)
        except ValueError:
            messagebox.showerror("Error : Number Input", "Wrong Input.\nYou need to input 12 numbers")
            del digit12
            return None

        if len(digit12) != 12:
            messagebox.showerror("Error : Number Input", "Wrong Input.\nYou need to input 12 numbers")
            del digit12
            return None

        self.angka = self.check_digit(digit12)
        
        '''Starts Drawing'''
        #Formula for barcode
        structure = {0:'LLLLLL', 1:'LLGLGG', 2:'LLGGLG', 3:'LLGGGL', 4:'LGLLGG', 5:'LGGLLG', 
                    6:'LGGGLL', 7:'LGLGLG', 8:'LGLGGL', 9:'LGGLGL'}
        code = {0:['0001101', '0100111', '1110010'], 5:['0110001','0111001','1001110'],
                1:['0011001', '0110011', '1100110'], 6:['0101111','0000101','1010000'], 
                2:['0010011','0011011','1101100'], 7:['0111011','0010001','1000100'],
                3:['0111101','0100001','1000010'], 8:['0110111','0001001','1001000'],
                4:['0100011','0011101','1011100'], 9:['0001011','0010111','1110100']}
        
        normalizerx = int((self.width/2)-((47.5)*2.75))             #Make the barcode centered
        normalizery = int((self.width/2)-(150/2))                   #Make the barcode centered
        
        self.barcode.create_text(normalizerx+150, normalizery-50, text="EAN-13 Barcode:", font=("Helvetica", 16, "bold"))
        self.barcode.create_text(normalizerx-12, normalizery+140, text=self.angka[0], font=("Helvetica", 16, "bold"))
        self.barcode.create_text(normalizerx+150, normalizery+175, text="Check Digit: {}".format(self.angka[-1]),
                                 font=("Helvetica", 16, "bold"), fill="orange")
        #start marker
        for n in '101':
            if n == '1':
                self.barcode.create_rectangle(normalizerx, normalizery, normalizerx+2,
                                 normalizery+150, fill="black", outline='black')
            normalizerx += 3
        normalizerx += 3

        #digit 1-7
        for x in range(6):
            self.barcode.create_text(normalizerx+10, normalizery+140, 
                            text=self.angka[x+1], font=("Helvetica", 16, "bold"))
            
            rumus = structure[int(self.angka[0])][x]
            if rumus == 'L':
                for n in code[int(self.angka[x+1])][0]:
                    if n == '1':
                        self.barcode.create_rectangle(normalizerx, normalizery,
                                 normalizerx+2, normalizery+125, fill="black", outline='black')             
                    normalizerx += 3

            elif rumus == 'G':
                for n in code[int(self.angka[x+1])][1]:
                    if n == '1':
                        self.barcode.create_rectangle(normalizerx, normalizery, 
                                normalizerx+2, normalizery+125, fill="black", outline='black') 
                    normalizerx += 3
            
        
        
        #center marker
        for n in '01010':
            if n == '1':
                self.barcode.create_rectangle(normalizerx, normalizery, normalizerx+2,
                                             normalizery+150, fill="black", outline='black') 
            normalizerx += 3

        #digit 7-13
        for x in range(7,13):
            self.barcode.create_text(normalizerx+10, normalizery+140, text=self.angka[x],
                                     font=("Helvetica", 16, "bold"))
            for n in code[int(self.angka[x])][2]:
                if n == '1':
                    self.barcode.create_rectangle(normalizerx, normalizery, normalizerx+2,
                                                 normalizery+125, fill="black", outline='black')          
                normalizerx += 3

        #end marker
        for n in '101':
            if n == '1':
                self.barcode.create_rectangle(normalizerx, normalizery, normalizerx+2,
                                             normalizery+150, fill="black", outline='black')          
            normalizerx += 3

        del digit12


def main():
    root = tk.Tk()
    userinterface = BarcodeImage(root)
    root.mainloop()

if __name__=='__main__':
    main()