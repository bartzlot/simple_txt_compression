import sys

file_path = sys.argv[1]


def decompress(compressed_file):

    try:
        with open(compressed_file, 'rb') as f:

            byte = f.read(1)
            f.seek(1)
            dict_len = int.from_bytes(byte, 'big')
            dict = list(f.read(dict_len).decode('utf-8'))

            bit_amount = (len(dict)-1).bit_length()

            compressed_text = f.read()
            compressed_text = bin(int.from_bytes(compressed_text, 'big'))[2:]

            if len(compressed_text)%8 != 0:
                compressed_text = '0' * (8 - len(compressed_text) % 8) + compressed_text

            redundat_bits = int(compressed_text[:3], 2)

            for i, letter in enumerate(dict):
                dict[i] = {'letter' : letter,
                        'bin_rep': format(i, f'0{bit_amount}b')}
            decompressed_message = ''
            letter = ''

            for integer in compressed_text[3:-redundat_bits]:

                letter += str(integer)
                for item in dict:
                    if item['bin_rep'] == letter:
                        decompressed_message += item['letter']
                        letter = ''
                        break
            
        return decompressed_message
    except:
        print('Nie udało się otworzyć pliku')
        sys.exit()


def write_file(decompressed_message):

    with open('decompressed.txt', 'w') as f:
        f.write(decompressed_message)


decompressed_message = decompress('compressed.txt')

write_file(decompressed_message)