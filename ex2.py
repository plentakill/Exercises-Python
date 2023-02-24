#EX2.1
def print_with_numbers(glass_of_water):
    print('something')
    return print("I drank", glass_of_water, "glasses of water today.")

print_with_numbers(glass_of_water=3)


#EX2.2
glass_of_water=3
print("I drank", glass_of_water, "glasses of water today.")
print(type(glass_of_water))

#EX2.3
def check_is_digit(input_str):
    if input_str.strip().isdigit():
        print("User input is Number")
    else:
        print("User input is string")

num1 = input("Enter number and hit enter")
check_is_digit(num1)


#Alternate EX2.3
print("Enter your input: ")
input_str = input()

# Split the input into a list of words
words = input_str.split()

# Loop through the words and determine their type
for word in words:
    if word.isnumeric():
        print(word, "is a number")
    elif word.isalpha():
        print(word, "is a string")
    else:
        print(word, "is an unknown type")
