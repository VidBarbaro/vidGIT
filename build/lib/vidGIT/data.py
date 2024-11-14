import hashlib
import os

GIT_DIR = '.vidGIT'

def init():
    try:
        if not os.path.exists(GIT_DIR):
            os.makedirs(GIT_DIR)
            os.makedirs(f'{GIT_DIR}/objects')
            print(f'Directory {GIT_DIR} created')
        else:
            print(f'Directory {GIT_DIR} already exists')

    except Exception as e:
        print(f'Error: {e}')

def hash_object(data):
    # Object ID
    oid = hashlib.sha1(data).hexdigest() # SHA-1 hashes the input data and converts the hash to a hexadecimal string
    with open(f'{GIT_DIR}/objects/{oid}', 'wb') as out: # creates a new file in the objects directory with name = OID, open the specified file in binary write mode
        out.write(data)
    return oid

def get_object(oid):
    with open(f'{GIT_DIR}/objects/{oid}', 'rb') as f: # open the file corresponding to the OID in binary read mode
        return f.read()
