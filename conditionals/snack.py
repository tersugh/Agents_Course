snack_order = input("Enter your order: ").lower()
#print(f"{snack_order}")
if snack_order == "cookies" or snack_order == "samosa" :
    print(f"Great Choice! Order on its way! {snack_order} about to be served!" )
else:
    print(f"Sorry your order {snack_order} is not Available at this time.")     