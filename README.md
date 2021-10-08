Google image downloader
=======================
Python script that lets you search for urls of images from google images using your tags and/or download them automatically onto you computer

Documentation
-------------

## Usage
1. Keywords in a file, such as `keywords.txt`, each line is a keyword
- `python download.py --kw_file keywords.txt --limit <num_imgs_per_keyword> --directory <save_directory>`

or

- `python download.py -f keywords.txt -l <num_imgs_per_keyword> -d <save_directory>`
2. Pass keywords directly, keywords separated by `,`

- `python download.py --keywords kw1,kw2 --limit <num_imgs_per_keyword> --directory <save_directory>`

or

- `python download.py -k kw1,kw2 -l <num_imgs_per_keyword> -d <save_directory>`
