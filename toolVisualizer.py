#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mar 19

@author: Pablo Carbonell
@description: Pathway visualizer.

"""
import argparse
import os
from rpviz.main import run

def arguments():
    parser = argparse.ArgumentParser(description='toolVisualizer: Pathway visualizer. Pablo Carbonell, SYNBIOCHEM, 2019')
    parser.add_argument('infile', 
                        help='Input SBML pathway file.')
    parser.add_argument('outfile', 
                        help='Output HTML file.')
    return parser
    
def runVisualizer( infile, outfile ):
    run(infile,outfile)



if __name__ == "__main__":
    parser = arguments()
    arg = parser.parse_args()
    assert os.path.exists(arg.infile)
    runVisualizer( arg.infile, arg.outfile )
