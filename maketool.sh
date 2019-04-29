#!/bin/bash
# author: Pablo Carbonell
# Create Selenzyme Galaxy tool using planemo.
#    --example_input reaction.csv \
#    --example_output out.csv \
#    --example_command 'python $__tool_directory__/toolSelenzyme.py $input1 $output1 -server $server' \

planemo tool_init --force \
    --id 'selenzyme' \
    --name 'Query Selenzyme: Enzyme sequence selection' \
    --requirement requests@2 \
    --example_command 'python $__tool_directory__/toolSelenzyme.py $input1 $output1' \
    --example_input 'reaction.csv' \
    --example_output 'out.csv' \
    --doi 10.1093/bioinformatics/bty065 \
    --help_from_command 'python3 toolSelenzyme.py -h'
    
planemo shed_init . --force \
    --name selenzyme \
    --owner pablocarb \
    --description 'Selenzyme tool: Enzyme sequence selection from reaction rules' \
    --category 'Systems Biology' \
    --homepage_url 'https://github.com/pablocarb/selenzyme_tool'
