from datetime import datetime

current_date_time = datetime.now()
day_of_week = current_date_time.weekday()

subtotal = float(input("Please enter the subtotal: "))

total_with_discount = subtotal - subtotal*.10
discount_amount = subtotal - total_with_discount


if day_of_week == (1 or 2)  and subtotal >= 50:
    print(f"Discount Amount: {discount_amount}")

sales_tax = subtotal*0.06
total = subtotal + sales_tax - discount_amount

print(f"Sales tax amount: {sales_tax}")
print(f"Total: {total}")
