echo "Checking requirements..."
echo "> Qt6 version: $(qmake6 --version)"
echo "> Python version: $(python --version)"
echo "> PIP version: $(pip --version)"
echo "  > pyside6: $(pip show pyside6)"
echo "> pipenv version: $(pipenv --version)"
echo "  > Pipfile verification... $(pipenv verify)"
echo "  > libgen_api: $(pipenv run pip show libgen_api)"

echo "Setting up application..."
pipenv run python libgenx-cli.py

echo "Goodbye!"