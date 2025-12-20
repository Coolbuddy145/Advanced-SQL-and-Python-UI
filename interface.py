import streamlit as st
import pandas as pd
from db_queries import total_supplier,total_products,total_categories,total_sales,total_restock,low_stock,supplier_details,product_suppliers,products_reorder,sql,get_products,get_prod_hist,get_cat,get_sup,call_sp

# ----------------------------------------------------- Header ----------------------------------------------------------

st.sidebar.title('Inventory Management Dashboard')
option=st.sidebar.radio('Select Option',['Basic Operation','Operational Tasks'])

# ------------------------------------------------- Basic Information Page -----------------------------------------
if option=='Basic Operation':
    st.title('Inventory and Supply Chain Management')
    st.header('Basic Metrics')
    
    col1,col2,col3=st.columns(3)
# creating KPI metric grid
    with col1:
        st.metric(label='Total Suppliers',value=total_supplier())
    with col2:
        st.metric(label='Total products',value=total_products())
    with col3:
        st.metric(label='Total Categories',value=total_categories())

# creating col 4 to 6
    col4,col5,col6=st.columns(3)

    with col4:
        st.metric(label='Total Sale Value(Last 10 Months)',value=total_sales())
    with col5:
        st.metric(label='Total Restock value(Last 10 months)',value=total_restock())
    with col6:
        st.metric(label='Low Stock Quantity & no Restock order is placed',value=low_stock())

    st.header('Suppliers Contact Details')
    st.dataframe(supplier_details())
    st.header('Products with Supplier and Stock')
    st.dataframe(product_suppliers())
    st.header('Products Needing Reorder')
    st.dataframe(products_reorder())

# ------------------------------------------------- Operational Task Page -----------------------------------------

elif option=='Operational Tasks':
    st.title('Inventory and Supply Chain Management')
    st.header('Operational Tasks')
    option_1=st.selectbox('Choose a Task',['Add a New Product','Product History','Place Reorder','Recieve Order'])

    # creating functions for each operation

    if option_1=='Add a New Product':
        st.header('Add Product')
        with st.form('Add New Product'):
            product_name=st.text_input('Enter Product Name')
            category=st.selectbox('Category',options=get_cat())
            price=st.number_input('Price',min_value=0.0)
            stock=st.number_input('Stock Quantity',min_value=0,step=1)
            reorder_level=st.number_input('Reorder Level',min_value=0,step=1)
            sup_name=get_sup()
            supplier_id=st.selectbox('Supplier',options=sup_name['supplier_id'],format_func=lambda x:sup_name.loc[sup_name['supplier_id']==x,'supplier_name'].values[0])
            submit1=st.form_submit_button('Add Product')
            if submit1:
                try:
                    call_sp(product_name,category,price,stock,reorder_level,supplier_id)
                    st.success("✅ Product added successfully")
                except Exception as e:
                    st.error(f"❌ Failed to add product: {e}")


    elif option_1=='Product History':
        st.header('Product Inventory History')
        with st.form('form2'):
            products_df=get_products()
            option_selected=st.selectbox("Choose a Product",options=products_df['product_id'],format_func=lambda x:products_df.loc[products_df['product_id']==x,'product_name'].values[0])
            submit2=st.form_submit_button('Get Details')
            if submit2:
                history=get_prod_hist(option_selected)
                st.dataframe(history)
            

    elif option_1=='Place Reorder':
        st.header('Place Reorder')
        with st.form('form3'):
            prod_name3=st.text_input('Choose Product Name')
            prod_quant=st.number_input('Enter Quantity')
            submit3=st.form_submit_button('Place Reorder')

    elif option_1=='Recieve Order':
        pass

            


