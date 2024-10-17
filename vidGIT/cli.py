import argparse

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser() # Create an ArgumentParser object

    commands = parser.add_subparsers(dest='command') # Add subparsers for commands
    commands.required = True # Make the command argument required

    init_parser = commands.add_parser('init') # Add a subparser for the 'init' command
    init_parser.set_defaults(func=init) # Set the default function to call for 'init' command

    return parser.parse_args() # Parse and return the command-line arguments

def init(args):
    print('Hello, World!')
