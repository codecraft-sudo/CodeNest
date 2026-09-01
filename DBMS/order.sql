CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Customer_ID INT,
    Order_Date DATE,
    Product_Name VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Total_Amount DECIMAL(10,2),
    Payment_Method VARCHAR(30),
    Order_Status VARCHAR(30),
    Shipping_Address VARCHAR(150)
);