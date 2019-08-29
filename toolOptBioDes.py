#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Pablo Carbonell
@description: Query OptBioDes: optimal synbio design.

"""
import requests
import argparse
import csv
import os
import json

def arguments():
    parser = argparse.ArgumentParser(description='toolOptBioDes: Optimal SynBio Design. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('size', 
                        help='Library size.')
    parser.add_argument('outfile', 
                        help='Output csv design file.')
    parser.add_argument('diagfile', 
                        help='Output csv diagnostics file.')
    parser.add_argument('-infile', default=None,
                        help='Input csv file (DoE specifications sheet).')
    parser.add_argument('-partsfile', default=None,
                        help='Input csv file (Regulartory parts).')
    parser.add_argument('-genesfile', default=None,
                        help='Input csv file (Genetic parts).')
    parser.add_argument('-sbolOut', default=None,
                        help='Output design in SBOL format.')
    parser.add_argument('-server', default='http://optbiodes.synbiochem.co.uk/REST',
                        help='OptBioDes server.')
    return parser

def testApp(url):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def sheetUpload(doefile, size, outfile, diagfile, url):
    files = { 'file': open(doefile, 'rb' ) }
    values = {'size': int(size), 'format': 'csv'}
    r = requests.post( os.path.join(url, 'Query' ), files=files, data=values )
    res = json.loads( r.content.decode('utf-8') )
    M = res['data']['M']
    with open(outfile, 'w') as h:
        cw = csv.writer(h)      
        cw.writerow( res['data']['names'] )
        for row in M:
            cw.writerow( row )
    with open(diagfile, 'w') as h:
        cw = csv.writer(h)
        cw.writerow( ['Size', 'Efficiency'] )
        cw.writerow( [res['data']['libsize'], res['data']['J']] )
    print( 'Size:', res['data']['libsize'], 'Efficiency:', res['data']['J'] )

def partsUploadSbol( partsfile, genesfile, size, outfile, diagfile, sbolOut, url ):
    files = { 
        'parts': open(partsfile, 'rb' ),
        'genes': open(genesfile, 'rb')
    }
    values = {'size': size}
    r = requests.post( os.path.join(url, 'Parts' ), files=files, data=values )
    res = json.loads( r.content.decode('utf-8') )
    M = res['data']['M']
    with open(outfile, 'w') as h:
        cw = csv.writer(h)      
        cw.writerow( res['data']['names'] )
        for row in M:
            cw.writerow( row )
    with open(diagfile, 'w') as h:
        cw = csv.writer(h)
        cw.writerow( ['Size', 'Efficiency'] )
        cw.writerow( [res['data']['libsize'], res['data']['J']] )
    open(sbolOut, 'w').write(res['data']['sbol'])
    print( 'Size:', res['data']['libsize'], 'Efficiency:', res['data']['J'] )


if __name__ == "__main__":
    parser = arguments()
    arg = parser.parse_args()
    if arg.sbolOut is None:
        sheetUpload( arg.infile, arg.size, arg.outfile, arg.diagfile, arg.server )
    else:
        partsUploadSbol(  arg.partsfile, arg.genesfile, arg.size,
                          arg.outfile, arg.diagfile, arg.sbolOut, arg.server )
