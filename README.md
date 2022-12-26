## How to create a venv python in project :bookmark:

- First, make a folder for a project
- Next, open terminal and use command line in below, which [python -m venv <name_env>]
```
python -m venv venv
```
Or, if you already have another python version in local you can use [python<version> -m venv <name_env>]
```
python3.9 -m venv venv
```
- after that for activate a env use command in below
```
.\venv\Scripts\Activate.ps1   
```
- for deactive venv, using command in below
```
deactivate
```
- enjoy :tada:

# Extra
For installing package for faster you can use requirements.txt, and write all package with version into that .txt. After write all package in .txt, you can use command in below
```
pip install -r requirements.txt
```
