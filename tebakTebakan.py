import random

def tebakString():
    pilihanx = ['merah', 'putih', 'merah', 'putih', 'merah',
               'putih', 'merah', 'putih', 'merah', 'putih']
    pilihan = ['merah','putih']
    for i in range(2, -1, -1):
        tersembunyi = random.choice(pilihan)
        nginput = input("masukkan pilihan (merah/putih) :")
        if i > 0:
            if nginput == tersembunyi:
                print("selamat kamu lolos")
                break
            else:
                print("tinggal", i, "percobaan, coba lagi")
        elif i == 0:
            print("maaf, kamu gagal")
        else:
            print("tinggal", i, "percobaan, coba lagi")

def banyakList():
    xListGung = ['idaayumayangsari','desinurhidayah','aghnianuramalia','shadamaziyyah']
    xListWes = ['ninaainidewi','alifanurruannafiu','lisnahilmiyatiirfani','nofinurulfadhilah','chikmauliyyah','amandadina','diannurcahyani','intanmaulidafitria','risnamegasari','ajengratnaningrum']
    return random.choice(xListWes+xListGung)

class Hangman:
    def __init__(self, kata):
        self.__kata = kata

    def tebakHangman(self):
        xString = ''
        for i in range(len(self.__kata)):
            pilihan = [self.__kata[i],'_']
            pilihanX = random.choice(pilihan)
            xString += pilihanX
        return xString 

    def nebakHangman(self):
        xVar = self.tebakHangman()
        print (xVar)
        xVarList = list(xVar)
        hurufSalah = []
        while True:
            if '_' in xVarList:
                inputan = input("masukkan huruf yg hilang:")
                if inputan in self.__kata:
                    for i in range(len(self.__kata)):
                        if inputan == self.__kata[i]:
                            xVarList[i] = inputan
                    if len(hurufSalah) > 0 :
                        print (f"{hurufSalah}")
                    print ("".join(xVarList))
                else:
                    print ("salah, tidak ada")
                    hurufSalah.append(inputan)
                    print (f"{hurufSalah}")
                    print ("".join(xVarList))
                if len(hurufSalah) == 3:
                    print ("maaf, anda kurang beruntung, kebanyakan maksiat wkwkwk")
                    print (f"kata yg benar adalah {self.__kata}")
                    break
            else:
                print ("Yey anda berhasil horeeee")
                break

if __name__ == '__main__':
    # tebakString()
    kataku = Hangman(banyakList())
    kataku.nebakHangman()
    
    
    
    
