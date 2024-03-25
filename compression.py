import sys

file_path = sys.argv[1]
text_data = []
compressed_text = ''
compressed_message = ''
compresion_keys = []

def get_bin_rep(letter, compression_keys):

    for item in compresion_keys:

        if item['letter'] == letter:
            return item['bin_rep']

def convert_to_bytes(binary_string):

  if not all(char in ("0", "1") for char in binary_string):
    raise ValueError("Binarne wartości mogą zawierać tylko 0 i 1.")

  padded_string = binary_string.zfill(len(binary_string) + (8 - len(binary_string) % 8) % 8)

  bytes_list = []
  for i in range(0, len(padded_string), 8):
    byte_string = padded_string[i:i+8]
    byte_value = int(byte_string, 2)
    bytes_list.append(byte_value)

  return bytes_list

try: 

    with open(file_path) as f:
        for line in f:
            text_data.append(line)
except:
    print('Nie udało się otworzyć pliku')
    sys.exit()


symbols = sorted(set(text_data[0]))

bit_amount = (len(symbols)-1).bit_length()
dict_len = len(symbols)
dict_len = bytes([dict_len])

for i, letter in enumerate(symbols):
    compresion_keys.append({'letter' : letter,
                       'bin_rep': format(i, f'0{bit_amount}b')})

for letter in text_data[0]:

    compressed_message += get_bin_rep(letter, compresion_keys)

redundant_bits_amount = 8 - (len(compressed_message) % 8)

compressed_text += format(redundant_bits_amount - 3, '03b')
compressed_text += compressed_message
compressed_text += (redundant_bits_amount -3 ) * '0'

int_list = convert_to_bytes(compressed_text)
int_list = bytes(int_list)

with open('compressed.txt', 'wb') as f:
    f.write(dict_len)
    for i in symbols:
        f.write(i.encode('utf-8'))
    f.write(int_list)


