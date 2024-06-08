import argparse

parser = argparse.ArgumentParser(
    prog='WC-Tool',
    description='Word count tool using the command line interface.',
    epilog='Made in NYC with ♥.')

parser.add_argument('filename')

parser.add_argument('-c', '--byte', action='store_true')
parser.add_argument('-l', '--line', action='store_true')
parser.add_argument('-w', '--word', action='store_true')
parser.add_argument('-m', '--character', action='store_true')

args = parser.parse_args()

try:
    with open(args.filename, 'rb') as file:
        read = file.read()
        read_lines = read.splitlines()
        decoded = read.decode('utf-8')
except Exception as e:
    print(f"File problem: {e}")
    exit()

if not (args.byte or args.line or args.word or args.character):
    print(f"\t{len(read)} {len(read)} {len(decoded.split())} {args.filename}")

if args.byte:
    print(f"\t{len(read)} {args.filename}")

if args.line:
    print(f"\t{len(read_lines)} {args.filename}")

if args.word:
    
    print(f"\t{len(decoded.split())} {args.filename}")

if args.character:
    decoded = read.decode('utf-8')
    print(f"\t{len(decoded)} {args.filename}")


