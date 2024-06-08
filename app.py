import argparse
import sys

parser = argparse.ArgumentParser(
    prog='WC-Tool',
    description='Word count tool using the command line interface.',
    epilog='Made in NYC with ♥.')

parser.add_argument('filename', nargs='?', default=None)

parser.add_argument('-c', '--byte', action='store_true')
parser.add_argument('-l', '--line', action='store_true')
parser.add_argument('-w', '--word', action='store_true')
parser.add_argument('-m', '--character', action='store_true')

args = parser.parse_args()

input_source = args.filename if args.filename else 'stdin'

try:
    if args.filename:
        with open(args.filename, 'rb') as file:
            read = file.read()
    else:
        read = sys.stdin.buffer.read()
    
    read_lines = read.splitlines()
    decoded = read.decode('utf-8')
except Exception as e:
    print(f"File problem: {e}")
    exit()

if not (args.byte or args.line or args.word or args.character):
    print(f"\t{len(read_lines)} {len(decoded.split())} {len(read)} {input_source}")

if args.byte:
    print(f"\t{len(read)} {input_source}")

if args.line:
    print(f"\t{len(read_lines)} {input_source}")

if args.word:
    print(f"\t{len(decoded.split())} {input_source}")

if args.character:
    print(f"\t{len(decoded)} {input_source}")


