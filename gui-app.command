cd "$(dirname "$0")"
echo "\033[1;34mThis tool helps you convert a Flutter project into an IPA file.\033[0m"
echo "\033[1;34mYou will be prompted to enter the root directory of your Flutter project and the output directory for the IPA file.\033[0m"

source .venv/bin/activate
pip install -r requirements.txt
python app.py