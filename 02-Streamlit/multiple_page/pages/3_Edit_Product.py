import streamlit as st

st.title("Edit Product")

if 'editing_product_index' in st.session_state and st.session_state.editing_product_index is not None:
    product_to_edit = st.session_state.products[st.session_state.editing_product_index]

    with st.form("edit_product_form"):
        edited_name = st.text_input(
            "Product Name", value=product_to_edit['name'], key="edit_name")
        edited_price = st.number_input(
            "Price", value=product_to_edit['price'], min_value=0.0, format="%.2f", key="edit_price")
        edited_description = st.text_area(
            "Description", value=product_to_edit['description'], key="edit_description")

        submitted = st.form_submit_button("Save Changes")
        if submitted:
            if edited_name and edited_price is not None:
                st.session_state.products[st.session_state.editing_product_index] = {
                    "name": edited_name,
                    "price": edited_price,
                    "description": edited_description
                }
                st.success(f"Product '{edited_name}' updated successfully!")
                del st.session_state.editing_product_index  # Clear editing state
                st.switch_page("pages/1_Product_List.py")
            else:
                st.error("Product Name and Price are required.")
else:
    st.warning(
        "No product selected for editing. Please select a product from the list.")
    if st.button("Go to Product List"):
        st.switch_page("pages/1_Product_List.py")
