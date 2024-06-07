echo "> Checking requirements..."
echo "> Qt6 version: $(qmake6 --version)"
echo "> Python version: $(python --version)"
echo "> PIP version: $(pip --version)"
echo "> pipenv version: $(pipenv --version)"

until [ "$git_up" = "y" ] || [ "$git_up" = "Y" ] || [ "$git_up" = "n" ] || [ "$git_up" = "N" ]
do
  read -r -p "Update git repository? [y/n] " git_up
done

until [ "$pip_up" = "y" ] || [ "$pip_up" = "Y" ] || [ "$pip_up" = "n" ] || [ "$pip_up" = "N" ]
do
  read -r -p "Update python environment? [y/n] " pip_up
done

if [ "$git_up" = "y" ] || [ "$git_up" = "Y" ]
then
  echo "> Updating git repository..."
  git pull
fi
echo "> Git repository is up to date."

if [ "$pip_up" = "y" ] || [ "$pip_up" = "Y" ]
then
  echo "> Updating python environment..."
  pipenv update
fi
echo "> Python environment is up to date."

echo "> Pipfile verification... $(pipenv verify)"
echo "> pyside6: $(pipenv run pip show pyside6)"
echo "> libgen_api: $(pipenv run pip show libgen_api)"

echo "> Done. Goodbye!"