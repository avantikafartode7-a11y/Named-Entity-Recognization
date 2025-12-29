import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition (NER) App")
st.write("Enter a sentence to extract named entities using spaCy")

# Text input
txt = st.text_area(
    "Enter text:",
    "Virat Kohli was born in Delhi and plays cricket for India"
)

if st.button("Extract Entities"):
    result = nlp(txt)

    if result.ents:
        st.subheader("Extracted Entities:")
        for ent in result.ents:
            st.write(f"**Entity:** {ent.text}")
            st.write(f"**Label:** {ent.label_}")
            st.write("---")
    else:
        st.warning("No entities found.")
