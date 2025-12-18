import pandas as pd
import streamlit as st
from sqlalchemy import create_engine,text

# creating db engine
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

password = quote_plus("Pikachu@123")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/sql_db",
    echo=True
)

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
    print("✅ Connected successfully")


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
    WHERE P.stock_quantity<p.reorder_level AND r.product_id IS NULL"""
    df=pd.read_sql(query,engine)
    return int(df['count_'].iloc[0])
