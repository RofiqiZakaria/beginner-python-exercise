import random


def play():
    user = input("Gunting Batu Kertas ???\n")
    computer = random.choice(['gunting', 'batu', 'kertas'])
    if user == computer:
        return f'imbang sama, komputer : {computer}'

    if isWin(user, computer):
        return f'kamu menang, komputer : {computer}'

    return f'kamu kalah, komputer : {computer}'


def isWin(player, opponent):
    if (player == 'batu' and opponent == 'gunting') or (player == 'gunting' and opponent == 'kertas') or (player == 'kertas' and opponent == 'batu'):
        return True


if __name__ == '__main__':
    print (play())



    