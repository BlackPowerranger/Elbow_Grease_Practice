#function to arrange the names in order from youngest to oldest
def my_function(*kids):
    reversed_kids= kids[::-1]
    print (f"The order from youngest to oldest is: {reversed_kids}")

#asks for names from oldest to youngest
raw_input= input("Enter names from oldest to youngest: ")

#seperates the names depending on spacing
raw_names=raw_input.split()


#checks if names entered are valid
try:
    for name in raw_names:
        if not name.isalpha():
            raise ValueError
    my_function(*raw_names)
except ValueError:
    print("Invalid input. Please enter names using letters only.")

