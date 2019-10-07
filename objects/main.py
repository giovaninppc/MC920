from file_manipulation import *
from arguments import *

def main():
    args = setupArguments()

    img = openImage(args.imagePath)
    print(img)

if __name__ == '__main__':
    main()


def convert_to_grayscale(img):
    return rgb2gray(original)
