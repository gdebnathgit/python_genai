import streamlit as st

st.title("Add New Product")

with st.form("add_product_form"):
    product_name = st.text_input("Product Name", key="add_name")
    product_price = st.number_input(
        "Price", min_value=0.0, format="%.2f", key="add_price")
    product_description = st.text_area("Description", key="add_description")

    submitted = st.form_submit_button("Add Product")
    if submitted:
        if product_name and product_price is not None:
            new_product = {"name": product_name, "price": product_price,
                           "description": product_description}
            st.session_state.products.append(new_product)
            st.success(f"Product '{product_name}' added successfully!")
            st.switch_page("pages/1_Product_List.py")  # Navigate back to list
        else:
            st.error("Product Name and Price are required.")
