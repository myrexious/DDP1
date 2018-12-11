def bgst(y):
    hasil = ''
    if len(y) == 1:
        if y not in "aiueo":
            hasil += x
        else:
            hasil += y
    else:
        if y[-1] not in "aiueo":
            hasil += y[-1]
        else:
            hasil += x
        bgst(y[:-1])
    print(hasil)

bgst("belajar ddp")