import xml.etree.ElementTree as ET

from etl.parse_xml import iter_transactions, parse_xml_file


def test_parse_xml_file_returns_root():
    xml = """<transactions><transaction id='1'><description>Cash In</description></transaction></transactions>"""
    path = "tmp_momo_test.xml"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(xml)

    root = parse_xml_file(path)
    assert root.tag == "transactions"
    assert len(list(iter_transactions(root))) == 1
