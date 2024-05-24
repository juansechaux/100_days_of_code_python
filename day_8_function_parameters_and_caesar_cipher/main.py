from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    final_text = ""
    shift = shift % 26
    for char in text:
        if char in alphabet:
            ind = alphabet.index(char)
            if direction.lower() == "decode":
                final_text += alphabet[ind - shift]
            elif direction.lower() == "encode":
                if ind + shift > 25:
                    final_text += alphabet[ind + shift - 26]
                else:
                    final_text += alphabet[ind + shift]
            else:
                print("You type an invalid method")
                exit()
        else:
            final_text += char
    print(f"The {direction}d text is {final_text}")

print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
print("Goodbye")
