#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
import shutil
from os import path
from  shutil import make_archive
from  zipfile import ZipFile
def main():
    # make a duplicate of an existing file
     if path.exists("textfile.txt"):
         # get the path to the file in the current directory
         src=path.realpath("textfile.txt") #dosyanin adresini variable atadi
         # let's make a backup copy by appending "bak" to the name
         dst=src+".bak" #dosya adina bak uzantisi ekleyecek
         shutil.copy(src,dst) # src variable indaki dosya adi dst ile kopyasi olusacak
         # rename the original file
         os.rename("textfile.txt", "newtext.txt") #dosyinin ismi degisecek
        # now put things into a ZIP archive
        srcq = path.realpath("textfile.txt.bak")
        if path.exists("textfile.txt.bak"):
         root_dir, tail=path.split(srcq) # dosya adresini ikiye boldu. dosya adi, dosya uzantisi
        shutil.make_archive("archive", "zip", root_dir) #dosyanin zip uzantili halini yeni adiyla olusturdu
        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
    main()
