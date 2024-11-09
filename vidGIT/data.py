import os

GIT_DIR = '.vidGIT'

def init():
    try:
        if not os.path.exists(GIT_DIR):
            os.makedirs(GIT_DIR)
            print(f'Directory {GIT_DIR} created')
        else:
            print(f'Directory {GIT_DIR} already exists')

    except Exception as e:
        print(f'Error: {e}')