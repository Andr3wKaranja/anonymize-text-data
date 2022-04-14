import streamlit as st
import spacy
from annotated_text import annotated_text


@st.cache(show_spinner=False, allow_output_mutation=True, suppress_st_warning=True)
def load_models():
    english_model = spacy.load("./models/en/")
    french_model = spacy.load("./models/fr/")
    models = {
        "en": english_model,
        "fr": french_model
    }
    return models


def process_text(doc, selected_entities, anonymize=False):
    tokens= []
    for token in doc:
        if (token.ent_type_ == "PERSON") & ( "PER" in selected_entities):
            tokens.append((token.text, "PERSON", "#faa"))
        elif (token.ent_type_ in  ["GPE", "LOC"]) & ( "LOC" in selected_entities):
            tokens.append((token.text, "LOCATION", "#fda"))
        if (token.ent_type_ == "ORG") & ( "ORG" in selected_entities):
            tokens.append((token.text, "ORGANIZATION", "#afa"))
        else:
            tokens.append((" " + token.text + " "))
    
    if anonymize:
        anonmized_tokens = []
        for token in tokens:
            if type(token) == tuple:
                anonmized_tokens.append(("X" * len(token[0]), token[1], token[2]))
            else:
                anonmized_tokens.append(token)
                
        return anonmized_tokens
    return tokens

models = load_models()

selected_language = st.sidebar.selectbox("Select a language", options=["English(en)", "French(fr)"])
selected_entities = st.sidebar.multiselect(
    "Select the entities you wish to detect",
    options=["LOC", "PERSON", "ORG"],
    default=["LOC", "PERSON", "ORG"]
)

selected_model=models[selected_language]

text_input = st.text_area("Type a text to anonymize")

uploaded_file = st.file_uploader("or Upload a file", type=["doc", "docx", "pdf", "txt",])
if uploaded_file is not None:
    text_input = uploaded_file.get_value()
    text_input = text_input.decode("utf-8")
    
anonymize = st.checkbox("Anonymize")
# process the text
doc= selected_model(text_input) 
tokens = process_text(doc, selected_entities)

# *tokens unpacks the tuple
annotated_text(*tokens)

if anonymize:
    st.markdown("** Anonymized text**")
    st.markdown("---")
    anonymized_tokens = process_text(doc, selected_entities, anonymize=anonymize)
    annotated_text(*anonymized_tokens)
