import argparse

class Arguments():
    def __init__(self, imagePath: str):
        self.imagePath = imagePath
        self.imageName = imagePath.replace('.png', '').replace('/', '-')

def setupArguments() -> Arguments:
    argParser = argparse.ArgumentParser(description = 'Arguments for the Image processing')
    argParser.add_argument('input_image_path', help = 'The path to image file to be processed')

    args = argParser.parse_args()
    image_path = args.input_image_path

    return Arguments(image_path)
