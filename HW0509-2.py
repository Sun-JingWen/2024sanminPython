
#九九乘法顛倒
for a in range(1,10):
    for b in range(9,1,-1):
        print(b,'*',a,'=', a*b, sep="", end = "\t")