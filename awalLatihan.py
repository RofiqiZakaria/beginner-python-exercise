import datetime as dt
import re

def pungsi(param):
    paramx = 0
    for num in range(1, param):
        paramx = paramx + num
        print("no ke :", num, " = ", paramx)
    print(paramx)


def perulangan():
    avatar = ['nina', 'desi', 'maya', 'alifa', 'lisna', 'nia', 'shada']
    mod3 = []
    mod2 = []
    mod1 = []
    for i in range(1, 25):
        if (i % 3 == 0):
            mod3.append(i)
        elif (i % 2 == 0):
            mod2.append(i)
        else:
            mod1.append(i)
    print(mod1)
    print(mod2)
    print(mod3)
    index = 0
    while True:
        index += 1
        print('berhasil menjalankan while ke', index)
        if index == 10:
            break
    kata = 'python developer'
    for i in enumerate(kata):
        print("enumerasi:", i)
    for i in zip(mod3, mod2, mod1):
        print("cetak szip / gabungan: ", i)
    if 'a' in kata:  # item checking
        print("huruf 'a' ada")
    else:
        print("huruf 'a' gk ada")
    isi = [i**2 for i in range(1, 10) if i % 2 == 0]
    print("list komprehension:", isi)


def temukan_kata(kalimat):
    return 'python' in kalimat.lower()
    # py = 'python'
    # if py.capitalize() or py.upper() or py.lower() in kalimat.lower():
    # if 'python' in kalimat.lower():
    #     return True
    # else:
    #     return False


def angka():
    bil1 = 13
    bil2 = 4
    bil3 = 7.0
    bil4 = 40000000
    bil5 = 100.52343425
    x_bil4 = f"harga jutaan :  = {bil4:,}"
    x_bil5a = f"2 angka dibelakang koma :  = {bil5:.2f}"
    x_bil5b = f"5 angka dibelakang koma :  = {bil5:.5f}"
    xplus = bil1+bil2
    xminus = bil1-bil2
    xkali = bil1*bil2
    xbagi = bil1/bil2
    xpangkat = bil1**bil2
    xmodulus = bil1 % bil2
    xfloor = bil1//bil2
    print("hasil Penjumlahan dari {} + {} : ".format(bil1, bil2), xplus)
    print("hasil Pengurungan dari {} - {} : ".format(bil1, bil2), xminus)
    print("hasil Pengalian dari {} * {} : ".format(bil1, bil2), xkali)
    print("hasil Pembagian dari {} / {} : ".format(bil1, bil2), xbagi)
    print("hasil Pangkat dari {} ** {} : ".format(bil1, bil2), xpangkat)
    print("hasil Modulus dari {} % {} : ".format(bil1, bil2), xmodulus)
    print("hasil Floor dari {} // {} : ".format(bil1, bil2), xfloor)
    print("tipe data bilangan 1 : ", type(bil1))
    print("tipe data bilangan 3 : ", type(bil3))
    print(x_bil4)
    print(x_bil5a)
    print(x_bil5b)
    print(bil1, "-> binary :", bin(bil1),
          "octal :", oct(bil1), "Hexal:", hex(bil1))


def logika():
    xa = 10
    xb = 10
    print(xa is xb)
    logika_a = True
    logika_b = False
    x_logika1 = logika_a and logika_a
    x_logika2 = logika_a and logika_b
    x_logika3 = logika_b and logika_a
    x_logika4 = logika_b and logika_b
    y_logika1 = logika_a or logika_a
    y_logika2 = logika_a or logika_b
    y_logika3 = logika_b or logika_a
    y_logika4 = logika_b or logika_b
    z_logika1 = logika_a ^ logika_a
    z_logika2 = logika_a ^ logika_b
    z_logika3 = logika_b ^ logika_a
    z_logika4 = logika_b ^ logika_b
    xkeramat = 11
    nokeramat = (xkeramat >= 4 and xkeramat <= 10)
    print("True dan True :", x_logika1)
    print("True dan False :", x_logika2)
    print("False dan True :", x_logika3)
    print("False dan False :", x_logika4)
    print("True atau True :", y_logika1)
    print("True atau False :", y_logika2)
    print("False atau True :", y_logika3)
    print("False atau False :", y_logika4)
    print("True Xluxive Or True :", z_logika1)
    print("True Xluxive Or False :", z_logika2)
    print("False Xluxive Or True :", z_logika3)
    print("False Xluxive Or False :", z_logika4)
    print("hasil dari nomor keramat :", nokeramat)


def waktu():
    hari_ini = dt.date.today()
    bornday = dt.date(1995, 10, 29)
    umur_hari = hari_ini - bornday
    umur_tahun = umur_hari.days // 365
    umur_bulan_sisa = (umur_hari.days % 365) // 30
    print(f"hari ini : {hari_ini:%A}")
    print(f"hari 29 okt : {bornday:%A}")
    print(f"umur hari :{umur_hari}")
    print(f"umurnya :{umur_tahun} tahun, {umur_bulan_sisa} bulan")


