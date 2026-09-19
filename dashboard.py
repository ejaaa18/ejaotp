import os
import json
import hashlib
from datetime import datetime
from os import system
from time import sleep

USERS_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            return data.get("users", [])
    except Exception:
        return []


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump({"users": users}, f, indent=4)


def cek_online(last_seen_str):
    if not last_seen_str:
        return False
    try:
        last = datetime.strptime(last_seen_str, "%Y-%m-%d %H:%M:%S")
        beda = (datetime.now() - last).total_seconds()
        return beda < 120
    except Exception:
        return False


def menu_lihat():
    system("clear")
    users = load_users()
    print("=== DAFTAR USER ===")
    print()
    if not users:
        print("Belum ada user.")
    else:
        print("No | Username        | Status  | Device ID       | Terakhir Online")
        print("-" * 75)
        for i, u in enumerate(users, 1):
            dev = u.get("device_id", "-")
            if dev and len(dev) > 8:
                dev = dev[:8] + "..."
            last = u.get("last_seen", "-")
            print(str(i).ljust(3) + "| " + u.get("username", "").ljust(16) + "| " + u.get("status", "aktif").ljust(8) + "| " + str(dev).ljust(16) + "| " + str(last))
    print()
    input("Tekan Enter untuk kembali...")


def menu_tambah():
    system("clear")
    print("=== TAMBAH USER ===")
    print()
    username = input("Username : ").strip()
    if not username:
        print("Username tidak boleh kosong.")
        sleep(2)
        return

    users = load_users()
    for u in users:
        if u.get("username") == username:
            print("Username sudah dipakai.")
            sleep(2)
            return

    password = input("Password : ").strip()
    if not password:
        print("Password tidak boleh kosong.")
        sleep(2)
        return

    users.append({
        "username": username,
        "password": hash_password(password),
        "device_id": "",
        "status": "aktif",
        "last_seen": "",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_users(users)
    print()
    print("[OK] User berhasil ditambahkan!")
    sleep(2)


def menu_edit():
    system("clear")
    users = load_users()
    if not users:
        print("Belum ada user.")
        sleep(2)
        return

    print("=== EDIT USER ===")
    print()
    for i, u in enumerate(users, 1):
        print(str(i) + ". " + u.get("username", ""))

    print()
    try:
        pilih = int(input("Pilih nomor user : "))
    except ValueError:
        print("Input tidak valid.")
        sleep(2)
        return

    if pilih < 1 or pilih > len(users):
        print("Nomor tidak valid.")
        sleep(2)
        return

    user = users[pilih - 1]
    print()
    print("Edit user: " + user.get("username", ""))
    print("(kosongkan jika tidak diubah)")
    print()

    new_username = input("Username baru : ").strip()
    new_password = input("Password baru : ").strip()
    new_status = input("Status (aktif/banned) : ").strip()
    reset_device = input("Reset device ID? (y/n) : ").strip().lower()

    if new_username:
        user["username"] = new_username
    if new_password:
        user["password"] = hash_password(new_password)
    if new_status in ["aktif", "banned"]:
        user["status"] = new_status
    if reset_device == "y":
        user["device_id"] = ""

    save_users(users)
    print()
    print("[OK] User berhasil diupdate!")
    sleep(2)


def menu_hapus():
    system("clear")
    users = load_users()
    if not users:
        print("Belum ada user.")
        sleep(2)
        return

    print("=== HAPUS USER ===")
    print()
    for i, u in enumerate(users, 1):
        print(str(i) + ". " + u.get("username", ""))

    print()
    try:
        pilih = int(input("Pilih nomor user : "))
    except ValueError:
        print("Input tidak valid.")
        sleep(2)
        return

    if pilih < 1 or pilih > len(users):
        print("Nomor tidak valid.")
        sleep(2)
        return

    user = users[pilih - 1]
    konfirmasi = input("Yakin hapus " + user.get("username", "") + "? (y/n) : ").strip().lower()

    if konfirmasi == "y":
        users.pop(pilih - 1)
        save_users(users)
        print()
        print("[OK] User berhasil dihapus!")
    else:
        print("Dibatalkan.")
    sleep(2)


def menu_online():
    system("clear")
    users = load_users()
    print("=== USER YANG SEDANG ONLINE ===")
    print()
    online = []
    for u in users:
        if cek_online(u.get("last_seen", "")):
            online.append(u)

    if not online:
        print("Tidak ada user yang online.")
    else:
        for u in online:
            print("- " + u.get("username", "") + " (terakhir: " + u.get("last_seen", "-") + ")")

    print()
    input("Tekan Enter untuk kembali...")


while True:
    system("clear")
    print("+======================================+")
    print("|          DASHBOARD ADMIN             |")
    print("+======================================+")
    print()
    print("1. Lihat semua user")
    print("2. Tambah user")
    print("3. Edit user")
    print("4. Delete user")
    print("5. Lihat siapa yang online")
    print("6. Keluar")
    print()

    pilih = input("Pilih (1-6) : ").strip()

    if pilih == "1":
        menu_lihat()
    elif pilih == "2":
        menu_tambah()
    elif pilih == "3":
        menu_edit()
    elif pilih == "4":
        menu_hapus()
    elif pilih == "5":
        menu_online()
    elif pilih == "6":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")
        sleep(1)
