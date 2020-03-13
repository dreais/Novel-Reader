import sqlite3
import config


def get_user_id(email):
    conn = sqlite3.connect(config.DATABASE)
    c = conn.cursor()
    id = 0
    c.execute("SELECT id FROM users WHERE email='" + email + "';")
    id = int(c.fetchone()[0])
    conn.close()
    if id:
        return id
    else:
        return -1