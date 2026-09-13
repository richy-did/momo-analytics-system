from __future__ import annotations

import sqlite3
from pathlib import Path


def get_connection(db_path: str | Path = "data/db.sqlite3"):
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn


def init_db(conn: sqlite3.Connection):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_ref TEXT,
            date TEXT,
            amount REAL,
            phone TEXT,
            type TEXT,
            channel TEXT,
            description TEXT
        )
        """
    )
    conn.commit()


def insert_transaction(conn: sqlite3.Connection, record: dict):
    conn.execute(
        """
        INSERT INTO transactions (transaction_ref, date, amount, phone, type, channel, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record.get("transaction_ref"),
            record.get("date"),
            record.get("amount", 0.0),
            record.get("phone"),
            record.get("type"),
            record.get("channel"),
            record.get("description"),
        ),
    )
    conn.commit()
