import tkinter as tk

root = tk.Tk()

structure = {0:'LLLLLL', 1:'LLGLGG', 2:'LLGGLG', 3:'LLGGGL', 4:'LGLLGG', 5:'LGGLLG', 
            6:'LGGGLL', 7:'LGLGLG', 8:'LGLGGL', 9:'LGGLGL'}
code = {0:['0001101', '0100111', '1110010'], 5:['0110001','0111001','1001110'],
        1:['0011001', '0110011', '1100110'], 6:['0101111','0000101','1010000'], 
        2:['0010011','0011011','1101100'], 7:['0111011','0010001','1000100'],
        3:['0111101','0100001','1000010'], 8:['0110111','0001001','1001000'],
        4:['0100011','0011101','1011100'], 9:['0001011','0010111','1110100']}

width = 900
height = 900
blkwdt = 4
normalizer = int((width/2)-(47.5*blkwdt))

kanpas = tk.Canvas(root, width=width, height=height, bg='white')
kanpas.pack(padx=10, pady=10)

abc = '1234567890128'

for n in '101':
    if n == '1':
        kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+125, fill="black", outline='black')         
    normalizer += 3
normalizer += 3

for x in range(6):
    rumus = structure[int(abc[0])][x]
    if rumus == 'L':
        for n in code[int(abc[x+1])][0]:
            if n == '1':
                kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+100, fill="black", outline='black')            
            normalizer += 3

    elif rumus == 'G':
        for n in code[int(abc[x+1])][1]:
            if n == '1':
                kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+100, fill="black", outline='black')
            normalizer += 3
    
for n in '01010':
        if n == '1':
            kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+125, fill="black", outline='black')
        normalizer += 3

for x in range(7,13):
        for n in code[int(abc[x])][2]:
            if n == '1':
                kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+100, fill="black", outline='black')         
            normalizer += 3

for n in '101':
    if n == '1':
        kanpas.create_rectangle(normalizer, 30, normalizer+2, 30+125, fill="black", outline='black')         
    normalizer += 3


root.mainloop()