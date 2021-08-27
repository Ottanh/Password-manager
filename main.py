
import crypto
import files
import ast
import stdiomask
from pathlib import Path


def main():

    file = ''
    content = {}
    secret = b''

    while(True):
        file = input('Open file: ')

        if Path(file).is_file():
            secret, content = login(content, file)
            break
        else:
            cmd = input('File not found. Create new? (y/n) ')
            if(cmd == 'y'):
                secret, content = create(file, content)
                print("File created! Type 'help' for a list of commands")
                break


    command = ''
    while(command != 'quit'):
        command = input('>>')

        if(command == 'get'):
            print_all(content)
        elif(command == 'add'):
            content = add(content)
        elif(command == 'save'):
            bcontent = str(content).encode('utf-8')
            cipher = crypto.encrypt(bcontent, secret)
            files.write(cipher, file)
        elif(command == 'remove'):
            content = remove(content)
        elif(command == 'help'):
            print('\nCommands\n\nadd     | add a key to your file\nhelp    | show a list of commands\nget     | print all the keys in your file\nsave    | save changes\nremove  | remove selected key\nquit    | close the program\n')

def print_all(content):

    for key, value in content.items():
        print(key, '->', value)


def add(content):

    key = input('')
    value = input('')
    content.update({key: value})

    return content

def remove(content):

    key = input('')
    if input("Delete selected key? (Y/N) ") == "y":
        del content[key]
    return content

def login(content, file):

    secret = stdiomask.getpass('Password: ').encode('utf-8')

    #read and decrypt
    ciphertext = files.read(file)
    byte_str = crypto.decrypt(secret, ciphertext)

    #bytes to dictionary
    dict_str = byte_str.decode('utf-8')
    content = ast.literal_eval(dict_str)

    return secret, content

def create(file, content):
    try:
        secret = stdiomask.getpass('Password: ').encode('utf-8')
        content.update({file: secret.decode('utf-8')})
        bcontent = str(content).encode('utf-8')
        cipher = crypto.encrypt(bcontent, secret)
        files.write(cipher, file)

    except ValueError:
        print("Error: File not created. Please enter a 16-digit password\n")
        main()

    return secret, content


main()
