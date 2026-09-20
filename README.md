# eja18-otp

# Persyaratan

- Android 7+
- Termux (dari F-Droid, bukan Play Store)
- Koneksi internet
- Storage kosong ~200 MB

# Install Termux

Download dari F-Droid:

https://f-droid.org/packages/com.termux/

Jangan install dari Play Store, versinya sudah usang.

# Buka Termux

Tunggu sampai muncul prompt:

    ~ $

# Update & Upgrade

    pkg update && pkg upgrade -y

Kalau muncul pertanyaan, ketik `y` lalu Enter.

# Izinkan Akses Storage

    termux-setup-storage

Akan muncul popup "Allow Termux to access files?" - tap Allow.

# Install Python

    pkg install python -y

Cek:

    python --version

# Install Git

    pkg install git -y

Cek:

    git --version

# Install Library Python

    pip install requests

Cek:

    python -c "import requests; print('OK')"

# Install nano

    pkg install nano -y

# Cara Clone Repo

    cd ~
    git clone https://github.com/ejaaa18/ejaotp.git
    cd ejaotp

# Cara Menjalankan

    python run.py

# Login

Masukkan username & password yang diberikan admin.

    +==========================================+
    |            LOGIN DULU                    |
    +==========================================+

    Username : budi
    Password : *******

    [OK] Login berhasil! Selamat datang, budi

# Masukkan Nomor

    Masukan Nomor : 08xxxxxxxxxx

Script akan mengirim OTP otomatis.

# Cara Update Script

    cd ~/ejaotp
    git pull
    python run.py

# Cara Berhenti

Tekan CTRL + C.

# Troubleshooting

Kalau muncul "command not found: python":

    pkg install python -y

Kalau muncul "ModuleNotFoundError: No module named 'requests'":

    pip install requests

Kalau muncul "Permission denied":

    termux-setup-storage

Kalau muncul "fatal: could not read Username":

    cd ~
    rm -rf ejaotp
    git clone https://github.com/ejaaa18/ejaotp.git

# Catatan

- Script berjalan loop tanpa batas (jeda 60 detik tiap round)
- Login cuma bisa dari 1 HP (anti-device)
- Kalau login dari HP lain, akun ter-BAN
- Jangan hapus folder ejaotp sembarangan

# Pertanyaan

Hubungi admin jika:

- Lupa password
- Akun ter-BAN
- Mau ganti device
- Butuh bantuan

# Lisensi

Private - hanya untuk pengguna terdaftar.
