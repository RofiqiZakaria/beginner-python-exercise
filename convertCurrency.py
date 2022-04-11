class Uang:
    
    def __init__(self,nominal, kurs) :
        self.__nominal = nominal
        self.__kurs = kurs

    def convertRupiah(self):
        nominal =  str(self.__nominal)
        nominal = nominal[::-1]
        xList = []
        if nominal.isdecimal():
            for i in range(len(nominal)):
                if i % 3 == 0:
                    xList.append(f"{nominal[i]}.")
                else:
                    xList.append(f"{nominal[i]}")
            xList[0] = xList[0][0]
            xList = xList[::-1]
            return "Rp "+"".join(xList)+",-"
        else:
            return "Inputan salah"

    def rupiahtoDollar(self):
        hasilBagi = self.__nominal // self.__kurs
        sisaBagi = self.__nominal - (self.__kurs*hasilBagi)
        persentase = float("{:.2f}".format(sisaBagi/self.__kurs))
        hasil = "$ "+str(hasilBagi+persentase)
        return hasil.replace('.',',')


if __name__ == '__main__':
    duwekku = Uang(70000,14000)
    duwekmu = Uang(35000,14000)
    print (duwekku.convertRupiah())
    print (duwekku.rupiahtoDollar())
    print (duwekmu.convertRupiah())
    print (duwekmu.rupiahtoDollar())








