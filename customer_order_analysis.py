import pandas as pd
import numpy as np 

# so that every time we run the code we get same random data
np.random.seed(2)

# creating fake order dataset
Data = {
    # creating order ids from 2001 to 2030
    "Order_Id": np.arange(2001, 2031),

    # randomly assigning customer names
    "Customer_Name": np.random.choice(
        ["Amit", "Riya", "Karan", "Neha", "Rahul", "Sneha"], 30
    ),

    # randomly assigning cities
    "City": np.random.choice(
        ["Dehli", "Haryana", "UP", "Mumbai", "MP", "Goa"], 30
    ),

    # randomly assigning products
    "Product": np.random.choice(
        ["Laptop", "Mobile", "Ear Phone", "Head Phone", "Mouse"], 30
    ),

    # random quantity between 1 and 5
    "Quantaity": np.random.randint(1, 6, 30),

    # random price between 5000 and 60000
    "Price_per_unit": np.random.randint(5000, 60000, 30)
}

# converting dictionary to dataframe
df = pd.DataFrame(Data)

# creating total amount column (quantity * price)
df["Total_Amount"] = df["Quantaity"] * df["Price_per_unit"]

# checking first 5 rows
print(df.head())


# checking dataset information (data types etc.)
print("\nThis is Info of Data")
print(df.info())

# getting statistical summary (mean, min, max etc.)
print("\nThis is Summary Statistical Description of Data")
print(df.describe())


# finding orders where total amount is greater than 100000
High_order = df[df["Total_Amount"] > 100000]

print("\nThese are high value orders")
print(High_order)


# orders where product is laptop and quantity is 2 or more
pro_lap = df[
    (df["Product"] == "Laptop") &
    (df["Quantaity"] >= 2)
]

print("\nLaptop orders with quantity >= 2")
print(pro_lap)


# calculating total revenue city-wise
Revenu_per_city = df.groupby("City")["Total_Amount"].sum()

print("\nTotal revenue per city")
print(Revenu_per_city)


# average price of each product
avg_pro = df.groupby("Product")["Price_per_unit"].mean()

print("\nAverage price per product")
print(avg_pro)


# total quantity sold for each product
Total_sold_pro = df.groupby("Product")["Quantaity"].sum()

print("\nTotal quantity sold per product")
print(Total_sold_pro)


# discount calculation
# 10% if amount > 150000
# 5% if between 80000 and 150000
conditions = [
    df["Total_Amount"] > 150000,
    (df["Total_Amount"] >= 80000) & (df["Total_Amount"] <= 150000)
]

choices = [
    df["Total_Amount"] * 0.10,
    df["Total_Amount"] * 0.05
]

# applying discount logic
df["Discount"] = np.select(conditions, choices, default=0)

print(df[["Total_Amount", "Discount"]])


# creating order category column
conditions1 = [
    df["Total_Amount"] < 50000,
    (df["Total_Amount"] >= 50000) & (df["Total_Amount"] < 120000),
    df["Total_Amount"] >= 120000
]

choices1 = ["Low Price", "Medium Price", "High Price"]

df["Order_Category"] = np.select(conditions1, choices1, default="Low Price")

print(df[["Total_Amount", "Order_Category"]].head())


# finding which city generated highest revenue
Revenu_High_city = df.groupby("City")["Total_Amount"].sum()

print("\nCity generating highest revenue")
print(Revenu_High_city.idxmax())


# finding most profitable product
most_profitable = df.groupby("Product")["Total_Amount"].sum()

print("\nProducts ranked by total revenue")
print(most_profitable.sort_values(ascending=False))


# checking which customer spent the most overall
Customer_spent = df.groupby("Customer_Name")["Total_Amount"].sum()

print("\nCustomer spending ranking")
print(Customer_spent.sort_values(ascending=False))
