number = int(input("input your number : "))
basis = int(input("input ur basis : "))

numberStr = str(number)

starter = -1
final = []

for a in range(0,len(numberStr)):
    usednumber = int(numberStr[starter])
    result = (basis**a)*usednumber
    final.append(result)
    starter -= 1

b = sum(final)
print("decimal : ", b)

numberInDecimal = b

if numberInDecimal == 0:
    print("0")
    
stringhelp = ""                         #string kosong untuk membantu

while numberInDecimal >= 1:
    binary = int(numberInDecimal%2)
    numberInDecimal = numberInDecimal // 2
    if binary == 1:                     #jika sisa bagi adalah 1
        stringhelp = stringhelp + "1"   #masukkan angka 1 ke string
    elif binary == 0:                   #jika sisa bagi adalah 0
        stringhelp = stringhelp + "0"   #masukkan angka 0 ke string
    elif numberInDecimal < 1:
        break
    
print("Bilangan binernya adalah : ", stringhelp[::-1])
