import os
from json2xml import json2xml
import json
import xml
from pathlib import Path
import pyAesCrypt
import time
import shutil

root_folder = Path.cwd() # this is the root directory
print(root_folder)
working_directory = root_folder / 'xml_dir'
os.chdir(working_directory)

# the decryption function - uses pyAesCrypt library
def decrypt_file(file_to_decrypt):
    bufferSize = 64 * 1024
    password = "foopassword"
    filename = ('{}'.format(file_to_decrypt)).replace('.aes','')
    pyAesCrypt.decryptFile(file_to_decrypt, filename, password, bufferSize)
    os.remove(file_to_decrypt)
    

def main(working_directory):
    for item in os.listdir(working_directory):
        item_tipe = '{}'.format(item)
        if '.aes' in item_tipe:
            decrypt_file(item)


while True:
    main(working_directory)
    time.sleep(10)

