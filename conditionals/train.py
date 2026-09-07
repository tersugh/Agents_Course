seat_type = input("Enter seat type Basic/AC/general/luxirious: ").lower()

match seat_type:
    case "basic":
        print(f"Basic seats")
    case "AC":
        print(f"Air Conditioned seats")
    case "general":
        print(f"General Seats")
    case "luxirious":
        print(f"Luxury Suites")
    case _:
        print(f"Invalid Seat")
        

