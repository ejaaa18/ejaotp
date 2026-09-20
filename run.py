import os
import sys

PRIVATE = os.path.expanduser("~/storage/downloads/otpeja")
TARGET = "eja18.py"


def main():
    old_dir = os.getcwd()
    target_path = os.path.join(PRIVATE, TARGET)

    if not os.path.exists(target_path):
        print("[!] File tidak ada: " + target_path)
        print("[!] Pastikan folder otpeja ada di Download.")
        sys.exit(1)

    os.chdir(PRIVATE)
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            kode = f.read()
        exec(compile(kode, target_path, "exec"), {"__name__": "__main__"})
    finally:
        os.chdir(old_dir)


main()
