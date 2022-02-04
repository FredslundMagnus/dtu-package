#!/bin/python
git add .
git commit -m"fix"
git push
python --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
read