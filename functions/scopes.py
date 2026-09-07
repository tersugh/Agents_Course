def serve_chai():
    chai_type = "Masala" #local scope
    print(f"Inside Life {chai_type}")

chai_type = "Lemon"
serve_chai()    
print(f"Outside Function {chai_type}")



def chai_counter():
    chai_order = "Lemon" #Enclosing Scope

    def print_order():
        chai_order = "Ginger"
        print(f"Inner Function", chai_order)
        print_order()
        print("Outer", chai_order)

chai_order = "Tulsi" # Global
chai_counter()
print("global:", chai_order )