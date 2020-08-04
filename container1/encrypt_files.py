import os
from json2xml import json2xml
import json
import xml
from pathlib import Path
import pyAesCrypt
import time
import shutil

root_folder = Path.cwd() # this is the root directory
working_directory = root_folder / 'json_dir' # the the input location - here the json files will be added, converted and encrypted
os.chdir(working_directory)
destination_directory = root_folder / 'xml_dir' # the destination folder - here the files will be moved and decrypted

# the encryption function - uses pyAesCrypt library
def encrypt_file(file_to_encrypt):
    bufferSize = 64 * 1024
    password = "foopassword"
    encrypted_filename = '{}.aes'.format(file_to_encrypt)
    pyAesCrypt.encryptFile(file_to_encrypt, encrypted_filename, password, bufferSize)
    return encrypted_filename

# reads the json files 
def get_json(data):
    with open(data, 'r') as f:
        try:
            data = json.loads(f.read())
        except Exception as e:
            print(e)
            pass
    return data

# exports the converted xml to a file
def export_xml_to_file(filename, export_data):
    f = open( filename, 'w' )
    f.write(export_data)
    f.close()


def main(source_folder,destination_folder):
    for item in os.listdir(working_directory):
        variable = get_json(item)
        exported_xml_name = '{}.xml'.format(item)
        try:
            variable_xml = json2xml.Json2xml(variable, wrapper="all", pretty=True, attr_type=False).to_xml() # converts to xml from json
            export_xml_to_file(exported_xml_name, variable_xml)
            encrypted_file = encrypt_file(exported_xml_name)
            try:
                shutil.move(encrypted_file, destination_folder)
            except Exception as e:
                pass
        except Exception as e:
            print(e)

        


# created for the container to stay alive
while True:
    main(working_directory, destination_directory)
    for item in os.listdir(working_directory):
        os.remove(item)
    time.sleep(10)

