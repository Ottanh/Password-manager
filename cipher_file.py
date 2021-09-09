from utility import files, crypto
import stdiomask


class CipherFile:
    
    #Constructor either creates a new file or opens an existing one
    def __init__(self, path='', new=False):

        self.path = path
        self.secret = ''
        self._content = ''

        if new:
            self.create()
        else:
            self.open_file()



    #Creates a new encryptet file
    def create(self):

        while(True):
            try:
                self.secret = stdiomask.getpass('Password: ').encode('utf-8')   #get password and encode it to bytes
                self.content = self.path + ' ' + self.secret.decode('utf-8')    #add initial content to file (cant be empty)
                bcontent = self.content.encode('utf-8')                         #encode content to bytes
                cipher = crypto.encrypt(bcontent, self.secret)                  #encrypt content
                files.write(cipher, self.path)                                  #write cipher to file
                break

            except ValueError:
                 print("Error: File not created. Please enter a 16-digit password\n")



    #Opens an existing file an decrypts it
    def open_file(self):

        while(True):
            try:
                self.secret = stdiomask.getpass('Password: ').encode('utf-8')   
                ciphertext = files.read(self.path)                              #read file 
                byte_str = crypto.decrypt(self.secret, ciphertext)              #decrypt content
                self.content = byte_str.decode('utf-8')                         #bytes to string
                break

            except ValueError:
                print("Error: Wrong password. Please try again\n")



    #Update and save content
    def set_content(self, content):
        self.content = content
        #save new content 
        bcontent = self.content.encode('utf-8')
        cipher = crypto.encrypt(bcontent, self.secret)
        files.write(cipher, self.path)
            

    def get_content(self):
        return self.content
       








