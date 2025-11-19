import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the application
st.title("My First Streamlit App")

# Add a header
st.header("Interactive Data Display")

# Add some introductory text
st.write("This app demonstrates basic Streamlit components.")

# Create a text input widget
user_name = st.text_input("Enter your name:", "Guest")
st.write(f"Hello, {user_name}!")

# Create a slider widget
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# Create a selectbox widget
option = st.selectbox(
    "Which is your favorite fruit?",
    ("Apple", "Banana", "Orange", "Grape")
)
st.write(f"Your favorite fruit is: {option}")

# Create a checkbox and display conditional content
if st.checkbox("Show a DataFrame"):
    st.subheader("Random Data")
    # Create a simple DataFrame
    data = pd.DataFrame(
        np.random.rand(10, 3),
        columns=['Column A', 'Column B', 'Column C']
    )
    # st.dataframe(data)
    st.table(data)

# Add a button
if st.button("Click me!"):
    st.success("Button clicked!")

# Display a chart
st.subheader("Simple Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['a', 'b']
)
st.line_chart(chart_data)
