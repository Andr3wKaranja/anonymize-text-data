# Built a text anonymizer with Spacy and Streamlit dependencies
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://github.com/Andr3wKaranja/anonymize-text-data) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://github.com/Andr3wKaranja/anonymize-text-data) [![Heroku](https://pyheroku-badge.herokuapp.com/?app=anonimizer-text-webapp&style=flat-square)](https://anonimizer-text-webapp.herokuapp.com/) 

A web app to anonymize provided text data with Streamlit and Spacy.
## Installation
Clone the project and init a pipenv environment in it by installing the needed dependencies:

```bash
git clone https://github.com/Andr3wKaranja/anonymize-text-data.git
cd anonymizer/
pip install -r requirements.txt
streamlit run app.py
```

Dependencies used in this repo:
* `streamlit`: to build the UI
* `spacy`: to perform named entity recognition
* `st-annotated-text`: A simple component to display annotated text in Streamlit apps
* `black` to format the code locally. This package will only be used in dev mode.

I've also deployed it to [Heroku](https://anonimizer-text-webapp.herokuapp.com/) and made it live on internet for other users to use and play with:

![alt text](/images/image.png?raw=true)
