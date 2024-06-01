echo "> Checking requirements..."
echo "> Qt6 version: $(qmake6 --version)"
echo "> Python version: $(python --version)"
echo "> PIP version: $(pip --version)"
echo "> pipenv version: $(pipenv --version)"

while getopts "cga:t:" flag; do
  case $flag in
    c) mode="cli";;
    g) mode="gui";;
    a) author="$OPTARG";;
    t) title="$OPTARG";;
    *)
      echo "> Usage: $0 [-c/-g] [-a author] [-t title]"
      exit 1;;
  esac
done

echo "Mode: $mode"
echo "Author: $author"
echo "Title: $title"

echo "> Setting up application..."
pipenv run python libgenx-$mode.py -a "$author" -t "$title"

echo "> Goodbye!"