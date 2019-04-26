#!/bin/bash
# author: Pablo Carbonell
# Create Selenzyme Galaxy tool using planemo.
#    --example_input reaction.csv \
#    --example_output out.csv \

planemo tool_init --force \
    --id 'selenzyme' \
    --name 'Query Selenzyme: Enzyme sequence selection' \
    --requirement requests@2 \
    --example_command 'python $__tool_directory__ toolSelenzyme.py $input $output' \
    --example_input 'reaction.csv' \
    --example_output 'out.csv' \
    --doi 10.1093/bioinformatics/bty065 \
    --help_from_command 'python3 toolSelenzyme.py -h'
    
