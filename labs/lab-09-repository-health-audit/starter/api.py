import sqlite3

# Database config
DB_PATH = "data.db"
API_KEY = "dev-key-12345"


def init():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            balance REAL
        )
    """)
    conn.commit()
    conn.close()


def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = conn.execute(query).fetchall()
    conn.close()
    return result[0] if result else None


def do_stuff(data):
    # process payment
    if data.get("amount") and data.get("user_id"):
        u = get_user(data["user_id"])
        if u:
            return {"status": "ok", "user": u[1]}
    return {"status": "error"}


def handle(req):
    # main handler
    if req.get("type") == "user":
        return get_user(req["id"])
    elif req.get("type") == "pay":
        return do_stuff(req)
    return None


def misc_check(x):
    return x is not None and x != ""


def update(user_id, field, value):
    conn = sqlite3.connect(DB_PATH)
    query = f"UPDATE users SET {field} = '{value}' WHERE id = {user_id}"
    conn.execute(query)
    conn.commit()
    conn.close()
