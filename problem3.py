import itertools
import csv

fruits = ['apple', 'banana', 'mango']  
weights = [1, 2, 3]  
prices = [100, 200]  
regions = ['North', 'South']  

combinations = list(itertools.product(fruits, weights, prices, regions))

csv_filename = "fruit_combination.csv"
with open(csv_filename, mode = "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Fruit", "Weight (kg)", "Price per kg", "Region"])
    writer.writerows(combinations)

total_rows = len(combinations)
print(f"Total rows in csv file: {total_rows}")