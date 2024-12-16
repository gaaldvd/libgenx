# validate options
if [ "$#" -eq 0 ] || [[ "$1" != "-u" && "$1" != "-c" && "$1" != "-g" ]]; then
    echo "> Usage: $0 [-u] [-c/-g] ['query'] [filters]"
    exit 1
fi

# interpret options
while getopts "ucg" flag; do
  case $flag in
    u)
      echo "> Updating LibGenX..."
      ./update.sh
      exit 0;;
    c)
      mode="cli"
      break;;
    g)
      mode="gui"
      break;;
    *)
      echo "> Usage: $0 [-u] [-c/-g] ['query'] [filters]"
      exit 1;;
  esac
done

# start application
if [ -n "$2" ]; then
    query="$2"
    # echo "> Query: $query"
    shift 2
    if [ "$#" -eq 0 ]; then
        pipenv run python src/libgenx_$mode.py "$query"
    else
        args="$@"
        # echo "> Args: $args"
        pipenv run python src/libgenx_$mode.py "$query" "$args"
    fi
else
    # echo "> No query specified."
    pipenv run python src/libgenx_$mode.py
fi
