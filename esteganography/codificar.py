from arguments import *
from textManipulation import *
from imageManipulation import *
from fileManipulation import *

def main():
    print('Codificando')

    args = setupCodificationArguments()

    # Get input text and image
    txt = openTextFile(args.input_text)
    img = openImage(args.input_image_path)

    # Convert text to binary and add to image
    binaryString = textToBinary(txt, args.debug)
    codedImg = addTextToImage(img, int(args.bits), binaryString, args.debug)

    # Save image
    saveImage(args.output_image_path, codedImg)


if __name__ == '__main__':
    main()
