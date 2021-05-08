@echo off
goto exist

:exist
if not exist "null.data" (
    pip install PySimpleGui
    pip install Rpc
    echo null >> null.data
    goto perg
) else (
    goto start
)

:perg
set /p per="voce tem certeza que tem o python instalado? (y/n)"
if '%per%' == 'y' goto exist
if '%per%' == 'n' goto py

:py
start https://www.python.org/downloads/release/python-395/


:start
python bm.py