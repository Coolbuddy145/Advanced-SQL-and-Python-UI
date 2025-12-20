import pandas as pd
import streamlit as st
# from sqlalchemy import create_engine,text

# creating db engine
# from sqlalchemy import create_engine, text
# from urllib.parse import quote_plus

# password = quote_plus("Pikachu@123")

# engine = create_engine(
#     f"mysql+pymysql://root:{password}@localhost:3306/sql_db",
#     echo=True
# )

import os
from sqlalchemy import create_engine, text

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    future=True,
    pool_pre_ping=True
)



# with engine.connect() as conn:
#     conn.execute(text("SELECT 1"))
#     print("✅ Connected successfully")

# helper function created
def sql(query, params=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), params or {})
        return pd.DataFrame(result.mappings().all())

# creating functions for each metric

def total_supplier():
    query1="SELECT COUNT(DISTINCT supplier_name) AS Toal_Supplier FROM suppliers"
    df1= pd.read_sql(query1,engine)
    return int(df1.iloc[0][0])


def total_products():
    query2="SELECT COUNT(DISTINCT product_name) AS Total_products FROM products"
    df2=pd.read_sql(query2,engine)
    return int(df2['Total_products'].iloc[0])

def total_categories():
    query3="SELECT COUNT(DISTINCT category) AS toal_categories FROM products"
    df3=pd.read_sql(query3,engine)
    return int(df3['toal_categories'].iloc[0])


def total_sales():
    query3="""SELECT ROUND(SUM(p.price*abs(s.change_quantity)),2) AS total_sales
    FROM products as p
    INNER JOIN stock as s
    ON p.product_id=s.product_id
    WHERE entry_date>=(SELECT DATE_SUB(MAX(entry_date),interval 10 month) from stock) and change_type='Sale'"""
    df3=pd.read_sql(query3,engine)
    return int(df3['total_sales'].iloc[0])

def total_restock():
    query3="""SELECT ROUND(SUM(p.price*abs(s.change_quantity)),2) AS total_restock
    FROM products as p
    INNER JOIN stock as s
    ON p.product_id=s.product_id
    WHERE entry_date>=(SELECT DATE_SUB(MAX(entry_date),interval 10 month) from stock) and change_type='Restock'"""
    df3=pd.read_sql(query3,engine)
    return int(df3['total_restock'].iloc[0])

def low_stock():
    query="""SELECT COUNT(DISTINCT p.product_id) as count_
    FROM products as p
    LEFT JOIN reorders as r
    ON p.product_id=r.product_id
    WHERE p.stock_quantity<p.reorder_level AND r.product_id IS NULL"""
    df=pd.read_sql(query,engine)
    return int(df['count_'].iloc[0])

def supplier_details():
    query="SELECT supplier_name,contact_name,email,phone FROM suppliers"
    return pd.read_sql(query,engine)

def product_suppliers():
    query="""SELECT p.product_name,s.supplier_name,p.stock_quantity,p.reorder_level
        FROM products as p
        INNER JOIN suppliers as s
        ON p.supplier_id=s.supplier_id"""
    return pd.read_sql(query,engine)

def products_reorder():
    query="""SELECT product_name,stock_quantity,reorder_level
        FROM products 
        WHERE stock_quantity<reorder_level
    """
    return pd.read_sql(query,engine)

def get_products():
    return sql("""SELECT product_id,product_name FROM products ORDER BY product_name""")

# def product_selector(get_products):
#     option_selected=st.selectbox("Choose a Product",options=get_products['product_id'],format_func=lambda x:get_products.loc[get_products['product_id']==x,'product_name'].values[0])
#     return option_selected
def get_prod_hist(option_selected):
    return sql("""SELECT p.product_name,s.change_quantity,s.change_type,s.entry_date
                FROM products as p
                INNER JOIN stock as s
                ON p.product_id=s.product_id
                WHERE p.product_id= :pid
                ORDER BY s.entry_date DESC""",{'pid':option_selected})

def get_cat():
    return sql("SELECT DISTINCT category FROM products")

def get_sup():
    return sql("SELECT supplier_id,supplier_name FROM suppliers")

def call_sp(product_name,category,price,stock,reorder_level,supplier_id):
    query=text("""CALL prod_add(:p_name,:p_category,:p_price,:p_stock,:p_reorder,:p_supplier)""")
    # here we have to pass values using place holder in stored procedure such as using :p_name and then the value gets passed in it.
    para={'p_name':product_name,
          'p_category':category,
          'p_price':price,
          'p_stock':stock,
          'p_reorder':reorder_level,
          'p_supplier':supplier_id}
    
    with engine.begin() as conn:
        conn.execute(query,para)

def reorder(product_id,quantity):
    query=text("""INSERT INTO reorders(reorder_id,product_id,reorder_quantity,reorder_date,status)
            SELECT MAX(reorder_id)+1,:pid,:qty,CURDATE(),"Ordered" FROM reorders""")
    para={'pid':product_id,
          'qty':quantity}
    
    with engine.begin() as conn:
        conn.execute(query,para)