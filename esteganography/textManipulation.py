stopCharacter = '00000000'

def textToBinary(txt, debug):
    binaryString = ''

    if debug: print('Converting <{}> to binary'.format(txt))

    for c in txt:
        ascii = ord(c)
        binaryAscii = '{0:08b}'.format(ascii)

        #DEBUG-----
        if debug: print('{} ->\t{}\t-> {}'.format(str(c), str(ascii), binaryAscii))
        #----------

        binaryString += binaryAscii

    return binaryString + stopCharacter


def binaryToText(bin, debug):
    binaryString = str(bin)
    string = ''

    if debug: print('converting <{}> to string'.format(binaryString))

    stringSize = int(len(binaryString) / 8)
    for index in range(0, stringSize):
        characterBinaryString = binaryString[(index * 8) : ((index + 1) * 8)]

        if characterBinaryString == stopCharacter: return string

        characterNumeric = int(characterBinaryString, 2)
        character = chr(characterNumeric)

        #DEBUG-----
        if debug: print('{} ->\t{}\t-> {}'.format(characterBinaryString, str(characterNumeric), character))
        #----------

        string += character

    return string
