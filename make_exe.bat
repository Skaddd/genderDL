
pyinstaller --onedir --add-data="./assets/*;assets" --add-data="./models/*;models" --add-data="./portrait/;portrait"  --add-data="./pictures/*;pictures" --add-data="./detection/;detection" --add-data="./tmp/*;tmp" Window1.py