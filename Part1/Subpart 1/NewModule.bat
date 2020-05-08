@Echo OFF
Echo Here You would like to install a module
Echo So Dont continue if you haven't installed using Installation.bat
pause
set /p nam="		Enter the Module you want to install:    "
Echo       Do you want to update the module or install 
Echo       Install---0
Echo       Update----1
set /p choi=" Input any one :  "
IF %choi%==1 (pipenv run pipenv update %nam%) ELSE (pipenv run pipenv install --skip-lock %nam%)
pause