import argparse

def setupArguments():
    argParser = argparse.ArgumentParser(description='Arguments for the Image processing')
    argParser.add_argument('input_image_path', help='The path to image file to be processed')
    argParser.add_argument('-k', '--component_number', help='Number of components for SDV compression')
    argParser.add_argument('-o', '--output_path', help='Custom output compressed image path (default: compressed.png)')

    return argParser.parse_args()
