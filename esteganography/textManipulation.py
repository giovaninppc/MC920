def textToBinary(txt, debug):
    loss = '00000000'
    binaryString = ''

    if debug: print('Converting <{}> to binary'.format(txt))

    for c in txt:
        ascii = ord(c)
        binaryAscii = '{0:b}'.format(ascii)
        formattedAscii = loss[0 : (8 - len(binaryAscii))] + binaryAscii

        #DEBUG-----
        if debug: print('{} ->\t{}\t-> {}'.format(str(c), str(ascii), formattedAscii))
        #----------

        binaryString += formattedAscii

    return binaryString


def binaryToText(bin, debug):
    binaryString = str(bin)
    string = ''

    if debug: print('converting <{}> to string'.format(binaryString))

    stringSize = int(len(binaryString) / 8)
    for index in range(0, stringSize):
        characterBinaryString = binaryString[(index * 8) : ((index + 1) * 8)]
        characterNumeric = int(characterBinaryString, 2)
        character = chr(characterNumeric)

        #DEBUG-----
        if debug: print('{} ->\t{}\t-> {}'.format(characterBinaryString, str(characterNumeric), character))
        #----------

        string += character

    return string
