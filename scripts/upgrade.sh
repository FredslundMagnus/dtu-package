#!/bin/sh
module -s load python3
source ../project-env/bin/activate
python -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git