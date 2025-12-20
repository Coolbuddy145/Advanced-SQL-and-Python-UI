import streamlit as st
import pandas as pd
from db_queries import (
    total_supplier, total_products, total_categories,
    total_sales, total_restock, low_stock,
    supplier_details, product_suppliers, products_reorder,
    sql, get_products, get_prod_hist,
    get_cat, get_sup, call_sp, reorder
)

# ----------------------------------------------------- Sidebar ----------------------------------------------------------

st.sidebar.title("📦 Inventory Dashboard")
st.sidebar.markdown("Manage inventory & supply chain")
option = st.sidebar.radio(
    "🔍 Select Section",
    ['📊 Basic Operation', '⚙️ Operational Tasks']
)

# ------------------------------------------------- Basic Information Page -----------------------------------------

if option == '📊 Basic Operation':
    st.title("📦 Inventory & Supply Chain Management")
    st.markdown("### 📊 Key Business Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👥 Total Suppliers", total_supplier())
    with col2:
        st.metric("📦 Total Products", total_products())
    with col3:
        st.metric("🗂️ Total Categories", total_categories())

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("💰 Sales (Last 10 Months)", total_sales())
    with col5:
        st.metric("🔄 Restock Value (Last 10 Months)", total_restock())
    with col6:
        st.metric("⚠️ Low Stock (No Reorder)", low_stock())

    st.divider()

    st.markdown("### 🏭 Supplier Contact Details")
    st.dataframe(supplier_details(), use_container_width=True)

    st.markdown("### 📦 Products with Supplier & Stock")
    st.dataframe(product_suppliers(), use_container_width=True)

    st.markdown("### 🚨 Products Needing Reorder")
    st.dataframe(products_reorder(), use_container_width=True)

# ------------------------------------------------- Operational Task Page -----------------------------------------

elif option == '⚙️ Operational Tasks':
    st.title("⚙️ Inventory Operations")
    st.markdown("### 🛠️ Perform Operational Tasks")

    option_1 = st.selectbox(
        "🧭 Choose a Task",
        ['➕ Add a New Product', '📜 Product History', '🔄 Place Reorder']
    )

    # -------------------------------- ADD PRODUCT --------------------------------

    if option_1 == '➕ Add a New Product':
        st.markdown("### ➕ Add New Product to Inventory")

        with st.form('Add New Product'):
            product_name = st.text_input("📦 Product Name")
            category = st.selectbox("🗂️ Category", options=get_cat())
            price = st.number_input("💰 Price", min_value=0.0)
            stock = st.number_input("📦 Stock Quantity", min_value=0, step=1)
            reorder_level = st.number_input("🔔 Reorder Level", min_value=0, step=1)

            sup_name = get_sup()
            supplier_id = st.selectbox(
                "🏭 Supplier",
                options=sup_name['supplier_id'],
                format_func=lambda x: sup_name.loc[
                    sup_name['supplier_id'] == x, 'supplier_name'
                ].values[0]
            )

            submit1 = st.form_submit_button("✅ Add Product")

            if submit1:
                try:
                    call_sp(product_name, category, price, stock, reorder_level, supplier_id)
                    st.success("🎉 Product added successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to add product: {e}")

    # -------------------------------- PRODUCT HISTORY --------------------------------

    elif option_1 == '📜 Product History':
        st.markdown("### 📜 Product Inventory History")

        with st.form('Product History Form'):
            products_df = get_products()
            option_selected = st.selectbox(
                "📦 Choose Product",
                options=products_df['product_id'],
                format_func=lambda x: products_df.loc[
                    products_df['product_id'] == x, 'product_name'
                ].values[0]
            )

            submit2 = st.form_submit_button("🔍 Get History")

            if submit2:
                history = get_prod_hist(option_selected)
                st.dataframe(history, use_container_width=True)

    # -------------------------------- PLACE REORDER --------------------------------

    elif option_1 == '🔄 Place Reorder':
        st.markdown("### 🔄 Place Product Reorder")

        with st.form('Place Reorder Form'):
            prod_namee = get_products()
            prod_id = st.selectbox(
                "📦 Choose Product",
                options=prod_namee['product_id'],
                format_func=lambda x: prod_namee.loc[
                    prod_namee['product_id'] == x, 'product_name'
                ].values[0]
            )

            prod_quant = st.number_input("📦 Reorder Quantity", min_value=1, step=1)

            submit3 = st.form_submit_button("🚚 Place Reorder")

            if submit3:
                try:
                    reorder(prod_id, prod_quant)
                    st.success("✅ Reorder placed successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to reorder product: {e}")
