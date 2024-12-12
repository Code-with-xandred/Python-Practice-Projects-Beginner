# 3.Temperature Conversion Program

unit = input("Is This Temperature In Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter The Temperature: "))

if unit == "C":
    temp = round(( 9 * temp) / 5 + 32, 1)
    # The Shortcut for This "°" Sign Is: Alt + 0176 
    print(f"The Temperature In Fahrenheit Is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature In Celcius Is: {temp}°C")
else:
    print(f"{unit} Is An Invalid Unit Of Mesurement")