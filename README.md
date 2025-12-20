![Project Snapshot](https://github.com/Coolbuddy145/Advanced-SQL-and-Python-UI/blob/40099519a031ee674967ab9fd4c90afac34de6d2/snapshot.png)

# 📦 Inventory & Supply Chain Management Dashboard

A **production-style full-stack inventory management system** built using **Python, Advanced SQL, Streamlit, and MySQL**, where complex database operations are seamlessly executed through an intuitive UI.

🔗 **Live App:** *https://coolbuddy145-advanced-sql-and-python-ui-app-jffegv.streamlit.app/*  
🗄️ **Database:** MySQL (Hosted on Railway)

---

## 🚀 Overview

This project allows users to manage inventory, suppliers, and reorders **without writing SQL**, while internally leveraging **advanced database logic** such as stored procedures, complex joins, aggregations, and transactional operations.

The UI abstracts database complexity, making the system usable even by non-technical users.

---

## ✨ Key Highlights

- 🔗 **Tightly Integrated UI & Database**  
  Perform real database operations directly from the UI — no SQL knowledge required.

- 🧠 **Advanced SQL Implementation**  
  Stored procedures, complex joins, subqueries, aggregations, and parameterized queries.

- ☁️ **Cloud-Deployed Architecture**  
  MySQL hosted on **Railway**, UI deployed on **Streamlit Cloud**, securely connected via environment secrets.

- 🔐 **Production-Grade Security**  
  No credentials in code or GitHub. All secrets managed via Streamlit Secrets.

---

## 🧩 Features

### 📊 Dashboard Metrics
- Total suppliers, products, categories  
- Sales & restock value (last 10 months)  
- Low-stock alerts (no active reorder)

### ⚙️ Operational Capabilities
- ➕ Add new products (via stored procedure)  
- 📜 View complete product inventory history  
- 🔄 Place product reorders  
- Real-time database updates reflected in UI  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Database | MySQL |
| DB Access | SQLAlchemy |
| Cloud DB | Railway |
| Hosting | Streamlit Cloud |

---

## 🧠 Architecture

---

## 📁 Project Structure

├── app.py # Streamlit UI

├── db_queries.py # SQL & DB logic

├── SQL Queries.sql # Schema & stored procedures

├── requirements.txt

└── README.md


---

## 🎯 Why This Project Matters

This project mirrors **real-world internal business tools**, demonstrating:
- End-to-end UI–database integration  
- Advanced SQL usage in production scenarios  
- Secure cloud deployment practices  
- Clean separation of UI, logic, and data layers  

It showcases skills in **data engineering, backend development, SQL optimization, and cloud deployment**.

---

## 👤 Author

**Zaid Khan**  




