import streamlit as st
import pandas as pd

st.title("Product List")

if st.session_state.products:
    df = pd.DataFrame(st.session_state.products)
    st.dataframe(df, use_container_width=True)

    # Edit/Delete functionality (simplified)
    st.subheader("Actions")
    product_names = [p['name'] for p in st.session_state.products]
    selected_product_name = st.selectbox(
        "Select product to edit or delete:", product_names)

    if selected_product_name:
        selected_product_index = next((i for i, p in enumerate(
            st.session_state.products) if p['name'] == selected_product_name), None)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Edit Selected Product"):
                st.session_state.editing_product_index = selected_product_index
                st.switch_page("pages/3_Edit_Product.py")
        with col2:
            if st.button("Delete Selected Product"):
                del st.session_state.products[selected_product_index]
                st.success(f"Product '{selected_product_name}' deleted.")
                st.rerun()  # Refresh the page to show updated list
else:
    st.info("No products added yet. Go to 'Add Product' to add new products.")
