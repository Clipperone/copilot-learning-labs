import re
import hashlib
from datetime import datetime


def fmt(d):
    return d.strftime("%Y-%m-%d") if d else ""


def check(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))


def h(password):
    return hashlib.md5(password.encode()).hexdigest()


def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except Exception:
        return None


def clean(text):
    if text:
        return text.strip().lower()
    return ""


def make_id():
    import uuid
    return str(uuid.uuid4())[:8]


def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}")
