import secrets

def is_prime(n, k=40):
    # Kiểm tra số nguyên tố bằng thuật toán Miller-Rabin (k vòng lặp)
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Tìm r và d sao cho n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 4) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(keysize=1024):
    # Tạo một số nguyên tố ngẫu nhiên có độ dài keysize bits
    while True:
        num = secrets.randbits(keysize)
        # Đảm bảo số lẻ và có độ dài bit đúng yêu cầu
        num |= (1 << (keysize - 1)) | 1
        if is_prime(num):
            return num

def extended_gcd(a, b):
    # Thuật toán Euclid mở rộng để tìm nghịch đảo mô-đun
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    # Tìm d sao cho (e * d) % phi == 1
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Không tồn tại nghịch đảo mô-đun")
    else:
        return x % phi