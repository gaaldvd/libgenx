# todo

## readme

- installation: python, Qt6, pip
  - install.sh
    - pipenv: `pip install pipenv --user`
    - pipenv setup: `pipenv sync`
    - make start.sh executable: `chmod -x start.sh`
- usage
  - config file, cli, gui
  - update through git
  - update virtualenv through pipenv: `pipenv update`

## ui

- toolbar
  - config: download location, preferred/filter file type
  - about
  - close
- input
  - search fields: author, title
- output
  - list (QTableWidget)
    - double-click: download preferred file type from primary mirror
    - context menu: alternative mirrors, file types
- statusbar
