import sys

def fahrenheit(celsius: float) -> float :
    return celsius * 1.8 + 32.0

def celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) / 1.8

def main():
    print("This program converts temperatures.")
    print("1 - celsius to fahrenheit")
    print("2 - fahrenheit to celsius")
    print("0 - quit")

    choice = input("Enter your choice: ")

    if choice == "0":
        sys.exit(0)

    if choice not in ("1", "2"):
        print("Invalid choice.")
        sys.exit(1)


    try:
        value = float(input("Введи значення температури:"))
    except ValueError:
        print("Invalid input. Please enter a numeric value (e.g., 36.6).")
        sys.exit(1)



    if choice == "1":
        print(f"tempeture in fahrenheit: {fahrenheit(value):.2f} °F")

    if choice == "2":
        print(f"tempeture in celsius: {celsius(value):.2f} °C")



if __name__ == "__main__":
    main()