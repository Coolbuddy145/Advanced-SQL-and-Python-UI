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


def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM products"))
        return [dict(row._mapping) for row in result.fetchall()]
    


import streamlit as st
st.dataframe(get_users())