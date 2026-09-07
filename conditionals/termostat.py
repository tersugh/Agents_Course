device_status = "active"
temperature = int(input("Input temperature here:"))
if device_status == "active":
    print(f"The device is active!")

if temperature >= 35:
   print(f"Warning Temperature too high ")
elif temperature <= 34:
    print(f"Temperature Normal")
    if device_status == "off":
        print(f"Device is offline")





