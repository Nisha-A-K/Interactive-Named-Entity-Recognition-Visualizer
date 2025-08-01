import streamlit as st
import spacy
from spacy import displacy

# A best practice in Streamlit is to cache heavy resources.
# The spaCy model is a heavy resource, so we use @st.cache_resource
# to load it only once and reuse it across user sessions.
@st.cache_resource
def load_model(model_name):
    """Loads the spaCy model and returns it."""
    st.info(f"Loading model '{model_name}'...")
    nlp = spacy.load(model_name)
    st.success(f"Model '{model_name}' loaded successfully!")
    return nlp

# Default example text for the text area
DEFAULT_TEXT = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California on April 1, 1976. It is one of the most valuable companies in the world."

# --- App UI ---

# Set the page title and a descriptive header
st.set_page_config(page_title="Interactive NER Visualizer", layout="wide")
st.title("Interactive Named Entity Recognition (NER) Visualizer")

# A small section to explain the app
st.markdown("""
This tool highlights named entities (like People, Organizations, Locations, etc.) in the text you provide. 
It uses a pre-trained model from the `spaCy` library.
""")

# Load the spaCy model. We are using the small English model.
# The load_model function is cached, so this will be fast after the first run.
nlp = load_model("en_core_web_sm")

# Create the text area for user input
st.header("Enter Your Text")
text = st.text_area("Paste your text below and see the entities highlighted in real-time.", value=DEFAULT_TEXT, height=200)

# --- Processing and Visualization ---

# Only process the text if there is something to process
if text:
    # Process the text with the spaCy model
    doc = nlp(text)

    # Check if any entities were found
    if doc.ents:
        st.header("Recognized Entities")
        
        # Use displacy to generate the HTML for the entity visualization
        # jupyter=False makes it return the raw HTML string
        html = displacy.render(doc, style="ent", jupyter=False)
        
        # Display the HTML in the Streamlit app.
        # unsafe_allow_html=True is required to render the HTML.
        st.write(html, unsafe_allow_html=True)
    else:
        st.info("No entities were found in the provided text.")
