@echo off

IF "%1" == "upgrade" goto upgrade
goto other

:upgrade
git add .
git commit -m"fix"
git push
python -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
goto done

:other
dtu %1
goto done

:done

