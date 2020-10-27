# NewsForYou
Django web app designed to summarize and detect political bias in text

## Installation
First clone the reposirory, then optionally create a virtual environemt and activate it. Next pip install all the requirements. Finally cd into the 'newsBiasSite' folder and start the django server.

'''bash
git clone ##url##
python -m venv venv 
./venv/Scripts/activate
cd newsBiasSite
pip install -r requirements.txt
python manage.py runserver
'''


Hello all, 

The goal of this project is to create a website using Django. This code base touches many aspects of django, such as databases, the front end, and the backend.

To start this project I would first advise you create a virtual environment. Within the virtual encvironment download all the neccessary python libraries. This
can be found in the "requirements.txt" file.

To start the django server, cd into the main project directory and the type "pthon manage.py runserver".
This will start the serve running on your local host. 

The home page is where you can paste in an article to be summarized and politically scored. There is also a side box to add a comment.
The about page describes the project from a high level. 
The comments page keeps track of all comments in chronologicaly order (newest to oldest)