@echo off

IF "%1" == "upgrade" goto upgrade
IF "%1" == "generate" goto generate
IF "%1" == "init" goto other
goto help

:upgrade
IF "%2" == "--develop" (
    git add .
    git commit -m"fix"
    git push
)
python -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
goto done

:generate
python generate.py
goto done


:other
dtu_python %1
goto done

:help
echo Welcome to the dtu package! Try one of the following commands:
echo dtu init
echo dtu upgrade
echo dtu generate
goto done

:done

