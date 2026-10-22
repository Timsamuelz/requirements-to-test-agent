"""Illustrative XML checks; not a full ISO 20022 or CBPR+ validator."""
import xml.etree.ElementTree as ET
from decimal import Decimal, InvalidOperation
from pathlib import Path

def validate_payment_xml(path):
    try:
        root = ET.parse(Path(path)).getroot()
    except (ET.ParseError, OSError) as exc:
        return {"valid": False, "errors": [f"Could not parse XML: {exc}"]}
    def text_for(local_name):
        for element in root.iter():
            if element.tag.split("}")[-1] == local_name:
                return (element.text or "").strip()
        return ""
    errors = []
    names = ["MsgId", "EndToEndId", "InstdAmt"]
    values = {name: text_for(name) for name in names}
    for name, value in values.items():
        if not value:
            errors.append(f"Missing or empty required element: {name}")
    # Debtor and creditor are containers in this illustrative XML shape; require a non-empty name.
    for party in ("Dbtr", "Cdtr"):
        party_element = next((e for e in root.iter() if e.tag.split("}")[-1] == party), None)
        party_name = ""
        if party_element is not None:
            party_name = next(((e.text or "").strip() for e in party_element.iter()
                               if e.tag.split("}")[-1] == "Nm"), "")
        if not party_name:
            errors.append(f"Missing or empty required party name under: {party}")
    amount_text = values["InstdAmt"]
    if amount_text:
        try:
            if Decimal(amount_text) <= 0:
                errors.append("InstdAmt must be greater than zero")
        except InvalidOperation:
            errors.append("InstdAmt must be a valid decimal number")
    currency = ""
    for element in root.iter():
        if element.tag.split("}")[-1] == "InstdAmt":
            currency = element.attrib.get("Ccy", "").strip()
            break
    if not currency:
        errors.append("InstdAmt is missing the illustrative Ccy attribute")
    elif len(currency) != 3 or not currency.isalpha() or not currency.isupper():
        errors.append("Ccy must be a three-letter uppercase currency code")
    return {
        "valid": not errors,
        "errors": errors,
        "checks_performed": ["XML well-formedness", "Selected required elements",
                             "Positive decimal amount", "Three-letter uppercase currency code"],
        "scope_warning": "Illustrative checks only; not full ISO 20022 or CBPR+ validation."
    }
