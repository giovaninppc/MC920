from arguments import *
from textManipulation import *

def main():
    print('Codificando')

    args = setupCodificationArguments()

    binaryString = TextToBinary('socorro eu to aqui', args.debug)

    


if __name__ == '__main__':
    main()
