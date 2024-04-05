echo "Checking requirements..."
echo "> Qt6 version: $(qmake6 --version)"
echo "> Python version: $(python --version)"
echo "> PIP version: $(pip --version)"
echo "> pipenv version: $(pipenv --version)"
echo "  > Pipfile verification... $(pipenv verify)"
echo "  > pyside6: $(pipenv run pip show pyside6)"
echo "  > libgen_api: $(pipenv run pip show libgen_api)"

echo "Setting up application..."
pipenv run python libgenx-gui.py

echo "Goodbye!"