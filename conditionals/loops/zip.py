Names = ["John", "Excel", "Marmush", "Halaand"]
bills = [50, 100, 300, 450]


for name, amount in zip(Names, bills):
    print(f"{name} paid ${amount}")
    