#!/usr/bin/env python3
import sys
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description='Lists to matrix')
parser.add_argument('files', nargs='*', default=['/dev/stdin'],
    metavar='FILE')
parser.add_argument('-r', dest='row', default=0, type=int,
    help='name column index (1-based, default=1, filename if files are given)')
parser.add_argument('-c', dest='col', default=0, type=int,
    help='value column index (1-based, defaults to column after key, or 1)')
parser.add_argument('-v', dest='val', default=0, type=int,
    help='weight column index (1-based, weight is 1 if omitted)')
args = parser.parse_args()

matrix = defaultdict(lambda: defaultdict(float))
if args.files == ['/dev/stdin']: args.row = 1
if args.col == 0: args.col = args.row + 1
for filename in args.files:
    with open(filename) as file:
        for line in file:
            record = line.rstrip('\n').split('\t')
            row = filename if args.row == 0 else record[args.row - 1]
            col = record[args.col - 1]
            val = 1 if args.val == 0 else float(record[args.val - 1])
            matrix[row][col] += val

#I made this. I have no clue how it works
params = set([param for (_, params) in matrix.items() for param in params.keys()])
print(
    "\n".join(
        [
            "\t".join(["name"] + list(params))
        ] + [
            "\t".join(
                [name] + [str(fndict[param]) for param in params]
            )
            for (name, fndict) in matrix.items()
        ]
    )
)
