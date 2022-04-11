import math

def faktorPembagian(x):
    listed, xList = [], []
    varX = 0
    for i in range(1,x+1):
        if x % i == 0 :
            listed.append(i)
            if i == int(math.sqrt(x)) :
                varX = i
    setengah = int(len(listed)/2)
    setengahFirst = listed[0:setengah] 
    setengahLast = listed[setengah::]
    setengahLast.reverse()
    for i in range(setengah):
        xList.append(str(setengahFirst[i])+" x "+str(setengahLast[i]))
    if varX > 0 :
        xList.append(str(varX)+" x "+str(varX))
    return xList

def jumlahFaktorPembagian(batas,jumlahMin):
    xList = []
    for i in range(1,batas+1):
        longI = len(faktorPembagian(i)) 
        if longI >= jumlahMin:
            xList.append(str(i)+" => "+str(longI))
    return xList

if __name__ == '__main__':
    print (faktorPembagian(100))
    print (jumlahFaktorPembagian(100,4))








