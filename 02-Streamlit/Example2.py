import streamlit as st

st.set_page_config(page_title="App Overview", layout="wide")

# --- Overview Section ---
st.title("My Data Application Overview")
st.markdown("""
This application provides an overview of key performance indicators and detailed insights into our operational data.
""")

st.metric(label="Total Sales", value="$1.2M", delta="10% vs last month")
st.bar_chart({"Category A": 100, "Category B": 150, "Category C": 80})

# --- Details Section ---
with st.expander("Click for Detailed Analysis"):
    st.header("Detailed Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales by Region")
        st.dataframe({"Region": ["East", "West", "North", "South"], "Sales": [
                     300000, 450000, 200000, 250000]})

    with col2:
        st.subheader("Customer Demographics")
        st.line_chart([10, 20, 15, 25, 30])  # Example data

    st.subheader("Further Analysis Options")
    selected_product = st.selectbox(
        "Select a Product:", ["Product A", "Product B", "Product C"])
    st.write(f"Showing details for: {selected_product}")

    if selected_product == "Product A":
        st.bar_chart({"Category A": 100})
    if selected_product == "Product B":
        st.bar_chart({"Category B": 150})
    if selected_product == "Product C":
        st.bar_chart({"Category C": 80})
