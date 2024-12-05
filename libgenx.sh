# validate options
if [ "$#" -eq 0 ]; then
    echo "> Usage: $0 [-c/-g] ['query']"
    exit 1
fi

# interpret options
while getopts "cg" flag; do
  case $flag in
    c) mode="cli";;
    g) mode="gui";;
    *)
      echo "> Usage: $0 [-c/-g] ['query']"
      exit 1;;
  esac
done

if [ -n "$2" ]; then
    echo "> Query: $2"
else
    echo "> No query specified."
fi

# start script
# clear
pipenv run python src/libgenx_$mode.py "$2"
