import numpy as np
from arguments import *
from image_manipulation import *

def main():
    args = setupArguments()
    img = openImage(args.imagePath).astype(int)

    for config in args.halfTones:
        print('Processing ' + config.name)
        out = distributeError(img.copy(), config.distribution)
        saveImage('out/' + args.imageName + '_' + config.name + '.png', out.astype(np.uint8))
        print('Finished processing ' + config.name + '\n')


def distributeError(img, distribution):
    out = np.zeros(img.shape)
    for z in range(0, img.shape[2]):
        for y in range(0, img.shape[1]):
            range_x = range(0, img.shape[0])
            if y % 2 == 0:
                range_x = reversed(range_x)
            if y % 10 == 0:
                print('.', end = '', flush=True)
            for x in range_x:
                normalized = 0 if img[x][y][z] < 128 else 255
                error = img[x][y][z] - normalized
                distribution(img, error, x, y, z)
                out[x][y][z] = normalized
    return out


if __name__ == '__main__':
    main()
