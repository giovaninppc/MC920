# Métodos de limiarização

### Ajuda
Execute o comando `$ python3 main.py --help`

```
usage: main.py [-h] [-g] [-b] [-n] [-c] [-avg] [-med] [-sp] input_image_path

Arguments for the Image processing

positional arguments:
  input_image_path     The path to image file to be processed

optional arguments:
  -h, --help           show this help message and exit
  -g, --global_method  Apply global limiarization
  -b, --bernsen        Apply Bernsen limiarization
  -n, --niblack        Apply Niblack limiarization
  -c, --contrast       Apply Contrast limiarization
  -avg, --media        Apply Average limiarization
  -med, --mediana      Apply Mediana limiarization
  -sp, --sauvola       Apply Sauvola-Pietaksinen limiarization
```
