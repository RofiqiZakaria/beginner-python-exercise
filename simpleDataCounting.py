def cariIrisan(list1, list2):
    xlisted = []
    for i in list1:
        if i in list2:
            xlisted.append(i)
    xlisted.sort()
    return xlisted


def nonIrisan(list1, list2):
    ngiris = cariIrisan(list1, list2)
    xlisted = []
    for i in list1:
        if i not in ngiris:
            xlisted.append(i)
    for i in list2:
        if i not in ngiris:
            xlisted.append(i)
    xlisted.sort()
    return xlisted


def efisiensi(listed,filter="nonsort"):
    listedx = []
    for i in listed:
        loweri = i.lower()
        if loweri not in listedx:
            listedx.append(loweri)
    if filter == "sort":
        listedx.sort()
    return listedx


def merge(argv):
    listed = []
    for i in argv:
        for j in i:
            listed.append(j.lower())
    listed.sort()
    return listed


def multiefisiensi(argv):
    listed = []
    for i in merge(argv):
        if i not in listed:
            listed.append(i)
    listed.sort()
    return listed


def counting(argv):
    listed = []
    dict_counting = {}
    for i in multiefisiensi(argv):
        dict_counting[i] = merge(argv).count(i)
    # return dict_counting # menyortir dictionary berdasarkan key
    # return dict(sorted(dict_counting.items(),key=lambda x:x[0])) # menyortir dictionary berdasarkan keynya
    return dict(sorted(dict_counting.items(), key=lambda x: x[1])) # menyortir dictionary berdasarkan nilainya

def main():
    listed1 = ['ruby', 'javascript', 'pyTHON', 'django', 'php', 'c++', 'java', 'c++',
               'Python', 'perl', 'swift', 'tEnSoRfLoW', 'kotlin', 'python', 'flutter', 'django']
    listed2 = ['tensorflow', 'django', 'python',
               'flask', 'python', 'TeNSorFloW']
    listed3 = ['lyon', 'garuda', 'python', 'tigree', 'draco', 'turtlee']
    print("gabungan lebih dari 2 list :\n", merge([listed1, listed2, listed3]))
    print("menghapus data yg sama :\n",
          multiefisiensi([listed1, listed2, listed3]))
    print("menghitung item dlm list :\n",
          counting([listed1, listed2, listed3]))
    print("##########")
    print("pengefisienan list pertama :", efisiensi(listed1))
    print("pengefisienan list kedua :", efisiensi(listed2))
    print("irisannya adalah : ", cariIrisan(
        efisiensi(listed1), efisiensi(listed2)))
    print("non irisan adalah : ", nonIrisan(
        efisiensi(listed1), efisiensi(listed2)))


if __name__ == "__main__":
    main()
        
        
        
        
