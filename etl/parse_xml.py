from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path


def parse_xml_file(path: str | Path):
    """Parse a raw XML file and return an ElementTree."""
    tree = ET.parse(path)
    return tree.getroot()


def iter_transactions(root):
    """Yield transaction elements from the XML root."""
    for transaction in root.iter("transaction"):
        yield transaction
