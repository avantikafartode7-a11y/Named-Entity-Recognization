import streamlit as st
import spacy

# Load the model
# We use st.cache_resource so the model only loads once, making the app faster
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

st.title("Named Entity Recognizer")
st.write("Enter text below to extract entities like names, locations, and organizations.")

# User Input
user_input = st.text_area("Input Text", "Virat Kohli was born in Delhi and plays cricket for India")

if st.button("Extract Entities"):
    doc = nlp(user_input)
    
    if not doc.ents:
        st.write("No entities found.")
    else:
        # Display in a nice table
        data = [{"Entity": ent.text, "Label": ent.label_} for ent in doc.ents]
        st.table(data)
        
        # Also print to logs for debugging
        for ent in doc.ents:
            st.write(f"**{ent.text}** is a `{ent.label_}`")
