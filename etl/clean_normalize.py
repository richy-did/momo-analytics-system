from __future__ import annotations

import re
from datetime import datetime


def normalize_phone(value: str | None) -> str:
    """Return a consistent phone format for local identifiers."""
    if value is None:
        return ""
    cleaned = re.sub(r"\D", "", str(value))

    if cleaned.startswith("233"):
        cleaned = cleaned[3:]
    if cleaned.startswith("0"):
        cleaned = cleaned[1:]
    if len(cleaned) > 9:
        cleaned = cleaned[-9:]
    return cleaned


def normalize_amount(value: str | float | int | None) -> float:
    """Convert monetary values into a numeric float."""
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = str(value).replace(",", "").replace("GHS", "").replace("GH¢", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def normalize_date(value: str | None) -> str:
    """Normalize ambiguous dates to ISO YYYY-MM-DD if possible."""
    if value is None or value == "":
        return ""
    cleaned = str(value).strip()
    formats = ["%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y", "%Y/%m/%d", "%d %b %Y"]
    for fmt in formats:
        try:
            return datetime.strptime(cleaned, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return cleaned
