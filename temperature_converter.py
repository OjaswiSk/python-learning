def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit -32) * 5/9
    return celsius

print("Temperature Converter")
while True:
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit or Q to quit.):").upper()
    if unit == "Q":
        print("Goodbye! 👋")
        break
    if unit not in ["C", "F"]:
        print("❌ Invalid unit! Please use C, F, or Q to quit.")
        continue
    

    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("❌ Invalid input! Please enter a numeric temperature.")
        continue


#temperature = float(input("Enter the temperature:"))

    if unit== "C":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}C is {result}F")
    elif unit== "F":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}F is {result}C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")