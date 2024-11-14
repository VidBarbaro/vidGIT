import argparse
import os
import sys

from . import data

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser() # create an ArgumentParser object

    commands = parser.add_subparsers(dest='command') # add subparsers for commands
    commands.required = True # make the command argument required

    init_parser = commands.add_parser('init') # add a subparser for the 'init' command
    init_parser.set_defaults(func=init) # set the default function to call for 'init' command

    hash_object_parser = commands.add_parser('hash-object') # add a subparser for the 'hash-object' command
    hash_object_parser.set_defaults(func=hash_object) # set the default function to call for 'hash-object' command
    hash_object_parser.add_argument('file') # add a positional argument for the file to be hashed

    cat_file_parser = commands.add_parser('cat-file')  # add a subparser for the 'cat-file' command
    cat_file_parser.set_defaults(func=cat_file) # set the default function to call for 'cat_file' command
    cat_file_parser.add_argument('object') # add a positional argument for the object ID

    return parser.parse_args() # parse and return the command-line arguments

def init(args):
    data.init()

def hash_object(args):
    with open(args.file, 'rb') as f: # open the specified file in binary read mode
        print(data.hash_object(f.read()))

def cat_file(args):
    sys.stdout.flush() # flush the standard output to ensure buffer is clear
    sys.stdout.buffer.write(data.get_object(args.object)) # write the content of the object identified by args.object to the standard output in binary mode
