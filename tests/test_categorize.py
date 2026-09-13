from etl.categorize import categorize_transaction


def test_cash_in_category():
    assert categorize_transaction("Cash In from Jane") == "cash_in"


def test_cash_out_category():
    assert categorize_transaction("Cash Out to merchant") == "cash_out"


def test_unknown_category():
    assert categorize_transaction("Some weird message") == "unknown"
