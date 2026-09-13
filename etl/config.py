from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_XML_PATH = DATA_DIR / "raw" / "momo.xml"
PROCESSED_DIR = DATA_DIR / "processed"
DB_PATH = DATA_DIR / "db.sqlite3"
LOG_DIR = DATA_DIR / "logs"
DEAD_LETTER_DIR = LOG_DIR / "dead_letter"

TRANSACTION_TYPES = {
    "cash_in": "Cash In",
    "cash_out": "Cash Out",
    "transfer": "Transfer",
    "pay_bill": "Pay Bill",
    "airtime": "Airtime",
    "unknown": "Unknown",
}
