import math_utils

def generate_keypair(keysize=1024):
    p = math_utils.generate_large_prime(keysize)
    q = math_utils.generate_large_prime(keysize)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = math_utils.mod_inverse(e, phi)
    
    return ((n, e), (n, d))

def encrypt_decrypt(data_int, key):
    n, k = key
    return pow(data_int, k, n)