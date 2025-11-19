import streamlit as st

st.set_page_config(page_title="Product Management App", layout="wide")

st.title("Welcome to Product Management")
st.write("Use the sidebar to navigate through the app.")

if 'products' not in st.session_state:
    st.session_state.products = []  # Initialize an empty list to store products
