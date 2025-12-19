USE sql_db;

SELECT * FROM products
SELECT * FROM suppliers
SELECT * FROM shipments
SELECT * FROM reorders
SELECT * FROM stock

# Total Supplier
SELECT COUNT(DISTINCT supplier_name) FROM suppliers

# Total Products
SELECT COUNT(DISTINCT product_name) FROM products

# Total Categories
SELECT COUNT(DISTINCT category) FROM products

-- Total sales made in last 10 months

SELECT ROUND(SUM(p.price*abs(s.change_quantity)),2) AS total_sales
FROM products as p
INNER JOIN stock as s
ON p.product_id=s.product_id
WHERE entry_date>=(SELECT DATE_SUB(MAX(entry_date),interval 10 month) from stock) and change_type='Sale'


-- Total restock value in last 10 months
SELECT ROUND(SUM(p.price*abs(s.change_quantity)),2) AS total_restock
FROM products as p
INNER JOIN stock as s
ON p.product_id=s.product_id
WHERE entry_date>=(SELECT DATE_SUB(MAX(entry_date),interval 10 month) from stock) and change_type='Restock'

-- Number of products which has low stock quantity and no restock order is placed
SELECT COUNT(DISTINCT p.product_id)
FROM products as p
LEFT JOIN reorders as r
ON p.product_id=r.product_id
WHERE P.stock_quantity<p.reorder_level AND r.product_id IS NULL

# Suppliers Contact Details
SELECT supplier_name,contact_name,email,phone FROM suppliers

# Products with Supplier and Current Stock
SELECT p.product_name,s.supplier_name,p.stock_quantity,p.reorder_level
FROM products as p
INNER JOIN suppliers as s
ON p.supplier_id=s.supplier_id

































































