import random
import string
import time
import math
import re
import copy
from datetime import datetime as dt
import datetime as tanggalwaktu
from datetime import date as tanggal
from datetime import timedelta as waktudelta
from typing_extensions import _AnnotatedAlias
import simpleDataCounting as sdc
# from collections import Counter
import numpy as np
import socket
import sinauOOP as sop

# yg sudah dipelajari dalam Regular Expession yaitu : alternation|, group(), backslash\
# yg belum dipelajari dalam Regular Expession yaitu : period., caret^, dollar$, star*, plus+, question?, braces{},
# yg belum dipelajari Serialization

# <<<<<<< yg belum dipelajari => decorator, generator, logging, threading multithreading & processing multiprocessing, exception, context manager >>>>>>>

def jarak_hari_mundur(thn, bln, tgl):
    hari_mundur = tanggalwaktu.date(thn, bln, tgl)
    hari_lahir = tanggalwaktu.date(1995, 10, 29)
    umur_hari = hari_lahir - hari_mundur
    # return umur_hari
    xi = ""
    for i in str(umur_hari):
        xi += i
        if i == " ":
            break
    return xi


def jarak_hari():
    hari_ini = tanggalwaktu.date.today()
    hari_lahir = tanggalwaktu.date(1995, 10, 29)
    umur_hari = hari_ini - hari_lahir
    xi = ""
    for i in str(umur_hari):
        xi += i
        if i == " ":
            break
    return xi


def waktunow():
    waktu_time = dt.time(dt.now())
    waktu_date = dt.date(dt.now())
    detailtoday = dt.now()
    # xsekarang = str(waktu_date)[8:10]+"-"+str(waktu_date)[5:7]+"-"+str(waktu_date)[0:4]
    # sekarang = xsekarang+"_"+str(waktu_time)[0:8].replace(":",".")+"WIB"
    hari_dict = {'Sun': 'Minggu', 'Mon': 'Senin', 'Tue': 'Selasa',
                 'Wed': 'Rabu', 'Thu': 'Kamis', 'Fri': 'Jumat', 'Sat': 'Sabtu'}
    hari_itu = detailtoday.strftime("%a")
    sekarang = detailtoday.strftime(
        f"{hari_dict[hari_itu]},%d%b%Y_%H.%M.%S%p")
    return sekarang


def waktu_list():
    catatan_waktu = dt.now()
    hari_dict = {'Sun': 'Minggu', 'Mon': 'Senin', 'Tue': 'Selasa',
                 'Wed': 'Rabu', 'Thu': 'Kamis', 'Fri': 'Jumat', 'Sat': 'Sabtu'}
    hari_itu = catatan_waktu.strftime("%a")
    print (catatan_waktu)
    print(hari_dict[hari_itu])
    print(catatan_waktu.strftime("%m,%d,%y %H:%M:%S %p"))
    print(catatan_waktu.strftime("%D %H:%M:%S"))
    print(catatan_waktu.strftime("%A, %d %B %Y %H:%M:%S"))
    print(catatan_waktu.strftime("%a, %d %b %Y %H:%M:%S %p"))
    print(catatan_waktu.strftime(
        f"{hari_dict[hari_itu]}, %d %b %Y %H:%M:%S %p"))


def checkIP():
    hostname = socket.gethostname()
    IPaddr = socket.gethostbyname(hostname)
    print(IPaddr)
    subnetMaskA = IPaddr[0:3]
    subnetMaskB = IPaddr[4:7]
    subnetMaskC = IPaddr[8:11]
    subnetMaskD = IPaddr[12:14]
    subnetMaskAll = IPaddr.split('.')
    xSubnetMask = IPaddr.replace('.', ' ')
    print(subnetMaskAll)
    print(xSubnetMask)



def matchingB(a, b):
    listed = []
    var_a = a*len(b)
    var_b = b*len(a)
    for i in range(len(a)*len(b)):
        listed.append(var_a[i].capitalize()+" "+var_b[i].capitalize())
    return listed


def matchingA(a, b):
    listed = []
    for i in a:
        for j in b:
            listed.append(i+" "+j)
    return listed


def matchCounting(x, y):
    if len(x) % 2 == 0:
        if len(y) % 2 == 0:        # jika genap semua
            return matchingA(x, y)
        else:                      # jika ada salah satu ganjil
            return matchingB(x, y)
    else:
        if len(y) % 2 == 0:        # jika ada salah satu ganjil
            return matchingB(x, y)
        else:                      # jika ganjil semua
            if len(x) == len(y):   # tp jika bilangannya sama
                return matchingA(x, y)
            else:                  # bilangannya berbeda
                return matchingB(x, y)


def googleGloo(x):
    if len(x) % 2 == 0:
        setengahLen = int(len(x)/2)
        x1 = x[1:setengahLen]
        x2 = x[setengahLen:-1]
        return x2+x1
    else:
        return "pangjangnya ganjil, jadi tidak bisa "


def eksepsion():
    try:
        a = 10 / 0
        # b = a + 'x'
        c = a + 1
    except ZeroDivisionError as e:
        print("tidak bisa dibagi dengan 0")
    except TypeError as e:
        print(f'ada salah pengetikan {e}')
    else:
        print('semuanya aman')
    finally:
        print("beres bossque")




def argumenKeywordArgumen1(a,b,c,*args,**kwargs):
    print (f"{a} - {b} - {c}")
    print ("~~~~~~~~~~")
    for i in args:
        print (i)
    print ("~~~~~~~~~~")
    for i in kwargs:
        print (f"{i} - {kwargs[i]}")

