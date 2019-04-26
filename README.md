# galaxy_selenzyme

Creating a tool within Galaxy to run Selenzyme.

See:

* Tutorial to create a Galaxy tool: https://galaxyproject.org/admin/tools/add-tool-tutorial/
* How to install it in the Galaxy container: https://github.com/bgruening/docker-galaxy-stable
* Example for Uniprot: https://toolshed.g2.bx.psu.edu/repository?repository_id=c8774310981b07c5

Plan:
- [x] Create a basic command line tool using Python `requests` that submits a the reaction SMILES and gets the predicted sequences.
- [x] Create a Galaxy Tool XML file.
- [x] Check that the Galaxy container has `requests` installed, otherwise add to the `docker-compose` file.
- [x] Mount the folder with the tool in the container.
- [x] Install the tool in Galaxy.
- [ ] Create a tool using Galaxy XML that post JSON request and receives a JSON response (no local tool running in the Galaxy server).
- [ ] Submit the purely XML tool to the [Galaxy Tool Shed](https://toolshed.g2.bx.psu.edu/).