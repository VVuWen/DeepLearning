n = 0
w = open('result1.txt','w')
with open('C:\\Users\\Wuwen\\Desktop\\tabuflowerResultPro.txt','r') as f:
    while True:
        line = f.readline()
        n += 1
        print(n)
        if line[0] == '0':
            w.write(line)

            if line == None:
                break
    f.close()
    w.close()