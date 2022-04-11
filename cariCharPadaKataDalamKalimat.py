def efisiensi(listed, filter="nonsort"):
    listedx = []
    for i in listed:
        # loweri = i.lower()
        if i not in listedx:
            listedx.append(i)
    if filter == "sort":
        listedx.sort()
    return listedx


def alpha_inKata_atKalimat(x, y):
    xKalimat = x.split(' ')
    listed = []
    for i in xKalimat:
        if y in i.lower():
            listed.append(i)
        elif y in i.upper():
            listed.append(i)
    return listed


def angka_inKata_atKalimat(x):
    xKalimat = x.split(' ')
    listed = []
    for i in xKalimat:
        for j in i:
            if j.isdecimal():
                listed.append(i)
    return efisiensi(listed)


def char_inKata_atKalimat(x):
    xKalimat = x.split(' ')
    listed = []
    for i in xKalimat:
        for j in i:
            if j.isdecimal() or j.isalnum() or j.isalpha():
                pass
            else:
                listed.append(i)
    return efisiensi(listed,)


def main():
    varX = "profit $million dari Gl00kosa mencapai 70% di tahun 2021 Q3"
    print(alpha_inKata_atKalimat(varX, "a"))
    print(angka_inKata_atKalimat(varX))
    print(char_inKata_atKalimat(varX))


if __name__ == '__main__':
    main()
