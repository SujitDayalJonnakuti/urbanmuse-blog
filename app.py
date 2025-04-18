import streamlit as st
from your_pipeline import generate_content  # Replace with your actual function

st.title("UrbanMuse Content Generator")
product = st.text_input("Product Name")
brand_guide = st.file_uploader("Upload Brand Style Guide")
if st.button("Generate"):
    result = generate_content(product, brand_guide)
    st.json(result)
