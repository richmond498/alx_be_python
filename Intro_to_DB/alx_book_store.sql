CREAT TABLE Books (
    book_id(Primary key)
    title VARCHAR(130)
    author_id (Foreign Key)
    price DOUBLE
    publication_date DATE

)

CREAT TABLE Authors (
    author_id(Primary Key)
    author_name VARCHAR(215)
)

CREAT TABLE Customers (
    Customer_id (Primary Key)
    customer_name VARCHAR(215)
    email VARCHAR(215)
    address TEXT

)

CREAT TABLE Orders (
    order_id (Primary Key)
    customer_id (Foreign Key)
    order_date DATE

)

CREAT TABLE Order_Details (
    orderdetailid (Primary Key)
    order_id (Foreign Key)
    book_id (Foreign Key)
    quantity DOUBLE
)