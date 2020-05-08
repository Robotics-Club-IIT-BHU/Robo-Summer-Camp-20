@Echo OFF
python -m pip install wheel 
curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python
pause
ECHO This might take well over 10-15 minutes.
pipenv run pipenv install --skip-lock pybullet
pause
set /p id="		Enter the file to be run:    "
pipenv run python %id%
pause