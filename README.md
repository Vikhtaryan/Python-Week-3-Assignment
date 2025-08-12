"""
Discount Calculator

A simple Python program to calculate the final price after applying a discount.
The discount is applied only if it is 20% or higher.

Usage:
- Run this script.
- Enter the original price and discount percentage when prompted.

Example:
Enter the original price of the item: 100
Enter the discount percentage: 25
Discount applied. The final price is: 75.00
"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount)

if final_price == price:
    print(f"No discount applied. The price remains: {final_price:.2f}")
else:
    print(f"Discount applied. The final price is: {final_price:.2f}")
