def check_status(code: int):
    match code:
        case 200:
            print("Success")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Status Code")

check_status(200)
check_status(404)
check_status(123)  # Unknown Status Code

# Example with multiple cases

def day_type(day: str):
    match day.lower():
        case "saturday" | "sunday":
            print("It's a weekend!")
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("It's a weekday!")
        case _:
            print("Invalid day!")

day_type("Sunday")
day_type("Wednesday")
day_type("Holiday")  # Invalid day!

# Example with tuples

def get_shape(sides: int):
    match sides:
        case 3:
            print("Triangle")
        case 4:
            print("Quadrilateral")
        case 5:
            print("Pentagon")
        case _:
            print("Shape not recognized")

get_shape(3)
get_shape(4)
get_shape(7)  # Shape not recognized
