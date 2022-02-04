@echo off
IF "%1" == "upgrade" (
    IF "%2" == "--develop" (
        git add .
        git commit -m"fix"
        git push
        python -m pip install --upgrade --force-reinstall git+https://github.com/FredslundMagnus/dtu-package.git
    )
    
) ELSE (
    dtu_python %1
)

