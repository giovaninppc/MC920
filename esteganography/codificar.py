from arguments import *
from textManipulation import *

def main():
    print('Codificando')

    args = setupCodificationArguments()

    binaryString = textToBinary('socorro eu to aqui', args.debug)

    string = binaryToText(binaryString, True)


if __name__ == '__main__':
    main()
