# NewsForYou
Django web app designed to summarize and detect political bias in text

## Installation
First clone the reposirory, then optionally create a virtual environemt and activate it. Next pip install all the requirements. Finally cd into the 'newsBiasSite' folder and start the django server.

```bash
git clone ##url##
python -m venv venv 
./venv/Scripts/activate
cd newsBiasSite
pip install -r requirements.txt
```

## Usage
```bash
python manage.py runserver
```
- The home page is where you can paste in an article to be summarized and politically scored. There is also a side box to add a comment.
- The about page describes the project from a high level. 
- The comments page keeps track of all comments in chronological order (newest to oldest)

## AI Model
The AI Model is a support vector machine created from ~4,000 summarized political articles. Each article was scraped from far left, neutral or far right news sites and scored as either a 1, 3, or 5 accordingly. News sites were determined from https://www.allsides.com/media-bias/media-bias-ratings. 


## Tools Used
- Python 
- sklearn (SVM)
- gensim (text cleansing)
- django (website and database)
    - HTML
    - CSS
    - Javascript
    - SQLite

## Author
Kyle McIntyre

## Licence
GNU General Public License v3.0
