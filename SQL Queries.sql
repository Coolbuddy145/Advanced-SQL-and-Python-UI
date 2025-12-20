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

# Products Needing Reorder
SELECT product_name,stock_quantity,reorder_level
FROM products 
WHERE stock_quantity<reorder_level

# Product Inventory History
SELECT p.product_name,s.change_quantity,s.change_type,s.entry_date
FROM products as p
INNER JOIN stock as s
ON p.product_id=s.product_id
-- WHERE p.product_id= :pid
ORDER BY s.entry_date DESC

SELECT product_id,product_name FROM products ORDER BY product_name

# Add a Product in products table and update shipment and stock table also

DELIMITER $$
CREATE PROCEDURE prod_add(
IN p_name varchar(100),
IN p_category varchar(100),
IN p_price DECIMAL(10,2),
IN p_stock INT,
IN p_reorder INT,
IN p_supplier INT)
BEGIN 
	DECLARE new_prod_id INT;
    DECLARE new_ship_id INT;
    DECLARE new_entry_id INT;
    
    # make changes in product table
    # generating the new_prod_id
    SELECT IFNULL(MAX(product_id),0)+1 INTO new_prod_id FROM products;
    # inserting values in product table
    INSERT INTO products(product_id,product_name,category,price,stock_quantity,reorder_level,supplier_id)
    VALUES(new_prod_id,p_name,p_category,p_price,p_stock,p_reorder,p_supplier);
    
    # generating new_ship_id 
    SELECT IFNULL(MAX(shipment_id),0)+1 INTO new_ship_id FROM shipments;
    # inserting values into shipments table
    INSERT INTO shipments(shipment_id,product_id,supplier_id,quantity_received,shipment_date)
    VALUES(new_ship_id,new_prod_id,p_supplier,p_stock,CURDATE());
    
    # GENERATING new_entry_id
    SELECT IFNULL(MAX(entry_id),0)+1 INTO new_entry_id FROM stock;
    # inserting values into stock table
    INSERT INTO stock(entry_id,product_id,change_quantity,change_type,entry_date)
    VALUES(new_entry_id,new_prod_id,p_stock,"Restock",CURDATE());
END $$
DELIMITER ;

CALL prod_add("Phone Watch","Watch",250.00,300,150,9)
CALL prod_add(p_name,p_category,p_price,p_stock,p_reorder,p_supplier)
SELECT * FROM products WHERE product_name='Phone Watch'


# get categories
SELECT DISTINCT category FROM products

# supplier id and name
SELECT supplier_id,supplier_name FROM suppliers

SELECT * FROM products where product_name='Carrom Board'























































