# emailAlchemy
Crowdsourced Spam Detection for emails

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites and Installation

Ensure that you have python 2.7, pip and virtualenv installed.

(Optional) You can also install SQLite Database browser from http://sqlitebrowser.org/ 

Download and install git and run the following command
```
git clone https://github.com/antiproblemist/emailAlchemy.git
```
The code has been optimized for Django 1.11 version.

The virtual enviornment folder ```alchemyenv``` contains the packages which are required and they also have been mentioned in the [requirements.txt](requirements.txt) file

### Running for the first time

Activate the virtual enviornment by the activate command (which may differ on differents os).

On Windows run the following command from your project directory ```.\alchemyenv\Scripts\activate```.

After activating the virtual enviornment run the following command ```python manage.py makemigrations alchemy``` and then ```python manage.py migrate```. This will create a new sqlite database in you project directory with the necessary tables.

After the abpve steps the project will be able to run using the following command ```python manage.py runserver 8000```. This will start your Django project on http://localhost:8000

### Authors

**Shahzeb Qureshi** - [Linkedin](https://www.linkedin.com/in/shahzebq)


### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
