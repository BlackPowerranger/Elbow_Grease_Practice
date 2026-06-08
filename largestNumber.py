#function to check for the largest number
def find_max(*numbers):
    if len(numbers) == 0:
        return None

    largest_num = numbers[0]
    for num in numbers:
        if num > largest_num:
            largest_num = num
    return largest_num

#asks user for input as string separated by spaces
raw_input= input("Enter your numbers: ")

#splits the input into separate numbers, depending on where the spaces are
raw_numbers= raw_input.split()

#converts the string inputs to float
numbers = [float(num) for num in raw_numbers]

#calls function to print out the largest number
print(find_max(*numbers))
