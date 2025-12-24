def fahrenheit_to_celcius(fahrenheit):
    celcius=(fahrenheit - 32) * 5.0/9.0
    return celcius

fahrenheit = float(input("Enter fahrenheit temperature: "))

print(f"Temperature in celcius:{fahrenheit_to_celcius(fahrenheit)}")