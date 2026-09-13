from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from etl.clean_normalize import normalize_amount, normalize_date, normalize_phone
from etl.config import DB_PATH, PROCESSED_DIR, RAW_XML_PATH
from etl.categorize import categorize_transaction
from etl.load_db import get_connection, init_db, insert_transaction


def parse_arguments():
    parser = argparse.ArgumentParser(description="Run the MoMo ETL workflow.")
    parser.add_argument("--xml", type=str, default=str(RAW_XML_PATH), help="Path to the input XML file.")
    parser.add_argument("--db", type=str, default=str(DB_PATH), help="Path to the SQLite database.")
    return parser.parse_args()


def load_transactions(xml_path: str):
    root = ET.parse(xml_path).getroot()
    records = []

    for node in root.iter("transaction"):
        description = node.findtext("description") or node.findtext("message") or ""
        amount = normalize_amount(node.findtext("amount"))
        phone = normalize_phone(node.findtext("phone"))
        raw_date = node.findtext("date") or node.findtext("timestamp") or ""
        record = {
            "transaction_ref": node.get("id") or node.get("ref") or "",
            "date": normalize_date(raw_date),
            "amount": amount,
            "phone": phone,
            "type": categorize_transaction(description),
            "channel": node.get("channel") or "sms",
            "description": description,
        }
        records.append(record)

    return records


def export_dashboard(records):
    summary = [
        {"label": "Total transactions", "value": len(records)},
        {"label": "Total amount", "value": round(sum(item["amount"] for item in records), 2)},
        {"label": "Cash In", "value": sum(1 for item in records if item["type"] == "cash_in")},
        {"label": "Cash Out", "value": sum(1 for item in records if item["type"] == "cash_out")},
    ]

    categories = []
    for kind in ["cash_in", "cash_out", "transfer", "pay_bill", "airtime", "unknown"]:
        count = sum(1 for item in records if item["type"] == kind)
        categories.append({"label": kind.replace("_", " ").title(), "value": count})

    payload = {
        "summary": summary,
        "categories": categories,
        "transactions": [
            {
                "date": item["date"],
                "type": item["type"],
                "amount": item["amount"],
                "phone": item["phone"],
                "channel": item["channel"],
            }
            for item in records[:20]
        ],
    }

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DIR / "dashboard.json"
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return output_path


def main():
    args = parse_arguments()
    records = load_transactions(args.xml)

    conn = get_connection(args.db)
    init_db(conn)
    for item in records:
        insert_transaction(conn, item)
    conn.close()

    export_dashboard(records)
    print(f"Processed {len(records)} transactions into {args.db}")


if __name__ == "__main__":
    main()
