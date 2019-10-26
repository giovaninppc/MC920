import argparse

def setupCodificationArguments():
    argParser = argparse.ArgumentParser(description = 'Arguments for the Image processing')
    argParser.add_argument('input_image_path', help = 'The path to image file to be processed')
    argParser.add_argument('input_text', help = 'The path to the text to be codificated')
    argParser.add_argument('bits', help = 'The bit plan to be used')
    argParser.add_argument('output_image_path', help = 'The path to image file to be stored')
    argParser.add_argument('-d', '--debug', help='Show debug info', action='store_true')

    args = argParser.parse_args()

    return args

def setupDecodificationArguments():
    argParser = argparse.ArgumentParser(description = 'Arguments for the Image processing')
    argParser.add_argument('input_image_path', help = 'The path to image file to be processed')
    argParser.add_argument('bits', help = 'The bit plan to be used')
    argParser.add_argument('output_text_path', help = 'The path to decripted text file to be stored')
    argParser.add_argument('-d', '--debug', help='Show debug info', action='store_true')

    args = argParser.parse_args()

    return args
