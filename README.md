# Bank security console.
*This is an internal repository for bank employees. If you got into this repository by accident, then you will not be able to run the script, because you do not have access to the database, but you can freely use the Python/HTML code or see how database queries are implemented.*

*The security console is a website that can be connected to a remote database with visits and pass cards of our bank employees.*
## Installation.
*Next, I'll tell you how to run the server through the terminal in PyCharm.*
+ Install Python3 latest version. Install PyCharm IDE, if you need it
   > To isolate the project, I would recommend using a virtual environment model. [vertualenv/venv](https://docs.python.org/3/library/venv.html)

+ Download _'Bank security console'_ repository from Github to PyCharm.
  >Note that, you can also import my repository from PyCharm "welcome" screen.  Select "Get from VCS".
+ Once you have opened the repository, call the terminal and create a virtualenv:
```zch
% virtualenv venv
```
+ Activate the environment:
```zch
% source venv/bin/activate
```
+ Then use pip (or pip3, there is a conflict with Python2) to install dependencies (use requirements.txt file):
```zch
% python3 -m pip install -r requirements.txt
```
+ Export your sensitive data using these two commands, replacing variables with your key values:
```zsh
% SECRET_PASSWORD='DEFAULT_KEY'
% DB_URL="postgres://..."
```
 URL schema: __postgres://USER:PASSWORD@HOST:PORT/NAME__

> __Remark__: In this way, environment variable works only for the duration that shell is live. If you close the shell and restart it, you have to set environmental variable again. Env from environs prevents us from doing this repetitive work. For permanent set, create .env file and add variables in this format:
>  ``` python
> SECRET_PASSWORD = 'DEFAULT_KEY'
> DB_URL = "postgres://USER:PASSWORD@HOST:PORT/NAME"
> ```
+ Execute the command to start the server:
``` zsh
% python3 manage.py runserver 0.0.0.0:8000
```  
+ Let's try [localhost](http://127.0.0.1:8000)
## Project goals.
*The program was designed by a student from online web development courses for educational purposes [Devman](https://dvmn.org).*