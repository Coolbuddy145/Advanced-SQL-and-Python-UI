import streamlit as st
import pandas as pd

st.sidebar.title('Inventory Management Dashboard')
option=st.sidebar.radio('Select Option',['Basic Operation','Operational Tasks'])

# ------------------------------------------------- Basic Information Page -----------------------------------------
if option=='Basic Operation':
    st.title('Inventory and Supply Chain Management')
    st.header('Basic Metrics')
    
    col1,col2,col3=st.columns(3)
# creating KPI metric grid
    with col1:
        st.metric(label='Total Suppliers',value='--')
    with col2:
        st.metric(label='Total products',value='--')
    with col3:
        st.metric(label='Total Categories',value='--')

# creating col 4 to 6
    col4,col5,col6=st.columns(3)

    with col4:
        st.metric(label='Total Sale Value(Last 3 Months)',value='--')
    with col5:
        st.metric(label='Total Restock value(Last 3 months)',value='--')
    with col6:
        st.metric(label='Below Reorder and no pending Reorders',value='--')

    st.header('Suppliers Contact Details')
    # code
    st.header('Products with Supplier and Stock')
    # code
    st.header('Products Needing Reorder')

# ------------------------------------------------- Operational Task Page -----------------------------------------

elif option=='Operational Tasks':
    st.title('Inventory and Supply Chain Management')
    st.header('Operational Tasks')
    option_1=st.selectbox('Choose a Task',['Add a New Product','Product History','Place Reorder','Recieve Order'])

    # creating functions for each operation

    if option_1=='Add a New Product':
        st.header('form1')
        with st.form('Add New Product'):
            prod_name=st.text_input('Enter Product Name')
            prod_category=st.text_input('Enter Product Category')
            prod_price=st.text_input('Price')
            prod_stock=st.text_input('Stock Quantity')
            reorder_level=st.text_input('Reorder Level')
            prod_supplier=st.text_input('Supplier')

            submit1=st.form_submit_button('Add Product')

    elif option_1=='Product History':
        st.header('Product Inventory History')
        with st.form('form2'):
            prod_name2=st.text_input('Choose Product Name')
            submit2=st.form_submit_button('Get Details')

    elif option_1=='Place Reorder':
        st.header('Place Reorder')
        with st.form('form3'):
            prod_name3=st.text_input('Choose Product Name')
            prod_quant=st.number_input('Enter Quantity')
            submit3=st.form_submit_button('Place Reorder')

    elif option_1=='Recieve Order':
        pass

            


