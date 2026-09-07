masala_spices = ("pepper", "maggi", "ginger")
(spice1, spice2, spice3) = masala_spices
print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")
ginger_ratio, cadramom_ratio = 2,1
print(f"Ratio is G {ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is C {ginger_ratio} and G: {cadramom_ratio}")

#membership

print(f"is Ginger in Masala Spices ? {'ginger' in masala_spices}")
print(f"is Curry in Masala Spices?  {'curry' in masala_spices}")