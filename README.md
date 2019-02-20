# galaxy_selenzyme

Creating a tool within Galaxy to run Selenzyme.

See:

* Tutorial to create a Galaxy tool: https://galaxyproject.org/admin/tools/add-tool-tutorial/
* How to install it in the Galaxy container: https://github.com/bgruening/docker-galaxy-stable

Plan:
* Create a basic tool using Python `requests` that submits a the reaction SMILES and gets the predicted sequences.
* To do: check that the Galaxy container has `requests` installed, otherwise add to the `docker-compose` file.