#!/usr/bin/env python3
#reaction_find_connections - find connections between organisms
import sys

organisms = {}
for filename in sys.argv[1:]:
    with open(filename) as current:
        organisms[filename] = {'ins': set(), 'outs': set()}
        for line in current:
            record = line.rstrip('\n').split('\t')
            organisms[filename]['ins'].update(record[1].split('+'))
            organisms[filename]['outs'].update(record[3].split('+'))
            if record[2] == "=":
                organisms[filename]['ins'].update(record[3].split('+'))
                organisms[filename]['outs'].update(record[1].split('+'))
                

for name, current in organisms.items():
    for cpd in current['outs']:
        for othername, other in organisms.items():
            #if other == current: continue
            if cpd in other['ins']:
                print("\t".join([name, cpd, othername]))
