class CheckStrongPassword:

    def __init__(self, password) :
        self.__password = password

    def __str__(self):
        return self.funcCheck()

    def info(self):
        print (self.funcCheck())

    def funcCheck(self):
        scoreDec = scoreAllow = scoreAlupp = scoreChar = scoreSpace = 0
        batas1, batas2 = 1, 2
        if len(self.__password) < 8:
            hasil = "minimal 8 character"
        else:
            for i in self.__password:
                if i.isdecimal():
                    scoreDec += 1
                elif i.isalpha():
                    if i == i.lower():
                        scoreAllow += 1
                    elif i == i.upper():
                        scoreAlupp += 1
                elif i.isspace():
                    scoreSpace += 1
                else:
                    scoreChar += 1
            if scoreDec and scoreAllow and scoreAlupp > batas2 and scoreChar and scoreSpace > batas1:
               hasil = "powerfull sangat"
            elif scoreDec and scoreAllow and scoreAlupp > batas2 and scoreChar > batas1:
                hasil = "sudah kuat"
            elif scoreDec and scoreAllow > batas1 and scoreAlupp > batas1:
                hasil = "lumayan sedang"
            else:
                hasil = "masih lemah"
        return hasil

if __name__ == '__main__':
    kodeku = CheckStrongPassword('P@55word And4 ')
    kodemu = CheckStrongPassword('P@55word aND4 ')
    kodeku.info()
    kodemu.info()
