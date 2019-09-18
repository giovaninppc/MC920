import numpy as np

from imageManipulation import *
from arguments import *

def main():
    args = setupArguments()
    img = openImage(args.imagePath)

    for method in args.limiarizationMethods:
        print('Applying ' + method.name)
        out = limiarizate(img, method.method)
        saveImage('out/' + args.imageName + '_' + method.name + '_.pgm', out.astype(np.uint8))
        print('\nDone')

def limiarizate(img, method):
    return method(img.astype(int))

if __name__ == '__main__':
    main()
