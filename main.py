from utility import crypto, files
import ast
import stdiomask
from pathlib import Path
import cipher_file
import click

def main():

    file = open_file()

    #Edit file content in an editor
    assert file != None
    content = click.edit(file.get_content())

    if content == None:
        print('No changes were saved \n')
    else:
        file.set_content(content)
        print('Saved \n')

    main()


def open_file():

    #Loop until user manages to open a file
    while(True):
        path = input('Open file: ')

        #If file exist open else create new
        if Path(path).is_file():
            return cipher_file.CipherFile(path)
        else:
            cmd = input('File not found. Create new? (y/n) ')
            if(cmd == 'y'):
                return cipher_file.CipherFile(path,True)
                



main()
