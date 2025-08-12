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



