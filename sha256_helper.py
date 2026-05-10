import hashlib

def hash_file(file_path):
    sha256_hash = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        # Đọc từng khối 4096 bytes để tránh tốn RAM nếu file lớn
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    hash_hex = sha256_hash.hexdigest()
    # Chuyển chuỗi Hex (thập lục phân) thành số nguyên (integer) để tính toán RSA
    return int(hash_hex, 16), hash_hex