import numpy as np

from imageManipulation import *
from arguments import *

def main():
    args = setupArguments()
    img = openImage(args.imagePath)

    for method in args.limiarizationMethods:
        out = limiarizate(img, method.method)
        saveImage('out/' + args.imageName + '_' + method.name + '_.pgm', img.astype(np.uint8))

def limiarizate(img, method):
    return method(img)

if __name__ == '__main__':
    main()
