from arguments import *
from textManipulation import *
from imageManipulation import *
from fileManipulation import *


def main():
    print('Decodificando')

    args = setupDecodificationArguments()

    # Get input image
    img = openImage(args.input_image_path)
    binaryText = extractTextFromImage(img, int(args.bits), args.debug)

    decriptedString = binaryToText(binaryText, args.debug)
    writeTextFile(args.output_text_path, decriptedString)

    print('Done!')


if __name__ == '__main__':
    main()
