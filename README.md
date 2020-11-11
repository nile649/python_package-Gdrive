# Test

```
pip install -i https://test.pypi.org/simple/ Gdrive-nile649
```
```
from Gdrive import Gdrive
gdrive = Gdrive()
gdrive("1Z1RqRo0_JiavaZw2yzZG6WETdZQ8qX86", "lol2.zip")
```
# Project Folder

	Project Folder {Well}
	│ 
	│──Main Project Folder {Gdrive}
	│  │── <__init__.py> // File from where the main function will acts as import
	│  │── <Gdrive.py> // main func
	│  │── <Gdrive.sh> 
	│── tests {empty}
	│── setup.py
	│── LICENSE 
	│── README.md 

# Steps 

Step 1 : Register 
	   : https://test.pypi.org/account/register/ |Experimental server, pip is not avail to public on search|
	   : https://pypi.org/ |Public Version|

Step 2 : python -m pip install --user --upgrade setuptools wheel

Step 3 : python -m pip install --user --upgrade twine

Step 4 : python setup.py sdist bdist_wheel

Step 5 : python -m twine upload --repository testpypi dist/* |Enter credentials|

Step 6 : pip install -i https://test.pypi.org/simple/ Project_name_as_it_is_in_setup.py |Test server|


# Points to keep in mind

Use twine upload dist/* to upload your package and enter your credentials for the account you registered on the real PyPI. Now that you’re uploading the package in production, you don’t need to specify --repository; the package will upload to https://pypi.org/ by default.

Install your package from the real PyPI using pip install [your-package].

# Reference
1. https://packaging.python.org/tutorials/packaging-projects/
2. https://packaging.python.org/guides/using-testpypi/
3. https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script
4. https://stackoverflow.com/questions/4514751/pipe-subprocess-standard-output-to-a-variable
5. https://stackoverflow.com/questions/17242828/python-subprocess-and-running-a-bash-script-with-multiple-arguments
6. https://stackoverflow.com/questions/50794064/how-to-package-a-shell-script-in-a-pip-package
7. https://stackoverflow.com/questions/50585246/pip-install-creates-only-the-dist-info-not-the-package
