# db.py
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).with_name("logs.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT NOT NULL,
            energy INTEGER NOT NULL,
            mind INTEGER NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_log(energy: int, mind: int, note: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (time, energy, mind, note) VALUES (?, ?, ?, ?)",
        (datetime.now().strftime("%Y-%m-%d %H:%M"), energy, mind, note)
    )
    conn.commit()
    conn.close()

def fetch_logs():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_log(log_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    conn.commit()
    conn.close()

def get_log_by_id(log_id: int):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM logs WHERE id = ?", (log_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def update_log(log_id: int, energy: int, mind: int, note: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE logs SET energy = ?, mind = ?, note = ? WHERE id = ?",
        (energy, mind, note, log_id)
    )
    conn.commit()
    conn.close()
