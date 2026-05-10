import rsa_core
import sha256_helper

def sign_document():
    # Tạo khóa
    print("- Đang tạo cặp khóa RSA 1024-bit...")
    public_key, private_key = rsa_core.generate_keypair(1024)
    n, e = public_key

    # Mô phỏng việc "gửi" Khóa công khai bằng cách lưu ra file
    with open("public_key.txt", "w") as f:
        f.write(f"{n}\n{e}")
    print("    -> Đã xuất khóa công khai ra file: 'public_key.txt'\n")

    # Đọc và băm file PDF
    pdf_path = "document.pdf"
    try:
        print(f"- Đang băm nội dung file '{pdf_path}'...")
        hash_int, hash_hex = sha256_helper.hash_file(pdf_path)
        hash_hex = hash_hex.zfill(64)
        print(f"    -> Mã băm SHA-256 (Hash): {hash_hex}\n")
    except FileNotFoundError:
        print(f"    -> [LỖI] Không tìm thấy file {pdf_path} để ký!")
        return

    # Ký số bằng Khóa bí mật
    print("- Đang dùng Khóa Bí Mật để tạo Chữ Ký Số...")
    signature = rsa_core.encrypt_decrypt(hash_int, private_key)

    # Mô phỏng việc "gửi" Chữ ký số
    with open("signature.txt", "w") as f:
        f.write(str(signature))
    print("    -> Đã xuất chữ ký số ra file: 'signature.txt'")

if __name__ == "__main__":
    sign_document() 