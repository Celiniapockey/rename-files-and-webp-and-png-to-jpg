# rename-files-and-webp-and-png-to-jpg
rename files and change pictures from webp and png to jpg

## Introduce
The 2 code can change the file name into the foldername(the file in)+(count) and change the pictrue format from webp and png to jpg. If you have many files into different folders, it also can work even you put the code files into the grandfather folder.

But there are 2 point you need to be careful: 

First, the `rename.py` will rename all files except `.py`, you should make sure that there are no other files you don't want to rename.

Second, the `rename.py` will delete the `SPACE` in the name,be sure that you don't want `SPACE` in the name.

## How to run
Running them in terminal:

1.Install the Pillow of python:

`pip install Pillow`

2.Open the folder of the 2 python files

`cd THE-PATH-TO-YOUR-FILES`

3.Running the 2 files

`python rename.py`

`python webppng2jpg.py`
