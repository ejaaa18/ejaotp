# eja18-otp

Script OTP otomatis untuk Termux.

---

## Persyaratan

- Termux (dari F-Droid, bukan Play Store)
- Python 3.10+
- Internet

---

## Instalasi

### 1. Update Termux

    pkg update && pkg upgrade -y

### 2. Install Python & Git

    pkg install python git -y

### 3. Install Library

    pip install requests

---

## Cara Menjalankan

### 1. Clone Repo

    cd ~
    git clone https://github.com/ejaaa18/ejaotp.git
    cd ejaotp

### 2. Jalankan Script

    python run.py

### 3. Login

Masukkan username & password yang sudah diberikan admin.

    +==========================================+
    |            LOGIN DULU                    |
    +==========================================+

    Username : budi
    Password : *******

    [OK] Login berhasil! Selamat datang, budi

### 4. Masukkan Nomor

    Masukan Nomor : 08xxxxxxxxxx

Script akan mengirim OTP otomatis.

---

## Catatan

- Script berjalan **loop tanpa batas**
- Tekan **CTRL+C** untuk berhenti

---

## Pertanyaan

Hubungi admin jika:
- Lupa password
- Akun ter-BAN
- Butuh bantuan

---

## Lisensi

Private - hanya untuk pengguna terdaftar.
