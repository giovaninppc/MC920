def addTextToImage(img, bits, txt, debug):

    # 0 -> R
    # 1 -> G
    # 2 -> B
    channel = bits % 3
    counter = 0

    for x in range(0, img.shape[0]):
        for y in range(0, img.shape[1]):

            if counter >= len(txt): return img

            pixel = img[x][y][channel]

            binary = bin(pixel)[2:]
            binary = binary[:-1] + txt[counter]

            newPixel = int(binary, 2)
            img[x][y][channel] = newPixel

            counter += 1
