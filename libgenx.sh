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

echo "> Welcome!"

echo "  Mode: $mode"
echo "  Author: $author"
echo "  Title: $title"

echo "> Setting up application..."
pipenv run python libgenx-$mode.py -a "$author" -t "$title"