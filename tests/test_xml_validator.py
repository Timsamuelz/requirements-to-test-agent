import tempfile
import unittest
from pathlib import Path
from xml_validator import validate_payment_xml

EXAMPLE = Path(__file__).parents[1] / "examples" / "payment.xml"

class XmlValidatorTests(unittest.TestCase):
    def test_example_passes_illustrative_rules(self):
        result = validate_payment_xml(EXAMPLE)
        self.assertTrue(result["valid"], result["errors"])

    def test_empty_amount_is_reported(self):
        xml = '<Document><MsgId>M1</MsgId><EndToEndId>E1</EndToEndId><Dbtr>D</Dbtr><Cdtr>C</Cdtr><InstdAmt Ccy="EUR"></InstdAmt></Document>'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.xml"
            path.write_text(xml, encoding="utf-8")
            result = validate_payment_xml(path)
        self.assertFalse(result["valid"])
        self.assertTrue(any("InstdAmt" in e for e in result["errors"]))

    def test_malformed_xml_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.xml"
            path.write_text("<broken>", encoding="utf-8")
            result = validate_payment_xml(path)
        self.assertFalse(result["valid"])
        self.assertTrue(result["errors"])

if __name__ == "__main__":
    unittest.main()
