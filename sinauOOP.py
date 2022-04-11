class Device:

    penjual = 'Pak nDul'

    def __init__(self, merek, harga):
        self.brand = merek
        self.price = harga
        self.guarantee = '3 tahun'

    # jabatan outsourcing bersifat default pada parameter
    def keterangan(self, jabatan='outsourcing'):
        print(
            f"laptop dengan merek {self.brand} harganya {self.price} jt dijual oleh {self.penjual} seorang {jabatan}")


class Laptop(Device):

    def __init__(self, merek, harga):
        super().__init__(merek, harga)
        self.tahunRilis = []

    def perilisan(self, tambah):
        return self.tahunRilis.append(tambah)


class Kubus:

    def __init__(self, panjang):
        self.panjang = panjang

    def long(self):
        return self.panjang

    def area(self):
        return self.panjang**2

    def volume(self):
        return self.panjang**3


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"coor X: {self.x}, coor Y: {self.y}"

    def __call__(self):
        print("hello, ini method class called")


class Hero:

    jumlahHero = 0

    def __init__(self, name, mana, health):  # ini adalah instance variabel
        self.name = name
        self.mana = mana
        self.health = health
        Hero.jumlahHero += 1  # adalah suatu variabel yg akan menghitung jumlah inisiasi class Hero
        self.__private = "private"  # contoh variabel instance private
        self._protected = "protected"  # contoh variabel instance protected

    # ini adalah magic method
    def __repr__(self):
        # digunakan pada saat debug
        return f"ini adalah magic method _repr_ milik {self.name}"

    def __str__(self):
        # sama seperti repr, hanya saja dipakai kalau sudah jadi projectnya
        return f"ini adalah magic method _str_ milik {self.name}"

    def siapa(self):  # method tanpa return atau yg biasa kita kenal sebagai Void
        print(f"namaku adalah {self.name}")

    def healthUp(self, up):  # method dengan argumen
        print(f"darah {self.name} sebelum terHeal = {self.health}")
        self.health += up
        print(f"darah {self.name} sesudah terHeal = {self.health}")

    def getHealth(self):  # method dengan return
        return self.health

    def getMana(self):
        return self.mana

    def menyerang(self, Hero, down):
        print(self.name + ' menyerang -> ' + Hero.name)
        print(
            f"tampilkan Mana {self.name} (sebelum menyerang)  {self.getMana()}")
        self.mana -= down
        print(
            f"tampilkan Mana {self.name} (sesudah menyerang) {self.getMana()}")
        Hero.diserang(self, down)

    def diserang(self, Hero, down):
        print(self.name + ' [{< bertahan karena diserang ' + Hero.name)
        print(
            f"tampilkan HP {self.name} (sebelum diserang)  {self.getHealth()}")
        self.health -= down
        print(
            f"tampilkan HP {self.name} (sesudah diserang)  {self.getHealth()}")

    @property
    def info(self):
        return f"{self.name} Mana {self.mana} & HP {self.health}"


class StrengthHero(Hero):

    def __init__(self, name, mana, health, booster):
        super().__init__(name, int(mana*0.4*booster), int(health*0.7*booster))

    # override
    def info(self):
        return f"{self.name} Strength, Mana {self.mana} & HP {self.health}"


class AgilityHero(Hero):

    def __init__(self, name, mana, health, booster):
        super().__init__(name, mana * booster, int(health*0.5*booster))

    # override
    def info(self):
        return f"{self.name} Agility, Mana {self.mana} & HP {self.health}"


class InteligenceHero(Hero):

    def __init__(self, name, mana, health, booster):
        super().__init__(name, int(mana*0.5*booster), health * booster)

    # override
    def info(self):
        return f"{self.name} Inteligence, Mana {self.mana} & HP {self.health}"


