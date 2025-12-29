import streamlit as st
import spacy

# 1. Load the model with caching to prevent reloading on every click
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# 2. Streamlit UI
st.title("🏃‍♂️ Cricket Entity Extractor")
st.write("Enter a sentence to identify names, places, and organizations.")

# Text input
default_text = "Virat Kohli was born in Delhi and plays cricket for India"
user_text = st.text_area("Input Text:", value=default_text)

if st.button("Extract Entities"):
    doc = nlp(user_text)
    
    if len(doc.ents) > 0:
        st.subheader("Results:")
        # Display results in a clean format
        for ent in doc.ents:
            st.write(f"**Entity:** `{ent.text}`  →  **Label:** `{ent.label_}` ({spacy.explain(ent.label_)})")
    else:
        st.warning("No entities found in this text.")
