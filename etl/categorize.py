from __future__ import annotations


def categorize_transaction(description: str | None) -> str:
    """Assign a general category based on the description text."""
    text = (description or "").lower()
    if "cash in" in text or "deposit" in text:
        return "cash_in"
    if "cash out" in text or "withdraw" in text:
        return "cash_out"
    if "transfer" in text or "sent to" in text:
        return "transfer"
    if "airtime" in text or "top up" in text:
        return "airtime"
    if "bill" in text or "payment" in text:
        return "pay_bill"
    return "unknown"
