# Half tone transformation

### How to use
On the root folder run:

`python3 main.py image_file_path [-<args>]`

The specified half-tone transformation will be applied to the image and saved to `/out` folder.

For example, you could use the assets on the `/images` folder

`python3 main.py images/baboon.pn -fs`

This command would apply the Floyd-Steinberg half tone method to the baboon image.

`python3 main.py images/baboon.pn -fs -sa`

For both Floyd-Steinberg and Stevenson Arce half tone methods to the baboon image.

`python3 main.py images/baboon.pn -fs -sa`

For all half-tone methods implemented.

### Help documentation
```
usage: main.py [-h] [-fs] [-sa] [-b] [-si] [-st] [-jjn] [-all]
               input_image_path

Arguments for the Image processing

positional arguments:
  input_image_path            The path to image file to be processed

optional arguments:
  -h,   --help                Show this help message and exit
  -fs,  --floyd_steinberg     Make Floyd-Steinberg transformation
  -sa,  --stevenson_arce      Make Stevenson and Arce transformation
  -b,   --burkes              Make Burkes transformation
  -si,  --sierra              Make Sierra transformation
  -st,  --stucki              Make Stucki transformation
  -jjn, --jarvas_judice_ninke Make Jarvas Judice and Ninke transformation
  -all, --all                 Make all transformations to specified image
```
