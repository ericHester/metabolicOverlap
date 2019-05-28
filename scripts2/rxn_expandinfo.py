#!/usr/bin/env python3
import sys
import os
import re

idx_id, idx_eq, idx_dir = (0, 5, 7)

def unique(sequence):
    seen = set()
    for value in sequence:
        if value in seen: continue
        seen.add(value)
        yield value

def cleanequation(raw, direction):
    def cleancompound(raw):
        if raw == " ": return ""
        return re.match('.*(cpd[0-9]+\[[^\]]*\])', raw).group(1)

    ins, outs = [
        [cleancompound(y) for y in x.split('+')]
        for x in re.split('<=>|=>|<=', raw)
    ]
    if direction == "<": #Make sure it's always input > output
        direction = ">"
        ins, outs = outs, ins
    return '\t'.join(
        ['+'.join(sorted(ins)), direction, '+'.join(sorted(outs))]
    )

reactiondb = {}
if 'ModelSEEDDatabase' in os.environ:
    filename = os.environ['ModelSEEDDatabase']
else:
    filename = os.environ['PREFIX'] + '/share/ModelSEEDDatabase'
filename += '/Biochemistry/reactions.tsv'
with open(filename) as file:
    rows = ( line.rstrip('\n').split('\t') for line in file )
    reactiondb = { row[idx_id]:row[idx_id+1:] for row in rows }

with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as file:
    reactions = (line.rstrip("\n") for line in file)
    print("\n".join(
        "\t".join([
            id, cleanequation(reactiondb[id][idx_eq], reactiondb[id][idx_dir]),
        ]) 
        for id in reactions
    ))
