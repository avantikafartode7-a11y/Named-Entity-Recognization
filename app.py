import streamlit as st
import spacy

st.title("Named Entity Recognition (NER) App")

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

try:
    nlp = load_model()
except Exception as e:
    st.error("spaCy model not loaded properly.")
    st.stop()

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
