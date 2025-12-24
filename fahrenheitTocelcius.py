#function to convert fahrenheit to celcius
def fahrenheit_to_celcius(fahrenheit):
    celcius=(fahrenheit - 32) * 5.0/9.0
    return celcius
    
#function to convert celcius to fahrenheit
def celcius_to_fahrenheit(celcius):
    fahrenheit=(celcius*1.8) + 32
    return fahrenheit

#asking conversion type, either from fahrenheit to celcius or vice versia
choice=int(input("Choose: 1.Fahrenheit to Celcius or 2.Celcius to Fahrenheit: "))

if choice==1:
    fahrenheit = float(input("Enter fahrenheit temperature: "))
    print(f"Temperature in celcius:{fahrenheit_to_celcius(fahrenheit)}")
    
elif choice==2:
    celcius = float(input("Enter celcius temperature: "))
     print(f"Temperature in fahrenheit:{celcius_to_fahrenheit(celcius)}")
else:
    print ("invalid choice, try again.")
