import rsa_core
import sha256_helper

def verify_document():
    # Nhận và đọc dữ liệu
    print("- Đang đọc dữ liệu nhận được (Khóa & Chữ ký)...")
    try:
        with open("public_key.txt", "r") as f:
            lines = f.readlines()
            n = int(lines[0].strip())
            e = int(lines[1].strip())
            public_key = (n, e)

        with open("signature.txt", "r") as f:
            signature = int(f.read().strip())
        print("    -> Đã nạp thành công Khóa công khai và Chữ ký số.\n")
    except FileNotFoundError:
        print("    -> [LỖI] Thiếu file 'public_key.txt' hoặc 'signature.txt'. Không thể xác thực!")
        return

    # Băm lại file PDF hiện tại
    pdf_path = "document.pdf"
    print(f"- Đang tự băm lại file '{pdf_path}' đang có...")
    try:
        hash_int, hash_hex = sha256_helper.hash_file(pdf_path)
        hash_hex = hash_hex.zfill(64)
        print(f"    -> Mã băm tự tính:     {hash_hex}\n")
    except FileNotFoundError:
        print("    -> [LỖI] Không tìm thấy file tài liệu để kiểm tra!")
        return

    # Giải mã chữ ký bằng Khóa công khai
    print("- Đang dùng Khóa Công Khai để giải mã chữ ký...")
    recovered_hash_int = rsa_core.encrypt_decrypt(signature, public_key)
    recovered_hash_hex = hex(recovered_hash_int)[2:].zfill(64)
    print(f"    -> Mã băm từ chữ ký:   {recovered_hash_hex}\n")

    # Đối chiếu kết quả
    print("\n- KẾT QUẢ ĐỐI CHIẾU:")
    if hash_hex.lower() == recovered_hash_hex.lower():
        print("    ✅ HỢP LỆ! Mã băm hoàn toàn trùng khớp.")
        print("    => Tài liệu là nguyên bản và đúng người gửi.")
    else:
        print("    ❌ CẢNH BÁO: MÃ BĂM SAI LỆCH!")
        print("    => Tài liệu đã bị chỉnh sửa hoặc chữ ký là giả mạo.")

if __name__ == "__main__":
    verify_document()