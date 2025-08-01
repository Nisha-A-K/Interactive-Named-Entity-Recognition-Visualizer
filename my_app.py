import streamlit as st
import platform
import sys
import pip._internal.utils.compatibility_tags

st.set_page_config(layout="wide")

st.title("Streamlit Platform Diagnostics")
st.info("Please copy and paste all the information below in your reply.")

# --- Section 1: Python Version ---
st.header("1. Python Version")
st.code(f"sys.version: {sys.version}")

# --- Section 2: Platform Architecture ---
st.header("2. Platform Architecture")
st.code(f"platform.machine(): {platform.machine()}")
st.code(f"platform.platform(): {platform.platform()}")

# --- Section 3: Supported Pip Tags (Most Important) ---
st.header("3. Supported Pip Tags")
st.write("These are the types of 'wheel' (.whl) files this platform can install.")
st.write("This is the most critical information needed.")

try:
    tags = pip._internal.utils.compatibility_tags.get_supported()
    # Format the tags for easy reading in a text area
    tags_str = "\n".join([str(t) for t in tags])
    st.text_area("Copy these tags:", value=tags_str, height=400)
except Exception as e:
    st.error(f"Could not get pip tags: {e}")
    st.write("If this fails, the other information is still useful.")
