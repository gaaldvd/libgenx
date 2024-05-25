echo "> Checking requirements..."
echo "> Qt6 version: $(qmake6 --version)"
echo "> Python version: $(python --version)"
echo "> PIP version: $(pip --version)"
echo "> pipenv version: $(pipenv --version)"

echo "> Setting up application..."
pipenv run python libgenx-gui.py

echo "> Goodbye!"