import argparse
import json
from workflow import draft_from_requirement
from xml_validator import validate_payment_xml

def main():
    parser = argparse.ArgumentParser(description="Requirements-to-Test Agent demo")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--requirement", help="Plain-language business requirement")
    group.add_argument("--validate-xml", help="Path to a synthetic payment XML file")
    args = parser.parse_args()
    if args.requirement:
        print(json.dumps(draft_from_requirement(args.requirement), indent=2))
    else:
        result = validate_payment_xml(args.validate_xml)
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result["valid"] else 1)

if __name__ == "__main__":
    main()
