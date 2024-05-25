# todo

## readme

### installation 
- install from package manager: git, python, Qt6, pip, pipenv (`pip install pipenv --user`)
- clone git repository: `git clone https://github.com/strugamano/libgenx.git`
- run `sh install.sh`

### usage
- cli
- gui: `./ligenx.sh`
- config file: {"downloadDir": "/home/<user>/<directory>", "pdfOnly": <true/false>}
- update script: `./update.sh`

## scripts

### libgenx-gui.py
- connect show_details() to right-click on list items?
- itemSelectionChanged() on listwidget
  - new search -> currentRow() runs out of range
  - click -> show_details() runs twice
- try to reimplement context menu with customContextMenuRequested() (https://wiki.python.org/moin/PyQt/Handling%20context%20menus)

### libgenx-cli.py
- the whole thing...