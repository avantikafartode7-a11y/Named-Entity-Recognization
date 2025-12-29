import streamlit as st
import spacy
import subprocess
import sys

st.title("Named Entity Recognition (NER) App")

@st.cache_resource
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except:
        # Install model if not present
        subprocess.run(
            [sys.executable, "-m", "spacy", "download", "en_core_web_sm"],
            check=True
        )
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

text = st.text_area(
    "Enter text",
    "Virat Kohli was born in Delhi and plays cricket for India"
)

if st.button("Extract Entities"):
    doc = nlp(text)

    if doc.ents:
        for ent in doc.ents:
            st.write(f"**Entity:** {ent.text}")
            st.write(f"**Label:** {ent.label_}")
            st.write("---")
    else:
        st.warning("No entities found")
