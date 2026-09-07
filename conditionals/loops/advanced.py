flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]
for flavor in flavours:
    if flavor == "Out of stock":
     continue
    if flavor == "Discontinued":
        print(f"{flavor} item found")
        break
   
print(f"Outside of loop")
