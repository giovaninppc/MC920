def TextToBinary(txt, debug):
    binaryString = ''

    if debug: print('Converting <{}> to binary'.format(txt))

    for c in txt:
        ascii = ord(c)
        binaryString += '{0:b}'.format(ascii)
        if debug: print(str(c) + '->\t' + str(ascii) + '\t-> {0:b}'.format(ascii))

    return binaryString
