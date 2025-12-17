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