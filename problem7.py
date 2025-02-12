import pandas as pd 

sales_data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Headphones', 'Smartphone', 'Laptop', 'Tablet'],
    'Quantity': [15, 20, 7, 5, 30, 15, 10, 25],
    'Price': [500, 300, 200, 150, 50, 300, 500, 200],
    'Date': ['2023-01-15', '2023-02-10', '2023-03-12', '2023-04-20', '2023-05-10', '2023-06-05', '2023-07-07', '2023-08-14']
}

df = pd.DataFrame(sales_data)

df['Total Sales'] = df['Quantity']* df['Price']

total_sales_per_product = df.groupby('Product')['Total Sales'].sum()

max_sales_product = total_sales_per_product.idxmax()
max_sales_value = total_sales_per_product.max()

filtered_data = df[df['Quantity'] > 10]

print("Updated DataFrame with 'Total Sales' Column:\n", df)
print("\nTotal Sales for Each Product:\n", total_sales_per_product)
print(f"\nProduct with highest total sales: {max_sales_product}, Total Sales:{max_sales_value}")
print("\nFiltered Data (Quantity > 10):\n", filtered_data)
