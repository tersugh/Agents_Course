chai_order = dict(type= "Masala Chai", size = "Large", sugar = 2 ),
print(f"Chai Order: {chai_order}")
chai_recipe = {}
chai_recipe ["base"] = "black tea"
chai_recipe ["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe ["liquid"]
print(f"Recipe: {chai_recipe}")
print(f"is sugar in the order? { "sugar" in chai_recipe}")
chai_order = {"type": "ginger chai", "size": "Medium", "sugar": 2  }
#print(f"Order Details (keys) : {chai_order.keys()}")
#print(f"Order Details (values) : {chai_order.values()}")
#print(f"Order Details (items) : {chai_order.items()}")
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")