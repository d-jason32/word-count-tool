import argparse

parser = argparse.ArgumentParser(
    prog='WC-Tool',
    description='Word count tool using the command line interface.',
    epilog='Made in NYC with ♥.')

parser.add_argument('filename')

parser.add_argument('-c',
                    '--byte',
                    action='store_true')

parser.add_argument('-l',
                    '--line',
                    action='store_true')
                    
args = parser.parse_args()

if args.byte:
    with open(args.filename, 'rb') as file:
        content = file.read()
        print(f"{len(content)} {args.filename}")

if args.line:
    with open(args.filename, 'rb') as file:
        content = file.readlines()
        print(f"{len(content)} {args.filename}")
