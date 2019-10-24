def addTextToImage(img, bits, txt, debug):

    replaceIndex = 7 - bits
    counter = 0

    if debug:
        print('----------------')
        print('Applying changes on {} bit'.format(replaceIndex))

    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):
            for z in range(0, img.shape[2]):

                if counter >= len(txt): return img

                pixel = img[x][y][z]

                binary = '{0:08b}'.format(pixel)
                replacedBinary = binary[:replaceIndex] + txt[counter] + binary[replaceIndex + 1:]

                newPixel = int(replacedBinary, 2)
                img[x][y][z] = newPixel

                if debug: print('{} + {} ->\t{} -> {}'.format(pixel, txt[counter], binary, replacedBinary))

                counter += 1
