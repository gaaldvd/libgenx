echo "Installing pipenv..."
pip install pipenv --user
echo "Setting up pipenv..."
pipenv sync
echo "Configuring start script priviliges..."
chmod -x libgenx.sh
echo "Done."