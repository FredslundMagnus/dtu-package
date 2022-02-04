#!/bin/sh
git add .
git commit -m"fix"
git push
read
C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git