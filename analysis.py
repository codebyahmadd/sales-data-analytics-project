import pandas as pd
import matplotlib.pyplot as plt

# CSV file read karo
df = pd.read_csv("sales_data.csv")

# Total sales calculate karo
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Total sales
total_sales = df["Total_Sales"].sum()

# Top 3 products
top_products = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

# Best category
best_category = df.groupby("Category")["Total_Sales"].sum().idxmax()

# Terminal output
print("===== SALES REPORT =====")
print(f"Total Sales: {total_sales}")
print(f"Best Category: {best_category}")

print("\nTop 3 Products:")
print(top_products)

# Category-wise sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

# Bar chart
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.show()

# Pie chart
plt.figure(figsize=(6, 6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales Distribution")
plt.savefig("pie_chart.png")
plt.show()

# Excel report
df.to_excel("sales_report.xlsx", index=False)

print("\nFiles saved successfully!")
df.to_excel("sales_report.xlsx", index=False)