def argumenKeywordArgumen2(a,*args,b):
    print (f"{a}")
    print ("~~~~~~~~~~")
    for i in args:
        print (i)
    print ("~~~~~~~~~~")
    print (f"{b}")

def argumenKeywordArgumen3(*args,a,b):
    print (f"{a}")
    print ("~~~~~~~~~~")
    for i in args:
        print (i)
    print ("~~~~~~~~~~")
    print (f"{b}")

def ateriskOperator():
    dictA = {'a':13,'b':25}
    dictB = {'c':10,'d':40}
    gabunganDict ={**dictA, **dictB}
    print (gabunganDict)
    setX = {1,4,7}
    tuppleX = (10,40,70)
    xList = [*setX, *tuppleX]
    print (xList)
    print ("~~~~~~~~~~")
    ngopy = [4,7,10,13,25,40,70]
    ngopx = ngopy
    ngopx[2]=1000
    print (f"{ngopx} & {ngopy}")
    ngopz = copy.deepcopy(ngopy)
    # ngopz = ngopy.copy()
    # ngopz = ngopy[:]
    ngopz[2]=999
    print (f"{ngopz} & {ngopy}")


def regex():
    pola = '^u....a$'
    print(pola[1:len(pola)-1])
    contoh = ['uchiha', 'uChihA', 'uchihha']
    for i in contoh:
        hasil = re.match(pola, i)
        if hasil:
            print(i, " : match RegEx success")
        else:
            print(i, " : match RegEx failed")
    nginput = "I'm from clan Uchiha "
    hasil2 = re.findall(r"[chia]", nginput)
    print("ini findall RegEx :", hasil2)
    for i in contoh:
        print(re.search(r'^uc', i))  # menccari huruf 'ha'
    print("########")
    doi1 = 'ida ayu mayangsari'
    print(re.findall(r'm|a|i', doi1))  # mencari huruf a,i,m dalam variabel doi
    # mencari huruf ya,da,ma dalam variabel doi
    print(re.findall(r'(y|d|m)a', doi1))
    print("########")
    contoh2 = ['the sun', 'at the night', 'The light']
    for i in contoh2:
        print(re.findall(r'\Athe', i))  # mencari kata 'the' diawal kalimat
    print("########")
    contoh3 = ['football', 'a football', 'afootball', 'is a football']
    for i in contoh3:
        # mencari kata 'foot' diawal sebuah kata
        print(re.findall(r'\bfoot', i))
    print("~~~~")
    contoh4 = ['ballon', 'ball on dior', 'ballballan']
    for i in contoh4:
        # mencari kata 'ball' diakhir sebuah kata
        print(re.findall(r'ball\b', i))
    print("########")
    for i in contoh3:
        # mencari kata 'foot' bukan diawal sebuah kata
        print(re.findall(r'\Bfoot', i))
    print("~~~~")
    contoh4 = ['ballon', 'ball on dior', 'ballballan']
    for i in contoh4:
        # mencari kata 'ball' bukan diakhir sebuah kata
        print(re.findall(r'ball\B', i))
    print("########")
    contoh5 = ['roz@ck', '147', 'nopunggung13',
               'bangsal13', '7langit', '7bidadari']
    for i in contoh5:
        print(re.findall(r'\d', i))  # mencari apakah terdapat angka
    print("~~~~")
    for i in contoh5:
        print(re.findall(r'\D', i))  # mencari apakah terdapat yg bukan angka
    print("########")
    contoh6 = ['desi nur hidayah', 'aghnia amalia', 'maziyyah', 'maya']
    for i in contoh6:
        print(re.findall(r'\s', i))  # mencari apakah ada spasi
    print("########")
    contoh7 = ['123&%wkwk#*', '70%bossque[/]']
    for i in contoh7:
        print(re.findall(r'\w', i))  # mencari digit dan alphabet
    print("~~~~")
    for i in contoh7:
        print(re.findall(r'\W', i))  # mencari yg bukan digit dan alphabet

if __name__ == '__main__':

    waktu_list()
    # tebak_hangman()
    hari = ['minggu', 'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']
    pasaran = ['legi', 'pahing', 'pon', 'wage', 'kliwon']
    x1 = ['maya', 'desi', 'nia']
    x2 = ['merah', 'biru', 'hijau']
    len_weton = len(matchCounting(hari, pasaran))
    # print (jarak_hari())
    # print (jarak_hari_mundur(1995, 10, 29))
    count_weton = matchCounting(hari, pasaran)
    count_weton_mundur = matchCounting(hari, pasaran)
    count_weton_mundur.reverse()
    count_wetonx = int(jarak_hari())
    count_weton_mundurx = int(jarak_hari_mundur(1900, 1, 1))
    # print ("weton hari ini :",count_weton[(count_wetonx%len_weton)])
    # print ("weton hari itu :",count_weton_mundur[(count_weton_mundurx%len_weton)-1])
    # print (dapat_dibagi_berapa(12))
    # print (dapat_dibagi_berapa_aja(9600))
    varX = "once upon a time in the morning with my SexPartner have a nice time"
    varY = "once upon a longtime in the evening with my LovePartner have a nice Time"
    # varX = varX.split(" ")
    # varY = varY.split(" ")
    # print (sdc.counting([varX,varY]))
    # eksepsion()
    checkIP()
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # regex()
    # argumenKeywordArgumen1(4,7,10,100,130,250,varX=13, varY=25, varZ=40)
    # print ("\n##########\n")
    # argumenKeywordArgumen2(10,13,25,40,b=1)
    # print ("\n##########\n")
    # argumenKeywordArgumen3(10,13,25,a=40,b=1)
    # ateriskOperator()
   