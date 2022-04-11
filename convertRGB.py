def intoHexfromDec(n):
    # char array to store hexadecimal number
    noHexDec = ['0'] * 100
    # hexadecimal's counter number array
    i = 0
    while (n != 0):
        #  remainder is stored in a temporary variable named __temp
        _temp = 0
        # Storing remainder in _temp variable.
        _temp = n % 16
        # Check if _temp < 10
        if (_temp < 10):
            noHexDec[i] = chr(_temp + 48)
            i = i + 1
        else:
            noHexDec[i] = chr(_temp + 55)
            i = i + 1
        n = int(n / 16)
    codeHexa = ""
    if (i == 2):
        codeHexa += noHexDec[0]
        codeHexa += noHexDec[1]
    elif (i == 1):
        codeHexa = "0"
        codeHexa += noHexDec[0]
    elif (i == 0):
        codeHexa = "00"
    # Return the equivalent of hexadecimal color code
    return codeHexa

def RGBintoHex(R, G, B):
    if ((R >= 0 and R <= 255) and (G >= 0 and G <= 255) and (B >= 0 and B <= 255)):
        codeHexa = "#"
        codeHexa += intoHexfromDec(R)
        codeHexa += intoHexfromDec(G)
        codeHexa += intoHexfromDec(B)
        return codeHexa
    # If the hexadecimal color code does not exist, return -1
    else:
        return "-1"

if __name__ == '__main__':
    print(RGBintoHex(10, 0, 255))
    print(RGBintoHex(0, 40, 100))
    print(RGBintoHex(1, 4, 7))
    print(RGBintoHex(222, 255, 200))
