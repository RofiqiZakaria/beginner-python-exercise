def findKatainList(List,kata):
    point = 0
    namaNama = []
    for i in range(len(List)):
        if kata in List[i]:
            point += 1
            namaNama.append(List[i])
    print (f"{point} point")
    print (namaNama)

if __name__ == '__main__':
    xListGung = ['ida ayu mayangsari','desi nur hidayah','aghnia nur amalia','shada maziyyah']
    xListWes = ['nina aini dewi','alifa nurru annafiu','lisna hilmiyati irfani','nofi nurul fadhilah','chikmah uliyyah','amanda dina','dian nur cahyani','intan maulida fitria','risna mega sari','ajeng ratna ningrum']
    findKatainList(xListWes+xListGung,'ni')
    


