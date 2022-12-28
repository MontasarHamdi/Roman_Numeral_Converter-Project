# ===== pseudo code =====
# Find the largest number from the list that is less than or equal to x.
# Write down the roman numeral representation of this number and subtract its value from x.
# Repeat steps 1-2 until you are left with 0.


def roman_num_convert(x):
    numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # Each time loop runs we want to look for largest number than is less than or equal to x.
    # Largest number in list is 1000 which is the 12th index.
    i = 12
    roman_conversion = ''  # variable to hold answer with empty string

    while x != 0:  # while loop if not 0 so loop will end once the remainder is 0
        if numbers[i] <= x:  # i represents 1000
            roman_conversion += roman_numerals[i]  # i in both lists represent the same value
            x = x - numbers[i]
        else:  # if i is not smaller or equal to x, move down the list by -1
            i = i - 1
    return roman_conversion


while __name__ == "__main__":
    user_input = int(input("Please enter number for conversion or 0 to exit: "))
    if user_input != 0:
        print(f"The integer {user_input}, converted to roman numerals is: {roman_num_convert(user_input)}")
    elif user_input == 0:
        print("Thank you for using Roman Numeral Converter. Goodbye!")
        exit()
