import random


class StringGenerator:

    def __init__(self, noAwal, xList):
        self.__noAwal = noAwal 
        self.__noAwal2 = noAwal 
        self.__xList = xList 

    def voucherAcak(self):
        abjad = list("abcdefghijklmnopqrstuvwxyz0123456789")
        string_acak = ""
        for i in range(13):
            string_acak += random.choice(abjad).upper()
        return string_acak

    def noWAacak(self):
        for i in range(8):
            self.__noAwal += str(random.randint(0,9))
        return f"{self.__noAwal[0:4]} {self.__noAwal[4:8]} {self.__noAwal[8:12]}"

    def noWAacakSpecial(self):
        under10 = []
        for i in self.__xList:
            if i < 10:
                under10.append(i)
        for i in range(8):
            if len(self.__noAwal2) == 11:
                self.__noAwal2 += str(random.choice(under10))
                break
            elif len(self.__noAwal2) == 12:
                break
            self.__noAwal2 += str(random.choice(xLIst))
        return f"{self.__noAwal2[0:4]} {self.__noAwal2[4:8]} {self.__noAwal2[8:12]}"

    def pinAcak(self):
        pin = []
        for i in range(6):
            pin.append(str(random.randint(0,9)))
        return "".join(pin)        
        

if __name__ == '__main__':
    noAwal = '0822'
    xLIst = [1,4,7,10,13,25,40,70]
    variabel = StringGenerator(noAwal, xLIst)
    print (variabel.noWAacak())
    print (variabel.noWAacakSpecial())
    print (variabel.pinAcak())
    print (variabel.voucherAcak())





    