from skimage.color import rgb2gray
from file_manipulation import *
from arguments import *
from imageManipulation import *

def main():
    args = setupArguments()

    img = openImage(args.imagePath)

    grayscale = convert_to_grayscale(img)
    sobelCOnverted = detectEdge(grayscale)
    saveImage('out2.png', sobelCOnverted)
    print(img)

if __name__ == '__main__':
    main()
