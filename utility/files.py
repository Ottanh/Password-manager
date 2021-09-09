
def write(text, file):

    file = open(file, 'wb')
    file.write(text)
    file.close()


def read(file):

    file = open(file, 'rb')
    content = file.read()
    file.close()

    return content


