import tkinter as tk
np = str(306832005500)

structure = {0:'LLLLLL', 1:'LLGLGG', 2:'LLGGLG', 3:'LLGGGL', 4:'LGLLGG', 5:'LGGLLG', 6:'LGGGLL', 7:'LGLGLG', 8:'LGLGGL', 9:'LGGLGL'}
code = {0:['0001101', '0100111', '1110010'], 1:['0011001', '0110011', '1100110'], 2:['0010011','0011011','1101100'], 3:['0111101','0100001','1000010'], 4:['0100011','0011101','1011100'], 5:['0110001','0111001','1001110'], 6:['0101111','0000101','1010000'], 7:['0111011','0010001','1000100'], 8:['0110111','0001001','1001000'], 9:['0001011','0010111''1110100']}
hasil = 0
ganjil = []
genap = []
for x in range(0, len(np), 2):
    genap.append(np[x])
for y in range (1, len(np)+1, 2):
    ganjil.append(np[y])

for n in range(6):
    hasil += int(genap[n])+(3*(int(ganjil[n])))

if hasil%10 == 0:
    angkaterakhir = 0
else:
    angkaterakhir = 10-(hasil%10)


barcodetotal = np+str(angkaterakhir)
print(barcodetotal)

barcodekode = 'a'

rumus = structure[int(barcodetotal[0])]
print(rumus)

for z in range(len(rumus)):

    if rumus[z] == "L":
        barcodekode += code[int(barcodetotal[z+1])][0]

    elif rumus[z] == "G":
        barcodekode += code[int(barcodetotal[z+1])][1]

barcodekode += 'm'

for l in range(6):
    barcodekode += code[int(barcodetotal[l+7])][2]
barcodekode += 'a'

print(barcodekode)
'''
awak = '101'
mid = '01010'

root = tk.Tk()

width = 900
height = 900
blkwdt = 4
normalizer = int((width/2)-(47.5*blkwdt))

kanpas = tk.Canvas(root, width=width, height=height, bg='white')
kanpas.pack(padx=10, pady=10)

for k in barcodekode:
    if k =='a':
        for kebelangan in awak:
            if awak =='1':
                kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="black", outline='black')
            elif awak == '0':
                kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="white", outline='white')
            normalizer += 5


    elif k=='m':
        for belang in mid:
            if mid =='1':
                kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="black", outline='black')
            elif mid =='0':
                kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="white", outline='white')
            normalizer += 5
    
    else:
        if k =='1':
            kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="black", outline='black')
        elif k =='0':
            kanpas.create_rectangle(normalizer, 10, normalizer+4, 100, fill="white", outline='white')
    normalizer += 5


root.mainloop()
'''