# 📦 Inventory & Supply Chain Management Dashboard

A full-stack **Inventory and Supply Chain Management system** built using **Python, Advanced SQL, Streamlit, and MySQL**, where complex database operations are seamlessly abstracted behind an intuitive UI.

🔗 **Live App:** *(Add your Streamlit Cloud link here)*  
🗄️ **Database:** MySQL (Hosted on Railway)

---

## 🚀 Project Overview

This project demonstrates how a **non-technical user** can perform **complex database operations**—such as adding products, tracking inventory history, and placing reorders—**without writing a single SQL query**, all through a clean and interactive web interface.

Behind the scenes, the system uses:
- Advanced SQL queries
- Stored Procedures
- Transactional database logic
- Secure cloud deployment

---

## ✨ Key Highlights

### 🔹 Fully Integrated UI & Database
- Users can **add products**, **view inventory history**, and **place reorders** directly from the UI  
- No SQL knowledge required to operate the system  
- UI actions are mapped to real database transactions  

### 🔹 Advanced SQL Usage
- Stored Procedures for atomic operations (e.g. product creation)
- Complex joins, aggregations, and subqueries
- Inventory stock derived from transaction history
- Parameterized queries to prevent SQL injection

### 🔹 Cloud Deployment (Production-Style)
- **Database deployed on Railway (MySQL)**
- **Frontend deployed on Streamlit Cloud**
- Secure credential management using **Streamlit Secrets**
- No credentials hard-coded in the codebase

---

## 🧩 Features

### 📊 Business Metrics Dashboard
- Total Suppliers  
- Total Products  
- Total Categories  
- Sales & Restock Value (Last 10 Months)  
- Low Stock Alerts (No active reorder)  

### 🏭 Supplier & Inventory Views
- Supplier contact details  
- Products mapped with suppliers  
- Products below reorder level  

### ⚙️ Operational Capabilities
- ➕ Add new products (via Stored Procedure)  
- 📜 View complete product inventory history  
- 🔄 Place product reorders  
- Real-time database updates reflected in UI  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Database | MySQL |
| ORM / DB Access | SQLAlchemy |
| Cloud DB Hosting | Railway |
| App Hosting | Streamlit Cloud |
| Security | Environment Variables & Secrets |

---

## 🗂️ Project Structure

