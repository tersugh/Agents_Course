ingredients = ["water", "Milk", "Sugar", "Lipton"]
ingredients.append("Bread")
print(f"ingredients are {ingredients}")
ingredients.remove("water")
print(f"ingredients are {ingredients}")
spice_options = ["ginger", "cardamom", "fish"]
chai_ingredients = ["water", "bread"]
chai_ingredients.extend(spice_options)
print(f"chai : {chai_ingredients}")
chai_ingredients.insert(0,"lemon")
print(f"chai : {chai_ingredients}")
last_added = chai_ingredients.pop()
print(f"{last_added}")
chai_ingredients.reverse()
chai_ingredients.sort()
print(f"chai : {chai_ingredients}")
sugar_levels = [1,2,3,4,5,6,7,8,9]
print(f"Maximum Sugar Level: {max(sugar_levels)}")
print(f"Minimum Sugar Level: {min(sugar_levels)}")