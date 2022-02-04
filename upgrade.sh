#!/bin/python
git add .
git commit -m"fix"
git push
python -m pip --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
read