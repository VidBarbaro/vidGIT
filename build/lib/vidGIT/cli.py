import argparse
import os

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

    return parser.parse_args() # parse and return the command-line arguments

def init(args):
    data.init()
