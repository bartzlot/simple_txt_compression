import random

# def shifts_encryption_formula(total_shifts: int, key):




def generate_key(length: int):

    key = ''

    for i in range(length):
        key += chr(random.randint(0, 127))

    return key


def encode(key: str, text: str):

    encoded_text = ''
    last_shift = sum([ord(key[i % len(key)]) for i in range(len(text))])

    for i, letter in enumerate(text):
        
        shift = ord(key[i % len(key)]) + last_shift % 95 
        encoded_letter = chr(((ord(letter) - 32 + shift) % 95) + 32)

        while encoded_letter == '\n':
            shift += 1
            encoded_letter = chr(((ord(letter) - 32 + shift) % 95) + 32)

        encoded_text += encoded_letter
        last_shift = shift

    return encoded_text


def decode(key: str, text: str):

    decoded_text = ''
    last_shift = sum([ord(key[i % len(key)]) for i in range(len(text))])
    for i, letter in enumerate(text):
        
        shift = ord(key[i % len(key)]) + last_shift % 95 
        decoded_letter = chr(((ord(letter) - 32 - shift + 95) % 95) + 32)

        decoded_text += decoded_letter
    
        last_shift = shift
        
    return decoded_text


str = (encode('k', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
print(str)
print(decode('k', str))



#TODO najpierw kompresja, później szyfrowanie