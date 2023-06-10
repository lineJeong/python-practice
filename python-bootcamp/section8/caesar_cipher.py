alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    length_of_alphabel = len(alphabet)
    cipher_text = ""

    for letter in plain_text:
        index = alphabet.index(letter)
        chipher_index = index + shift_amount
        if chipher_index >= length_of_alphabel:
            chipher_index -= length_of_alphabel

        cipher_text += alphabet[chipher_index]

    print(cipher_text)

def decrypt(cipher_text, shift_amount):
    plain_text = ""

    for letter in cipher_text:
        index = alphabet.index(letter)
        plain_index = index - shift_amount
        plain_text += alphabet[plain_index]
    
    print(plain_text)

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)