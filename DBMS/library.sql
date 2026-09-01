CREATE TABLE Library (
    Book_ID INT PRIMARY KEY,
    Book_Name VARCHAR(100),
    Author VARCHAR(100),
    Publisher VARCHAR(100),
    ISBN VARCHAR(20),
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    Quantity INT,
    Edition VARCHAR(20),
    Publication_Year INT
);
