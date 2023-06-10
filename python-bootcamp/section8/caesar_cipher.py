alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        length_of_alphabet = len(alphabet)
        if new_position >= length_of_alphabet: # encode에서만 해당 조건 발생
            new_position -= length_of_alphabet

        end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}")

caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

# def caesar(cipher_direction, start_text, shift_amount):
#     end_text = ""

#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if(cipher_direction == "encode"):
#             new_position = position + shift_amount
#             length_of_alphabet = len(alphabet)
#             if new_position >= length_of_alphabet:
#                 new_position -= length_of_alphabet

#         end_text += alphabet[new_position]

#     print(end_text)

# def encrypt(plain_text, shift_amount):
#     length_of_alphabet = len(alphabet)
#     cipher_text = ""

#     for letter in plain_text:
#         index = alphabet.index(letter)
#         chipher_index = index + shift_amount
#         if chipher_index >= length_of_alphabet:
#             chipher_index -= length_of_alphabet

#         cipher_text += alphabet[chipher_index]

#     print(cipher_text)

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""

#     for letter in cipher_text:
#         index = alphabet.index(letter)
#         plain_index = index - shift_amount
#         plain_text += alphabet[plain_index]
    
#     print(plain_text)

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)