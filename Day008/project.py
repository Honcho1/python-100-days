alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift_amount, action):
    result = []
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            if action == "encode":
                new_index = (index + shift_amount) % 26
            elif action == "decode":
                new_index = (index - shift_amount) % 26
            else:
                print("Invalid direction. Choose either 'encode' or 'decode'.")
                return
            result.append(alphabet[new_index])
        else:
            result.append(char)
    final_result = "".join(result)
    print(f"The {action}d text is: {final_result}")

from art import logo
print(logo)

def cipher_program():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

def main():
    while True:
        cipher_program()
        choice = input("Would you like to restart the cipher program? Type 'yes' or 'no'.\n")
        if choice != "yes":
            print("Goodbye!")
            break