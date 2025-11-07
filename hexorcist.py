"""
This program converts numbers from on base to another base. 
It starts by turning the number into base 10, then into the new base that that user wants.
This two step method allows us to avoid any confusing math anf keeps the logic of it simple.
"""

# I made the string uppercase so that it woud be easier to match letters.
# Since bases such as 16 use letters A-F, so this keeps things consistent.
def to_decimal(number_string, original_base):

    """
    I choose to convert everything to base 10 first because it is a universally used base.
    Once we have the base 10 value, converting to any other base is straightforward instead of trying to convert directly.
    """

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0 
    power = 0

# I reverse the string to make it easier to calculate the value based on position.
# Starting from the right makes calculating powers of the base a lot simpler.
    for char in number_string[::-1]:
        # Allow a easy way to check if the digit actually exists in the base.
        # This also prevents bad inputs from causing errors later on.
        if char not in digits[:original_base]:
            print(f"Invalid digit '{char}' for base {original_base}.")
            return None
        char_value = digits.index(char)
        # This mirros how normal base 10 works but for an base.
        # This is multiplying the digit value by the base raised to apple the place value.
        total_value += char_value * (original_base ** power)
        power += 1

    return total_value

def from_decimal(decimal_number, target_base):

    """
    This function uses repeated division because it is the most reliable in order to break down decimal numbers down into a digits for any base.
    """

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Made sure to handle tneh zero right away to avoid having to run the while loop unnecessarily.
    if decimal_number == 0:
        return "0"
    
    result_string = ""
  # We use division and remainders because each remainder
  # represents a single digit in the new base. Building the
  # result from right to left keeps it in the right order.
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = digits[remainder]
        # We add new digits to the front since the remainders come out in reverse.
        # Prepending keeps the number in the correct order.
        result_string = char_to_add + result_string
    return result_string

def main():

    """
    I made this part separate from the conversion functions so that the code would be easer to be tested.
    The logic allows it to flow and for everything to stay organized in its own place.
    """

    print("Welcome to the Hexorcist!")
# makes sure the users input stays inside conversion functions. This way they only focus on the math in the functions above. 
    number_string = input("Enter the number you want to convert: ").strip()
    original_base = int(input("Enter the number's current base: "))
    target_base = int(input("Enter the new base you want: "))
# Always convert to decimal first in order to avoid having to directly jump from base to base.
    decimal_value = to_decimal(number_string, original_base)
    # If the input was invalid, we stop the process here in order to avoid bad results or crashing.
    if decimal_value is None:
        return
    # Doing conversions in two parts makes sure it keeps each step clear and it is easy to debug.
    converted_value = from_decimal(decimal_value, target_base)

    print(f"'{number_string}' (Base-{original_base}) is '{converted_value}' (Base-{target_base}).")
# This check makes sure the main function only runs when the user run the file directly.
# This is useful if the user ever want to import this file into another one for testing
if __name__ == "__main__":
    main()