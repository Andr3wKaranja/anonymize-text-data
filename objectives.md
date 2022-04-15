## Notes
Dependencies:
* `streamlit`: to build the UI
* `spacy`: to perform named entity recognition
* `st-annotated-text`: A simple component to display annotated text in Streamlit apps
* `black` to format the code locally. This package will only be used in dev mode.

Collect the user inputs and perform the required operations:
* the language of the model(en, fr)
* the entity types(PERSON, ORG, LOC)
* the input text in the text area
* the file uploader to upload TXT files
