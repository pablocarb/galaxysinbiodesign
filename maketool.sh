#!/bin/bash
# author: Pablo Carbonell
# Create Selenzyme Galaxy tool using planemo.
#    --example_input reaction.csv \
#    --example_output out.csv \
#    --example_command 'python $__tool_directory__/toolSelenzyme.py $input1 $output1 -server $server' \

# Generate tool backbone (additional params need to be entered manually 
planemo tool_init --force \
    --id 'selenzyme' \
    --name 'Selenzyme' \
    --description 'enzyme sequence selection from reaction template' \
    --requirement requests@2 \
    --example_command 'python $__tool_directory__/toolSelenzyme.py $input1 $output1 -server $server' \
    --example_input 'reaction.csv' \
    --example_output 'out.csv' \
    --doi 10.1093/bioinformatics/bty065 \
    --help_from_command 'python3 toolSelenzyme.py -h'
   
# Init shed repository
planemo shed_init . --force \
    --name synbiodesign \
    --owner pablocarb \
    --description 'BioCAD for Industrial Biotechnology' \
    --category 'Systems Biology' \
    --homepage_url 'https://github.com/pablocarb/galaxysynbiodesign'

# Create repository in the toolshed
planemo shed_create \
    --shed_target toolshed \
    --shed_key_from_env TOOLSHED 

# Update repository in the toolshed
planemo shed_update \
    --check_diff --shed_target toolshed \
    --shed_key_from_env TOOLSHED

