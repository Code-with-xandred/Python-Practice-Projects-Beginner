# 21. Ceaser Cipher Text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here Is The {encode_or_decode}d Result: {output_text}")

should_contniue = True

while should_contniue:
    direction = input("Type 'encode' To Encrypt, Type 'decode' To Decrypt:\n").lower()
    text = input("Type You Message:\n").lower()
    shift = int(input("Type The Shift Number:\n"))

    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' If You Want To Go Again. Otherwise, Type 'no'.\n").lower()
    if restart == "no":
        should_contniue = False
        print("GoodBoy")

# -----------------------------------------------------------------------------------------
