
import crypto
import files
import ast
from pathlib import Path

def main():

    file = ''
    content = {}
    secret = b''
   
    while(True):
        file = input('File: ')

        if Path(file).is_file():
            secret, content = login(content, file)
            break
        else:
            cmd = input('File not found. Create new? (y/n) ')
            if(cmd == 'y'):
                secret, content = create(file, content)
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



def print_all(content):

    for key, value in content.items():
        print(key, '->', value)


def add(content):

    key = input('')
    value = input('')
    content.update({key: value})

    return content


def login(content, file):

    secret = input('password: ').encode('utf-8')

    #read and decrypt
    ciphertext = files.read(file)
    byte_str = crypto.decrypt(secret, ciphertext)

    #bytes to dictionary
    dict_str = byte_str.decode('utf-8')
    content = ast.literal_eval(dict_str)

    return secret, content

def create(file, content):

    secret = input('Password: ').encode('utf-8')
    content.update({file: secret.decode('utf-8')})

    bcontent = str(content).encode('utf-8')
    cipher = crypto.encrypt(bcontent, secret)
    files.write(cipher, file)

    return secret, content


main()
