def separate_and_convert(input_string):
    # Separate numbers and letters
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    print("Number String:", number_string)
    print("Letter String:", letter_string)

    # Convert even numbers to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values_numbers = [ord(chr(num)) for num in even_numbers]

    print("Even Numbers:", even_numbers)
    print("ASCII Code Decimal Values for Numbers:", ascii_values_numbers)

    # Convert upper-case letters to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_values_letters = [ord(char) for char in upper_case_letters]

    print("Upper-case Letters:", upper_case_letters)
    print("ASCII Code Decimal Values for Letters:", ascii_values_letters)

# Example Usage
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
separate_and_convert(input_string)

# part 2 -decrypt_cryptogram

def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_message = ""
    for char in cryptogram:
        if char.isalpha():
            ascii_value = ord(char)
            decrypted_char = chr((ascii_value - shift_key) % 26 + ord('A') if char.isupper() else (ascii_value - shift_key) % 26 + ord('a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

cryptogram = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'
shift_key = 1  # You may need to try different shift values to decipher the cryptogram

decrypted_quote = decrypt_cryptogram(cryptogram, shift_key)
print("Decrypted Quote:", decrypted_quote)

# Decrypt the cryptogram with different shift key values
for shift_key in range(26):  # Try all possible shift values
    decrypted_quote = decrypt_cryptogram(cryptogram, shift_key)
    print(f"Shift Key = {shift_key}: {decrypted_quote}")