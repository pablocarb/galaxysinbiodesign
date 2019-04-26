#!/bin/bash
# author: Pablo Carbonell
# Create Selenzyme Galaxy tool using planemo.
#    --example_input reaction.csv \
#    --example_output out.csv \

planemo tool_init --force \
    --id 'selenzyme' \
    --name 'Query Selenzyme: Enzyme sequence selection' \
    --requirement requests@2 \
    --requirement python@3 \
    --example_command 'python3 toolSelenzyme.py $input $output' \
    --example_input 'reaction.csv' \
    --example_output 'out.csv'
    --doi 10.1093/bioinformatics/bty065 \
    --help_text 'This tool calls Selenzyme to select enzyme sequences for a given target reaction represented in SMARTS.'
    
