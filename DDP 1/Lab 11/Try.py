import tkinter as tk

class Guwi:

    def __init__(self, master):
        self.master = master

class Bank(Guwi):
    pass

class VVibu(Bank):
    pass

class Riaju(Bank):
    pass

class Normal(Bank):
    pass

def main():
    root = tk.Tk()
    chosenfile  = open(file="data_nasabah.in", 'r')
    lines = chosenfile.readlines()
    
    dicti = {}
    for x in range(len(lines)):
        readnow = lines[x]
        if readnow[0] == "WEABOO":
            nama = readnow[1]
            money = readnow[2]
            dicti[nama]=VVibu()
        if readnow[0] == "RIAJUU":
            nama = readnow[1]
            money = readnow[2]
            dicti[nama]=Riaju()
        if readnow[0] == "RIAJUU":
            nama = readnow[1]
            money = readnow[2]
            dicti[nama]=Normal()
    userinterface  = Guwi(root)
    root.mainloop()