class Warrior:  # class yg mengenkapsulasi method2 yg ada didalamnya

    __jumlahWarrior = 0

    def __init__(self, name, mana, health, aliansi):
        self.__name = name
        self.__manaBase = mana
        self.__healthBase = health
        self.__level = 1
        self.__exp = 0
        self.__mana = self.__manaBase * self.__level
        self.__healthMax = self.__healthBase * self.__level
        self.__health = self.__healthMax
        self._aliansi = aliansi
        Warrior.__jumlahWarrior += 1

    # method ini hanya berlaku untuk objek karena self harus hilang, karena self berlaku untuk objek
    def getJumlah():
        return Warrior.__jumlahWarrior

    # merubah method menjadi variabel
    @property
    def info(self):
        # return f"{self.__name} beraliansi dengan{self._aliansi} berMana {self.__mana} & berHP {self.__health}"
        return f"{self.__name} : \n\tlevel = {self.__level} \n\thealth = {self.__health}/{self.__healthMax} \n\tmana = {self.__mana} \n\tExp = {self.__exp} "

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(self.__name, 'lebelUp')
            self.__level += 1
            self.__exp -= 100
            self.__mana = int(self.__manaBase * self.__level)
            self.__healthMax = self.__healthBase * self.__level
            self.__health = self.__healthMax

    def attack(self, Warrior, down):
        self.gainExp = 60
        print(f"Mana {self.__name} (sebelum menyerang)  {self.getMana()}")
        self.__mana -= down
        print(f"Mana {self.__name} (sesudah menyerang)  {self.getMana()}")
        print(f"{self.__name} menyerang {Warrior.__name}")

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__health

    @armor.setter
    def armor(self, var):
        self.__health = var

    @armor.deleter
    def armor(self):
        self.__health = None

    # method static (decorator)
    @staticmethod
    def getJumlahStatt():
        return Warrior.__jumlahWarrior

    # class static (decorator jg)
    @classmethod
    def getJumlahClass(cls):
        return cls.__jumlahWarrior

    # method getter
    def getName(self):  # mengambil variabel nama yg telah di encapsulasi karena bersifat private
        return self.__name  # tidak bisa langsung memanggail Warrior.__name

    def getMana(self):
        return self.__mana

    def getHealth(self):
        return self.__health

    def tampil(self):
        return f"{self.__name} dari kelas warrior "


class Nation:

    def setNation(self, nation):
        self.nation = nation

    def showNation(self):
        return self.nation

    def tampil(self):
        return f"{self.nation} dari kelas nation "

    # ini adalah multiple inheritance


class KsatriaNusantara(Warrior, Nation):
    def __init__(self, name, mana, health, aliansi):
        super().__init__(name, mana, health, aliansi)
    
    def tampil(self):
        return f"{self.getName()} dari {self.nation} dari kelas KsatriaNusantara"

    
def oopHero():
    mirana = Hero('Princess of the moon', 70, 100)
    print(Hero.jumlahHero)
    jahrakal = Hero('Troll Warlord', 100, 130)
    tiny = Hero('Giant Stone', 130, 250)
    print(Hero.jumlahHero)
    rikimaru = Hero('Stealth Assassins', 250, 500)
    print(mirana.__dict__)
    print(tiny.__dict__)
    mirana.siapa()
    print("~~~~~~~~~~")
    jahrakal.healthUp(25)
    print("~~~~~~~~~~")
    mirana.menyerang(jahrakal, 13)
    print(repr(jahrakal))
    print(rikimaru)


def inheritanceHero():
    tengkorak = StrengthHero('Skeleton King', 100, 220, 4)
    zeus = AgilityHero('God of Thunder', 100, 130, 3)
    dumbledore = InteligenceHero('White Witcher', 70, 130, 3)
    print(tengkorak.info())
    print(zeus.info())
    print(dumbledore.info())
    dumbledore.menyerang(zeus, 13)
    print("<<<< multiple inheritance >>>>")
    gatotkaca = KsatriaNusantara('Awak Logam', 100, 1000, 'sentinel')
    gatotkaca.setNation('Indonesia')
    print(gatotkaca.showNation())
    print(gatotkaca.tampil())


def encapsulationWarrior():
    morphling = Warrior('Elastic Jelly', 100, 1000, 'sentinel')
    print(Warrior.getJumlah())
    print(morphling.getName())
    sven = Warrior('Rogue Knight', 100, 1300, 'sentinel')
    print(morphling.getJumlahStatt())
    axe = Warrior('Earth Breaker', 25, 1250, ' scourge')
    print(axe.getJumlahClass())
    print(Warrior.getJumlahClass())
    print(axe.info)
    axe.armor = 1300
    print(axe.armor)
    print(axe.info)
    del axe.armor
    print(axe.info)
    print("~~~~~~~~~")
    print(sven.info)
    # for i in range(10):
    #     sven.attack(axe, 10)
    #     print(sven.info)


def objectOrientedProgramming():
    barang1 = Device('Asus', 7)
    print(barang1.brand)
    print(barang1.price)
    print(barang1.guarantee)
    print(barang1.penjual)
    barang1.keterangan('sales')
    senti = Kubus(7)
    print(senti.long())
    print(senti.area())
    print(senti.volume())
    barang2 = Laptop('macBook', 13)
    barang2.perilisan(2014)
    print(barang2.tahunRilis)
    tri1 = Vector(25, 40)
    tri2 = Vector(10, 13)
    tri1and2 = tri1 + tri2
    print(f"{tri1and2.x} {tri1and2.y}")
    print(tri1and2)
    tri1and2()


if __name__ == "__main__":
    # objectOrientedProgramming()
    # oopHero()
    inheritanceHero()
    # encapsulationWarrior()
    