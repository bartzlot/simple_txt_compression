import random
import os

def generate_key(length: int):
    return os.urandom(length)


def encode(key: bytes, plaintext: bytes):

    encoded = bytearray()

    for i in range(len(plaintext)):
        encoded.append((plaintext[i] + i) % 256 ^ key[i % len(key)])

    return bytes(encoded)


def decode(key: bytes, ciphertext: bytes):

    decoded = bytearray()

    for i in range(len(ciphertext)):
        decoded.append((((ciphertext[i]) ^ key[i % len(key)]) - i) % 256)

    return bytes(decoded)
