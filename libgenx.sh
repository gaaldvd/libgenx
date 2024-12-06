# validate options
if [ "$#" -eq 0 ]; then
    echo "> Usage: $0 [-u] [-c/-g] ['query']"
    exit 1
fi

# interpret options
while getopts "ucg" flag; do
  case $flag in
    u)
      echo "> Updating LibGenX..."
      ./update.sh
      exit 0;;
    c) mode="cli";;
    g) mode="gui";;
    *)
      echo "> Usage: $0 [-c/-g] ['query']"
      exit 1;;
  esac
done

# start application
if [ -n "$2" ]; then
    # echo "> Query: $2"
    pipenv run python src/libgenx_$mode.py "$2"
else
    # echo "> No query specified."
    pipenv run python src/libgenx_$mode.py
fi
