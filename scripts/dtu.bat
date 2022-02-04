@echo off

IF "%1" == "upgrade" goto upgrade
IF "%1" == "generate" goto generate
goto other

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

:done

@REM IF "%1" == "upgrade" (
@REM     IF "%2" == "--develop" (
@REM         git add .
@REM         git commit -m"fix"
@REM         git push
@REM     )
@REM     python -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
@REM ) ELSE (
@REM     dtu_python %1
@REM )

