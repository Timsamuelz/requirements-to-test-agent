# Requirements-to-Test Agent

A Python prototype exploring how business requirements can be transformed into structured user stories, acceptance criteria, and test scenarios, alongside illustrative payment XML validation.

## Business Problem

Business Analysts and Product Owners often need to translate business requirements into clear, testable specifications. For cross-border payments and ISO 20022 migration projects, unclear requirements and incomplete validation can create avoidable issues during development and testing.

This project explores a small, transparent workflow to help structure requirements and demonstrate selected payment XML checks.

## Project Capabilities

### 1. Requirements Workflow
- Accepts a business requirement as input.
- Extracts the role, need, and benefit from a standard user story.
- Produces draft acceptance criteria and test scenarios.
- Flags the output for human review.

### 2. Payment XML Validation
- Checks whether XML is well-formed.
- Checks selected required elements.
- Checks that the payment amount is a positive decimal.
- Checks that the currency code uses three uppercase letters.

These are illustrative checks, not comprehensive ISO 20022, SWIFT CBPR+, or bank-specific validation rules.

### 3. Automated Tests
The project includes automated tests for user-story parsing and XML validation.

Current test result: **4 tests passed.**

## Technology
- Python
- XML parsing and validation
- Python `unittest`
- Git

## Run the Project

Run the requirements workflow:

```bash
python3 main.py --requirement "As a payments analyst, I want cross-border payment amounts and currency codes validated so that invalid payments are identified before processing."
```

Validate the example payment XML:

```bash
python3 main.py --validate-xml examples/payment.xml
```

Run the automated tests:

```bash
python3 -m unittest discover -s tests -v
```

## Current Status and Limitations

This is an early-stage, local Python prototype. The requirements workflow uses deterministic templates; it does not currently call a large language model or connect to Argon.

The project does not implement full ISO 20022 schema validation, SWIFT CBPR+ rule validation, or production payment processing.

Generated requirements and test scenarios require review by a qualified person before being used in a real project.

## Potential Next Steps
- Connect the workflow to an approved AI model.
- Explore integration with Argon to orchestrate custom AI-agent workflows.
- Add structured input and output validation.
- Expand test coverage using representative payment scenarios.
- Add applicable ISO 20022 schema and business-rule validation.

## Why This Project

The prototype reflects an interest in combining Business Analysis, Product Ownership, requirements engineering, test design, and payment-domain knowledge to explore practical AI-assisted workflows.
