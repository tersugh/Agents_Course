essential_spices = {"curry", "egusi", "pepper", "salt", "ginger" }
optional_spices = {"fish", "oil", "peris", "tatashe", "ginger"}
all_spices = essential_spices | optional_spices
print (f"All Spices: {all_spices}")
common_spices = essential_spices & optional_spices
print (f"Common Spices: {common_spices}")
only_in_essential = essential_spices - optional_spices
print(f"Only Essential Spices : {only_in_essential}")
print(f"Is 'Rice' in in essential spices? {'Rice' in essential_spices}")

