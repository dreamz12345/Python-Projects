import os
os.system("cls")

def cypher(message):
    message_changed = ""
    for letter_in_message in message:
        # If space in message, add space
        if letter_in_message == " ":
            message_changed += " "
        else:
            # Search for letter_in_message in letters[]
            # if letter is found use its index to 
            # add letter from letters_shifted[] to message_changed
            for index, letter_in_list in enumerate(letters):
                if letter_in_message == letter_in_list:
                    message_changed += letters_shifted[index]
                    break
    return message_changed

index_from_zero = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z',]
letters_shifted = list(letters)
letters_len = len(letters)

print("Welcome to Ceasar Cipher!")
mode = input("Would you like to 'code' or 'decode' your message?: ")
shift = int(input("What is the shift: "))
message = input("Please write your message: ")

for index, letter in enumerate(letters):
    # Shift letters_shifted[] right by shift amount
    if mode == "decode":
        if (index + shift) < letters_len:
            letters_shifted[index + shift] = letters[index]
        else:
            letters_shifted[index_from_zero] = letters[index]
            index_from_zero += 1
    # Shift letters_shifted[] left by shift amount
    elif mode == "code":
        if (index + shift) < letters_len:
            letters_shifted[index] = letters[index + shift]
        else:
            letters_shifted[index] = letters[index_from_zero]
            index_from_zero += 1

message_changed = cypher(message)
if mode == "decode":
    print(f"\nMessage decoded: {message_changed}\n")
elif mode == "code":
    print(f"\nCoded message: {message_changed}\n")
