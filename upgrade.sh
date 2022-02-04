#!/bin/sh
git add .
git commit -m"fix"
git push
C:/Users/magnu/AppData/Local/Microsoft/WindowsApps/python.exe -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
read