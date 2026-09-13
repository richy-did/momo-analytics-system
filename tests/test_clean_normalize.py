from etl.clean_normalize import normalize_amount, normalize_date, normalize_phone


def test_normalize_phone():
    assert normalize_phone("+233 20 123 4567") == "201234567"


def test_normalize_amount():
    assert normalize_amount("GHS 50.00") == 50.0


def test_normalize_date():
    assert normalize_date("12/05/2024") == "2024-05-12"
