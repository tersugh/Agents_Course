Order_amount = int(input("Enter Order Amount: "))
delivery_fees = 0 if Order_amount > 300 else 30
print(f"delivery fee is: {delivery_fees}")
