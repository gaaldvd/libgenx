echo "> Updating git repository..."
git pull origin main
echo "> Updating pipenv packages..."
pipenv update

echo "> Pipfile verification... $(pipenv verify)"
echo "> pyside6: $(pipenv run pip show pyside6)"
echo "> libgen_api: $(pipenv run pip show libgen_api)"

echo "> Done. Goodbye!"