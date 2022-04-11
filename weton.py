import datetime as dt

class Weton:

    def __init__(self,varTgl ,varBln, varThn):
        self.__varTgl = varTgl
        self.__varBln = varBln
        self.__varThn = varThn

    def __str__(self):
        return self.informasi()

    def daftarWeton(self):
        hari = ['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
        pasaran = ['pahing','pon','wage','kliwon','legi']
        listed = []
        varHari = hari*len(pasaran)
        varPasaran = pasaran*len(hari)
        for i in range(len(hari)*len(pasaran)):
            listed.append(varHari[i].capitalize()+" "+varPasaran[i].capitalize())
        return listed

    def daftarNeptu(self):
        listed = ['sri','rejeki','gedong','loro','pati']
        return listed*7

    def neptuAngka(self, x):
        varX = 0
        if "senin" in x.lower():
            varX += 4
        elif "selasa" in x.lower():
            varX += 3
        elif "rabu" in x.lower():
            varX += 7
        elif "kamis" in x.lower():
            varX += 8
        elif "jumat" in x.lower():
            varX += 6
        elif "sabtu" in x.lower():
            varX += 9
        elif "minggu" in x.lower():
            varX += 5
        if "pahing" in x.lower():
            varX += 9
        elif "pon" in x.lower():
            varX += 7
        elif "wage" in x.lower():
            varX += 4
        elif "kliwon" in x.lower():
            varX += 8
        elif "legi" in x.lower():
            varX += 5
        return varX

    def jarakHariTemplate(self):
        hariTarget = dt.date(self.__varThn, self.__varBln, self.__varTgl)
        hariDefault = dt.date(1900, 1, 1)
        umurHari = hariTarget - hariDefault 
        return umurHari.days

    def jarakDgnHariIni(self):
        hariIni = dt.date.today()
        hariTarget = dt.date(self.__varThn, self.__varBln, self.__varTgl)
        umurHari = hariIni - hariTarget  
        return umurHari.days

    def kalkulasi(self):
        lenWeton = len(self.daftarWeton())
        tglTarget = self.jarakHariTemplate()
        wetonTarget = self.daftarWeton()[tglTarget%lenWeton]
        neptuTarget = self.daftarNeptu()[tglTarget%lenWeton].capitalize()
        neptuAngkaTarget = self.neptuAngka(wetonTarget)

    def informasi(self):
        hariTarget = dt.date(self.__varThn, self.__varBln, self.__varTgl)
        dapatkanBulan = hariTarget.strftime("%b")
        string1 = f"weton {self.__varTgl} {dapatkanBulan} {self.__varThn}: {self.hasilWeton()}"
        if self.jarakDgnHariIni() < 0:
            string2 = "maaf, inputan tanggal melebihi hari ini "
        else:
            string2 = ''
            string2 += self.usia()
        return string1 + string2

    def info(self):
        print (self.informasi())

    def hasilWeton(self):
        lenWeton = len(self.daftarWeton())
        tglTarget = self.jarakHariTemplate()
        wetonTarget = self.daftarWeton()[tglTarget%lenWeton]
        neptuTarget = self.daftarNeptu()[tglTarget%lenWeton].capitalize()
        neptuAngkaTarget = self.neptuAngka(wetonTarget)
        return f"{wetonTarget}, berneptu {neptuTarget} {neptuAngkaTarget} \n"

    def usia(self):
        rentangHari = self.jarakDgnHariIni()
        rentangTahun = rentangHari // 365
        rentangBulan = (rentangHari % 365) // 30
        return f"usia: {rentangTahun} tahun {rentangBulan} bulan / {self.jarakDgnHariIni()} hari"        


if __name__ == '__main__':
    lahirku = Weton(29,10,1995)
    lahirku.info()
    print (lahirku.usia())
    print (lahirku.hasilWeton())
    
