number = int(input("Bilangan desimal yang akan dikonversi : "))

#DesimalKeBiner

if number == 0:
    print("0")
    
stringhelp = ""                         #string kosong untuk membantu

while number >= 1:
    binary = int(number%2)
    number = number // 2
    if binary == 1:                     #jika sisa bagi adalah 1
        stringhelp = stringhelp + "1"   #masukkan angka 1 ke string
    elif binary == 0:                   #jika sisa bagi adalah 0
        stringhelp = stringhelp + "0"   #masukkan angka 0 ke string
    elif number < 1:
        break
    
print("Bilangan binernya adalah : ", stringhelp[::-1])
