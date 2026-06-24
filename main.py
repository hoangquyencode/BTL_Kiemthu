import time
import os
import ctypes

# Cấu hình hiển thị màu cho Windows Terminal
if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"


# =====================================================================
# 1. HÀM CHỨC NĂNG CHUẨN CÓ XỬ LÝ BIÊN MẠNH (ROBUSTNESS)
# =====================================================================
def bank_loan_approval(credit_score: int, income: float) -> str:
    if not (300 <= credit_score <= 850):
        return "LỖI: Ngoài khoảng (300-850)!"
    if income < 0:
        return "LỖI: Thu nhập âm!"

    if credit_score >= 650 and income > 15.0:
        return "DUYỆT VAY"
    else:
        return "TỪ CHỐI"


# =====================================================================
# 2. HÀM TỰ ĐỘNG QUÉT VÀ IN RÕ BẢNG 7 TEST CASES
# =====================================================================
def run_auto_7_test_cases():
    # Định nghĩa ma trận dữ liệu 7 test cases chuẩn lý thuyết S5
    test_cases = [
        {"id": "TC01", "name": "Biên ĐÓNG đúng (C=650, I=25.0)", "c": 650, "i": 25.0, "expected": "DUYỆT VAY"},
        {"id": "TC02", "name": "Biên ĐÓNG sai  (C=649, I=25.0)", "c": 649, "i": 25.0, "expected": "TỪ CHỐI"},
        {"id": "TC03", "name": "Biên MỞ đúng   (C=700, I=15.1)", "c": 700, "i": 15.1, "expected": "DUYỆT VAY"},
        {"id": "TC04", "name": "Biên MỞ sai    (C=700, I=15.0)", "c": 700, "i": 15.0, "expected": "TỪ CHỐI"},
        {"id": "TC05", "name": "Giá trị cực tiểu (C=300, I=0.0) ", "c": 300, "i": 0.0, "expected": "TỪ CHỐI"},
        {"id": "TC06", "name": "Giá trị cực đại  (C=850, I=500.0)", "c": 850, "i": 500.0, "expected": "DUYỆT VAY"},
        {"id": "TC07", "name": "Biên mạnh lỗi    (C=250, I=-5.0) ", "c": 250, "i": -5.0,
         "expected": "LỖI: Ngoài khoảng (300-850)!"},
    ]

    print("\n" + f"{YELLOW}⚙️  KÍCH HOẠT QUÉT MA TRẬN 7 KỊCH BẢN KIỂM THỬ TỰ ĐỘNG...{RESET}")
    time.sleep(0.5)

    print(f"\n{CYAN}╔══════╦══════════════════════════════════════════════╦══════════════╦════════╗{RESET}")
    print(f"{CYAN}║ Mã TC║ Mô tả kịch bản kiểm thử ranh giới biên       ║ Kết quả chạy ║ Trạng  ║{RESET}")
    print(f"{CYAN}╠══════╬══════════════════════════════════════════════╬══════════════╬════════╣{RESET}")

    for tc in test_cases:
        actual = bank_loan_approval(tc["c"], tc["i"])
        # Nếu kết quả thực tế trùng khớp với kỳ vọng thì là PASS
        status = f"{GREEN}  PASS  {RESET}" if actual == tc["expected"] else f"{RED}  FAIL  {RESET}"
        mau_chu = GREEN if "DUYỆT" in actual else (RED if "TỪ CHỐI" in actual else YELLOW)

        print(f"{CYAN}║{RESET} {tc['id']} ║ {tc['name']:<44} ║ {mau_chu}{actual:<12}{RESET} ║ {status} ║")

    print(f"{CYAN}╚══════╩══════════════════════════════════════════════╩══════════════╩════════╝{RESET}")


# =====================================================================
# 3. GIAO DIỆN TƯƠNG TÁC NHẬP TAY
# =====================================================================
def interactive_run():
    while True:
        print("\n" + f"{CYAN}═" * 65 + f"{RESET}")
        print(f"{CYAN}   HỆ THỐNG KIỂM THỬ TƯƠNG TÁC BIÊN MẠNH - HOÀNG QUYÊN{RESET}")
        print(f"{CYAN}═" * 65 + f"{RESET}")

        try:
            score = int(input(" -> Nhập Điểm tín dụng (Thử số bất kỳ(300 - 850)): "))
            inc = float(input(" -> Nhập Thu nhập hằng tháng (Triệu VNĐ): "))

            print("-" * 65)
            print(f"{YELLOW}⏳ ĐANG PHÂN TÍCH RẠNH GIỚI...{RESET}")
            time.sleep(0.3)

            ket_qua = bank_loan_approval(score, inc)
            mau = GREEN if ket_qua == "DUYỆT VAY" else (RED if ket_qua == "TỪ CHỐI" else YELLOW)

            print(f"\n{mau} Kết quả nhập tay của bạn ➔: {ket_qua}{RESET}")

        except ValueError:
            print(f"\n{RED}[LỖI] Vui lòng nhập đúng số!{RESET}")

        tiep = input("\nBạn có muốn thử nhập điểm khác bằng tay không? (y/n): ").lower()
        if tiep != 'y':
            break


if __name__ == '__main__':
    # Bước 1: Cho bạn nhập tay thoải mái để demo tương tác
    interactive_run()

    # Bước 2: Khi dừng nhập tay, tự động in ra bảng 7 test cases rõ mồn một để giải thích lý thuyết
    run_auto_7_test_cases()