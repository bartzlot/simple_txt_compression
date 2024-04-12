import sys
from scrambler import decode

file_path = sys.argv[1]
decryption_key = sys.argv[2]
decryption_key = bytes.fromhex(decryption_key)

def decompress(file_path):
    decompressed_text = ''

    try:
        with open(file_path, 'rb') as f:

            dict_len = int.from_bytes(f.read(1), byteorder='big')
            symbols = [int.from_bytes(f.read(1), byteorder='big') for _ in range(dict_len)]
            compressed_data = f.read()
            compressed_data = decode(decryption_key, compressed_data)

    except Exception as e:

        print(f'Nie udało się otworzyć pliku: {e}')
        sys.exit(1)

    bit_amount = (len(symbols)-1).bit_length()
    decompression_keys = [{'letter' : letter, 'bin_rep': format(i, f'0{bit_amount}b')} for i, letter in enumerate(symbols)]

    binary_string = ''.join(format(byte, '08b') for byte in compressed_data)
    redundant_bits_amount = int(binary_string[:3], 2)
    binary_string = binary_string[3:-redundant_bits_amount]

    for i in range(0, len(binary_string), bit_amount):
        bin_rep = binary_string[i:i+bit_amount]

        for item in decompression_keys:

            if item['bin_rep'] == bin_rep:
                decompressed_text += chr(item['letter'])

                break

    return decompressed_text


def write_file(decompressed_message):

    with open('decompressed.txt', 'w') as f:
        f.write(decompressed_message)


decompressed_message = decompress('compressed.txt')

write_file(decompressed_message)