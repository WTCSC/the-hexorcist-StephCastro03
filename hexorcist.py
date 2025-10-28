def to_decimal(number_string, original_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number_string = number_string.upper()
    total_value = 0 
    power = 0

    for char in number_string[::-1]:
        if char not in digits[:original_base]:
            print(f"Invalid digit '{char}' for base {original_base}.")
            return None
        char_value = digits.index(char)
        total_value += char_value * (original_base ** power)
        power += 1

    return total_value

def from_decimal(decimal_number, target_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if decimal_number == 0:
        return "0"
    
    result_string = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number = decimal_number // target_base
        char_to_add = digits[remainder]
        result_string = char_to_add + result_string
    return result_string

def main():
    print("Welcome to the Hexorcist!")

    number_string = input("Enter the number you want to convert: ").strip()
    original_base = int(input("Enter the number's current base: "))
    target_base = int(input("Enter the new base you want: "))

    decimal_value = to_decimal(number_string, original_base)
    if decimal_value is None:
        return
    
    converted_value = from_decimal(decimal_value, target_base)

    print(f"'{number_string}' (Base-{original_base}) is '{converted_value}' (Base-{target_base}).")

if __name__ == "__main__":
    main()