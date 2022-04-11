from datetime import date
from datetime import timedelta
import datetime as dt
import calendar


class MenghitungHari:
    
    def __init__(self, jarak):
        self.__jarak = jarak

    hariDict = {'Sun': 'Minggu', 'Mon': 'Senin', 'Tue': 'Selasa',
                'Wed': 'Rabu', 'Thu': 'Kamis', 'Fri': 'Jumat', 'Sat': 'Sabtu'}

    def hitungKemaren(self):
        varX = (date.today()-timedelta(days=self.__jarak))
        hariTarget = varX.strftime("%a")
        hariItu = varX.strftime(
            f"{MenghitungHari.hariDict[hariTarget]}, %d %b %Y")
        return f"{self.__jarak} hari yg lalu bertepatan pada hari: {hariItu}"

    def hitungBesok(self):
        varX = (date.today()+timedelta(days=self.__jarak))
        hariTarget = varX.strftime("%a")
        hariItu = varX.strftime(
            f"{MenghitungHari.hariDict[hariTarget]}, %d %b %Y")
        return f"{self.__jarak} hari yg akan datang bertepatan pada hari: {hariItu}"


class MenghitungJarakHari:

    def __init__(self, tglX, blnX, thnX, tglY, blnY, thnY):
        self.__tglX = tglX
        self.__blnX = blnX
        self.__thnX = thnX
        self.__tglY = tglY
        self.__blnY = blnY
        self.__thnY = thnY

    hariDict = {'Sun': 'Minggu', 'Mon': 'Senin', 'Tue': 'Selasa',
                'Wed': 'Rabu', 'Thu': 'Kamis', 'Fri': 'Jumat', 'Sat': 'Sabtu'}

    def hitungHarikeHari(self):
        hariX = dt.date(self.__thnX, self.__blnX, self.__tglX)
        hariY = dt.date(self.__thnY, self.__blnY, self.__tglY)
        umurHari = hariY - hariX
        umurHari_ = hariX - hariY
        if hariY >= hariX:
            umurTahun = umurHari.days // 365
            umurSisaBulan = (umurHari.days % 365) // 30
            varX = str(umurHari.days) + " hari " + str(umurTahun) + \
                " tahun " + str(umurSisaBulan) + " bulan "
            return varX
        else:
            umurTahun = umurHari_.days // 365
            umurSisaBulan = (umurHari_.days % 365) // 30
            varX = str(umurHari_.days) + " hari " + str(umurTahun) + \
                " tahun " + str(umurSisaBulan) + " bulan "
            return varX

    def hitungDetail(self, tahun, bulan, tanggal):
        hariIni = dt.date.today()
        hariTarget = dt.date(tahun, bulan, tanggal)
        hariterTarget = hariTarget.strftime("%a")
        hariterterTarget = hariTarget.strftime(
            f"{MenghitungJarakHari.hariDict[hariterTarget]}, %d %b %Y")
        umurHari = hariIni - hariTarget
        listed = []
        if umurHari.days < 0:
            umurHari = umurHari.days * -1
            umurTahun = umurHari // 365
            umurSisaBulan = (umurHari % 365) // 30
            umurAll = f"{hariterterTarget}: {umurHari} hari yg akan datang, {umurTahun} tahun {umurSisaBulan} bulan"
        elif umurHari.days > 0:
            umurHari = umurHari.days
            umurTahun = umurHari // 365
            umurSisaBulan = (umurHari % 365) // 30
            umurAll = f"{hariterterTarget}: {umurHari} hari yg lalu, {umurTahun} tahun {umurSisaBulan} bulan"
        else:
            umurAll = "itu hari ini"
        return umurAll

    def hitungHaridariSekarang(self):
        xList = []
        a = self.hitungDetail(self.__thnX, self.__blnX, self.__tglX)
        b = self.hitungDetail(self.__thnY, self.__blnY, self.__tglY)
        return a+"\n"+b


if __name__ == '__main__':
    countDay = MenghitungHari(7)
    countRangeDay = MenghitungJarakHari(25, 10, 2020, 26, 10, 2020)
    print(countDay.hitungBesok())
    print(countDay.hitungKemaren())
    print(countRangeDay.hitungHaridariSekarang())
    print(countRangeDay.hitungHarikeHari())
    # print (calendar.month(2017,10))







