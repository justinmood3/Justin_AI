import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS chat (
    sender TEXT,
    message TEXT
)
""")

def save(sender, message):
    c.execute("INSERT INTO chat VALUES (?, ?)", (sender, message))
    conn.commit()