"""AGE CALCULATOR THINGY"""

#asks for date of birth and converts to int
birth_date= int(input("Enter your birth year: "))

#asks for  year and converts to int
year= int(input("Enter the year: "))

#check if year is valid
def check_year_validity():
    #checking to see whether inputs are valid years
    if year>9999 or birth_date>9999:
        print("Please input valid year. Try again")
        return False

    elif year<=0 or birth_date<=0:
        print("Please input valid year. Try again")
        return False

    elif year<birth_date:
        print("You're not born yet...")
        return False

    else:
        print("Thank you...")
        return True

#calculating the age and outputting it
if check_year_validity():
    age=year-birth_date
    print(f"You are {age} years old")
else:
    print("Check if either birth date or year is valid and try again")




