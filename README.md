# Galaxy wrappers for SynBio Design Tools 

## galaxy_selenzyme

Creating a tool within Galaxy to run [Selenzyme](http://selenzyme.synbiochem.co.uk).

See:

* Tutorial to create a Galaxy tool: https://galaxyproject.org/admin/tools/add-tool-tutorial/
* How to install it in the Galaxy container: https://github.com/bgruening/docker-galaxy-stable
* Example for Uniprot: https://toolshed.g2.bx.psu.edu/repository?repository_id=c8774310981b07c5

Plan:
- [x] Create a basic command line tool using Python `requests` that submits a the reaction SMILES and gets the predicted sequences.
- [x] Create a Galaxy Tool XML file.
- [x] Check that the Galaxy container has `requests` installed, otherwise add to the `docker-compose` file.
- [x] Mount the folder with the tool in the container.
- [x] Install the tool locally in Galaxy.
- [x] Use planemo in order to create a repository in the toolshed.
- [x] Register in the toolshed.
- [x] Install in the Galaxy container from the toolshed.
- [ ] Create a tool using Galaxy XML that post JSON request and receives a JSON response (no local tool running in the Galaxy server).
- [ ] Submit the purely XML tool to the [Galaxy Tool Shed](https://toolshed.g2.bx.psu.edu/).

To learn more about Selenzyme:

Carbonell, Pablo, et al. Selenzyme: enzyme selection tool for pathway design. *Bioinformatics* 34: 2153-2154, (2018). https://doi.org/10.1093/bioinformatics/bty065

## galaxy_OptBioDes

Creating a tool within Galaxy to run OptBioDes (optimal design of experiments).

Plan:
- [x] Create a basic command line tool using Python that submits a ``CSV`` with the design specifications sheet.
- [x] Create a Galaxy Tool XML file.
- [x] Use planemo in order to create a repository in the toolshed.
- [x] Register in the toolshed.
- [x] Install in the Galaxy container from the toolshed.
- [ ] Write documentiation about the design specifications sheet.

## galaxy_RPViz

A tool to visualize pathways by querying an RPViz server.

* Note *: `RPViz` returns an interactive HTML file that runs javascript. The `RPViz` tools has to be included in the [Galaxy whitelist](https://docs.galaxyproject.org/en/latest/admin/config.html).



