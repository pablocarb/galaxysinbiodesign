#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Pablo Carbonell
@description: Query Selenzme: Enzyme sequence selection.

"""
import requests
import argparse
import csv
import os
import json

def arguments():
    parser = argparse.ArgumentParser(description='toolSelenzyme: Enzyme sequence selection. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Input csv file.')
    parser.add_argument('outfile', 
                        help='Input csv file.')
    parser.add_argument('-server', default='http://selenzyme.synbiochem.co.uk/REST',
                        help='Selenzyme server.')
    return parser

# Output columns, to be improved
columns = ['smarts', 'Seq. ID', 'Score', 'Organism Source', 'Description']

if __name__ == "__main__":
    parser = arguments()
    arg = parser.parse_args()
    assert os.path.exists(arg.infile)
    header = True
    with open(arg.infile) as handler, open(arg.outfile, 'w' ) as writer:
        cw = csv.writer( writer )
        cv = csv.DictReader(handler)
        for row in cv:
            url = arg.server
            assert 'smarts' in row
            smarts = row['smarts']
            r = requests.post( os.path.join(url, 'Query') , json={'smarts': smarts} )
            res = json.loads( r.content.decode('utf-8') )
            try:
                assert res['data'] is not None
                val = json.loads( res['data'] )
                assert 'Seq. ID' in val and len(val['Seq. ID'])>0
                if header:
                    cw.writerow( columns )
                    header = False
                for ix in sorted(val['Seq. ID'], key=lambda z: int(z)):
                    cw.writerow( [smarts]+[val[j][ix] for j in columns[1:]] )
            except:
                continue

