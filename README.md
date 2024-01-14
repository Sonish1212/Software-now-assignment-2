Firstly, we seperate inputs in numbers and alphabets using the isdigit and isalpha function.
Then, from the numbers we find out the even numbers and there ASCII values.
Uppercase alpahbets are seperated with the issupper function.
And on the next question about decrypting the ciphertext.
For Qn No 3:
Line 4: The for loop should iterate over the characters in the text variable, but it currently iterates over the numbers 1 to 5. You should change [1, 2, 3, 4, 5] to text.
Lines 7-10: This code block checks if the character is alphabetic, but it uses incorrect comparisons. The if char.isalpha() condition should be used instead of if char.isalpha():.
Lines 11-22: This code block shifts the lowercase letters by the key value, but it doesn't handle cases where the shifted letter goes beyond 'z'. You should add an else clause that wraps the shifted value back around to 'a' if it is greater than 'z'.
Lines 23-28: This code block is similar to the previous one, but it handles uppercase letters. It has the same error of not handling cases where the shifted letter goes beyond 'Z'. You should add an else clause that wraps the shifted value back around to 'A' if it is greater than 'Z'.
Line 30: The encrypted_text += chr(shifted) line should be indented two spaces more to be inside the if block.
Line 33: The print(encrypted_code) line should be indented two spaces less to be outside the for loop.
