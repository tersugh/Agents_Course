chai_type = "ginger_chai"
customer_name = "Priya"
print(f"Order for {customer_name}: {chai_type} please!")
chai_description = "Aromatic and Bold"
print(f"First Word:{chai_description [0:7] }")
print(f"First Word: {chai_description [:8]}")
print(f"Reverse Word: {chai_description [::-1]}")
print(f"Word Play: {chai_description [4:]}")
label_text = "Chai spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded Label: {label_text}")
print(f"Encoded Label: {encoded_label}")
#decoded_label = encoded_label.decode("utf-8")
#print(f"Decoded label : {decoded_label}")