def first_basic():
    print('sholat jum\'at')
    print('driev C:\\asoy\geboy')
    print("penggunaan \ttombol tab")
    print("penggunaan \ntombol enter")
    print("penggunaan \btombol backspace")
    print(r"penggunaan \b\n\traw string 'yg semuanya dianggap string'")
    triplet = f"""
    first  = {"ini baris pertama":>25}
    second = {"ini baris kedua":>25}
    third  = {"ini baris ketiga":>25}
    """
    print(triplet)
    ciwiciwi = ['maya', 'desi']
    item_pisces = ['patin', 'gurame', 'lele', 'nila',
                   'bandeng', 'mujair', 'tombro', 'bawal']
    kata = "achMaD roFiQi ZaKaRia"
    xxkata = "bilangan13"
    start = 2
    end = 16
    jrk = 2
    print("\n################\n")
    print("list terselect : ", item_pisces[3], item_pisces[1],  item_pisces[5])
    print("tampil huruf ke", start, "dari kata '", kata, "' : ",
          kata[start-1])  # karena list (array) diawali dengan 0
    print("tampil huruf ke 2 sampai", end, "dari kata '", kata,
          "' : ", kata[0:end])  # tanda : merupakan slicing dari & ke
    print("tampil huruf ke 1 sampai", end, " berjarak", jrk, "dari kata '",
          kata, "' : ", kata[0:end:jrk])
    print("tampil huruf ke 1 sampai habis berjarak", jrk, "dari kata '",
          kata, "' : ", kata[::jrk])  # aslinya kata[0:0:jrk] tp disingkat jadi kata[::jrk] karena 0 gk dianggap
    print("menampilkan secara reverse :", kata[::-1])
    print("membagi kalimat per kata : ", kata.split())
    print("membagi kalimat per huruf 'a' : ", kata.split('a'))
    print("gabungan list para selir :", ' '.join(ciwiciwi))
    print("\n################\n")
    print("uppercase : ", kata.upper())
    print("lowercase : ", kata.lower())
    print("capitalis : ", kata.capitalize())
    print("apakah lower :", kata.islower(),
          " & apakah upper :", kata.isupper())
    print("apakah huruf semua ??? : ", xxkata.isalpha())
    print("apakah huruf atau angka ??? : ", xxkata.isalnum())
    print("apakah angka semua ??? : ", xxkata.isdecimal())
    print("apakah ada spasinya ??? : ", kata.isspace())
    print("apakah depan nama sesuai :", kata.lower().startswith("achmad"))
    print("apakah belakang nama sesuai :", kata.lower().endswith("zakaria"))
    print("ini ada beberapa {} latihan".format('modul'))
    print("ini ada {} {} {} ditaman".format('ani', 'bella', 'cindy'))
    print("ini ada {2} {0} {1} ditaman".format('ani', 'bella', 'cindy'))
    print("ini ada {b} {c} {a} ditaman".format(a='ani', b='bella', c='cindy'))
    print("komandan panglima perang -> {}".format(kata))
    print("\n################\n")
    item_pisces.append('Garam')
    item_seafood = ['udang', 'lobster', 'tuna', 'salmon', 'kepiting', 'kerang']
    item_piscesx = item_pisces + item_seafood
    item_pisces.append(item_seafood)
    for i in range(len(item_pisces)):
        print(item_pisces[i])
    print("=========")
    for i in range(len(item_piscesx)):
        print(item_piscesx[i])
    print("\n################\n")
    print("nested list item piscces : ", item_pisces[len(item_pisces)-1][1])
    varx = [1, 4, 7, 13, 10, 7, 4, 1, 4, 1, 1, 10]
    varx.sort()
    print("mengurutkan dari nilai terkecil sebuah list bilangan :", varx)
    varx.reverse()
    print("membalikkan urutan sebuah list bilangan :", varx)
    nama = list(kata)
    print("sebuah string diubah kedalam list: ", nama)
    dict_mamalia = {'key1': 'sapi', 'key2': 'unta',
                    'key3': 'kambing', 'key4': 'domba', 'key5': 'biribiri'}
    print("nama nama dictionary mamalia :", dict_mamalia)
    print("unique dari dictionary mamalia :", dict_mamalia.keys())
    print("nilai nilai dari dictionary mamalia :", dict_mamalia.values())
    print("salah satu nama dictionary mamalia :", dict_mamalia['key3'])
    tuple_reptil = ('buaya', 'bunglon', 'ular', 'kadal',
                    'gecko', 'iguana', 'komodo')
    print("isi dari tuple reptil : ", tuple_reptil)
    print("isi dari tuple reptil ke 3 :", tuple_reptil[2])
    set_nama = set(kata)
    print("sets dari nama : ", set_nama)
    print("\n################\n")


def penjumlahan(*args):
    return sum((args))


kalimat1 = 'ini merupakan kalimat global'


def cetak():
    kalimat2 = 'ini merupakan kalimat local'

    def eksekusi():
        kalimat3 = 'ini merupakan kalimat sub-local'
        print("one :", kalimat1)
        print("two :", kalimat2)
        print("three :", kalimat3)

    eksekusi()


def fungsi_map():
    def kali10(x):
        return x*10

    def panjangkata(kata):
        if len(kata) % 2 == 0:
            return 'genap'
        else:
            return 'ganjil'

    angkax = [1, 4, 7, 10]
    hasil_angka = list(map(kali10, angkax))
    print("fungsi map pada int :", hasil_angka)
    katax = ['wkwkwk', 'hahahahaa', 'awokawokawok', 'hihihihii']
    hasil_kata = list(map(panjangkata, katax))
    print("fungsi map pada string:", hasil_kata)


def fungsi_filter():
    def cekgenap(x):
        return x % 2 == 0

    angka = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    hasil_filter_int = list(filter(cekgenap, angka))
    print("fungsi filter pada list :", hasil_filter_int)



if __name__ == '__main__':
    # nginput = int(input("masukkan banyaknya angka :"))
    # ax = total(nginput)
    # print (ax)
    # metotmetot()
    # fizzBuzz(15)
    # nginput = input("masukan data :")
    # print (nginput)
    # angka()
    waktu()
    # perulangan()
    # fungsi_map()
    # first_basic()
    # fungsi_filter()
    # cetak()
    # logika()
    # print(penjumlahan(2, 4, 3, 12, 53))
    # print(temukan_kata('belajar PYtHon itu mudah'))
    # first_basic()
