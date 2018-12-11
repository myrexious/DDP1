inputNum = (input("hex number : "))

dec = [10, 11, 12, 13, 14, 15]
hx = ['A', 'B', 'C', 'D', 'E', 'F']
result = []
i = -1

for a in range(0,len(inputNum)):
    chosen = inputNum[i]
    try:
        chosen1 = int(chosen)
        resA = ((16**a)*chosen1)
        result.append(resA)
    except ValueError:
        res_temp = int(dec[hx.index(chosen)])
        resB = res_temp*(16**a)
        result.append(resB)
    i -= 1

final = sum(result)
print(final)
