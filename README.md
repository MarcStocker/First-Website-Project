Marc's First Website
====================

This is the final project for Chico's CINS-465 Web development class, with Bryan Dixon.

This website will implement Python3 and Django as the backend. 
Of course other languages such as HTML, CSS and JS will be used for the front end.

The purpose of this website is to build a foundation for a personal website for my friend Edgar (Instagram name: EdgarRaw) to upload and keep track of his recipes, also allowing his Instagram followers to visit his page and look up specific recipes.

Scope
-----

Unsure of what the entire scope will be at this point.
At the moment my current plans are to imlpement a user system so Edgar can log in and edit recipes, and to create a search system using tags, or regex to allow users (both signed in and not) to search for recipes with key words/ingrediants

Requirements for using VirtualEnv
---------------------------------

I have created a virtualenv folder to hold all of the program software that will be used with this project to make it easy to program using the specific versions of each program found in *REPO/codingenv/requirements.txt*

How to use virtualenv
---------------------
These instructions are assuming you are using PowerShell
First off you need to have it installed. To install virtualenv

0. Download and install Python.
	* Make sure Python is in your environment `PATH` variable
0. Install pip - This link may be helpful for Windows users (https://pip.pypa.io/en/latest/installing/)
	* Download get-pip.py (https://bootstrap.pypa.io/get-pip.py)
	* Then run the following command - `python get-pip.py`
0. Upgrade pip - `python -m pip install -U pip`
0. Install virtualenv - `pip install virtualenv`
	- Hopefully that's all that needs to be done. I`ll update this if I figure out extra steps/different commands are needed in windows.
0. Navigate to the virtualenv folder - `*REPO/codingenv/Sources*`
0. Run `activate.ps1` found in the virtualenv's *Sources* folder by simply typing - `.\activate.ps1`
	- If your PS says `execution of scripts is disabled on this system` You`ll need to execute the command `Set-ExecutionPolicy RemoteSigned`. Enter `y`, you should not have to do this step again.

THAT'S it! Your commandline should now start with `(codingenv)` followed by your current folder path. 

If you type in `pip freeze` it should show you all current languages being used. 

* To exit the virtualenv type `deactivate`

Launching virtualenv
--------------------

From the projects source dir type - `\codingenv\Scripts\activate.ps1`
Or from the *edgarrawsite* project folder - `..\codingenv\Scripts\activate.ps1`
 + I`ll look for an easier way to accomplish this... but ultimately it's not high on my list, and from my current research looks to be impossible. :(


----------------
*Most of this information is for myself so that I don`t have to re-google everything if I reinstall my OS*

