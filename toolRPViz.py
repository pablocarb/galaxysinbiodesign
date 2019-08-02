#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Pablo Carbonell
@description: Query RPViz: pathway visualizer.

"""
import requests
import argparse
import csv
import os
import json
import tarfile

def arguments():
    parser = argparse.ArgumentParser(description='toolRPViz: Pathway visualizer. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Pathways in SBML format.')
    parser.add_argument('outfile', 
                        help='HTML visualizer file.')
    parser.add_argument('--input_format', default='sbml',
                        help='Input format: sbml|json')
    parser.add_argument('--choice', default="5",
                        help='What kind of output do you want ? \n 1/Single HTML file \n 2/Separated HTML files \n 3/View directly in Cytoscape \n 4/Generate a file readable in Cytoscape \n 5/Tar file')
    parser.add_argument('--selenzyme_table',
                        default="N",
                        help='Do you want to display the selenzyme information ? Y/N')
    parser.add_argument('--outfolder', 
                        help='Location of additional files')
    parser.add_argument('-server', default='http://rpviz.synbiochem.co.uk/REST',
                        help='RPViz server.')
    return parser

def testApp(url):
    r = requests.get( url )
    res = json.loads( r.content.decode('utf-8') )
    print( res )
    
def pathwayUpload( arg ):
    files = { 'file': open(arg.infile, 'rb' ) }
    data = {'selenzyme_table': arg.selenzyme_table, 'input_format': arg.input_format}
    print('Sending query to '+arg.server)
    r=requests.post( arg.server+'/Query',files=files,data=data )
    if arg.outfolder is None:
        arg.outfolder = os.path.dirname( arg.outfile )
    if not os.path.exists(outfolder):
        os.mkdir(arg.outfolder)
    outtar = os.path.join( arg.outfolder, 'out.tar' )
    open(outtar,'wb').write( r.content )
    print( 'Response successfully received' )
    tar = tarfile.open(outtar)
    tar.extractall(path=arg.outfolder)
    html = os.path.join( arg.outfolder, 'index.html' )
    shutil.cp( html, arg.outfile )  
    print( 'Files extracted' )


if __name__ == "__main__":
    parser = arguments()
    arg = parser.parse_args()
    assert os.path.exists( arg.infile )
    pathwayUpload( arg )
