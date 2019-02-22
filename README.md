# galaxy_selenzyme

Creating a tool within Galaxy to run Selenzyme.

See:

* Tutorial to create a Galaxy tool: https://galaxyproject.org/admin/tools/add-tool-tutorial/
* How to install it in the Galaxy container: https://github.com/bgruening/docker-galaxy-stable

Plan:
- [x] Create a basic command line tool using Python `requests` that submits a the reaction SMILES and gets the predicted sequences.
- [x] Create a Galaxy Tool XML file.
- [ ] Check that the Galaxy container has `requests` installed, otherwise add to the `docker-compose` file.
- [ ] Mount the folder with the tool in the container.
- [ ] Install the tool in Galaxy.