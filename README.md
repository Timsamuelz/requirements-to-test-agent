# Requirements-to-Test Agent

A portfolio demo of a configurable AI-agent workflow for business analysis and QA. It converts a plain-language requirement into a structured user story, Gherkin acceptance criteria, and test cases. It also provides a deterministic validator for a small, synthetic ISO 20022-style payment XML example.

> **Scope note:** This is a learning/demo project, not a production banking system and not a full ISO 20022 schema validator. Examples are synthetic. Generated requirements must be reviewed by a person before use.

## Features
- Configurable workflow instructions in `agent/instructions.md`
- Repeatable requirement-to-test workflow
- Structured JSON output
- Deterministic XML checks for required fields, amount, currency, and message identifiers
- Unit tests and no API key required for the starter demo
- Clearly documented extension point for a real LLM integration

## Quick start
Requires Python 3.10+.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python main.py --requirement "As a payment operations analyst, I want invalid payment messages flagged before submission so that I can correct them."
python main.py --validate-xml examples/payment.xml
python -m unittest discover -s tests -v
```

## How it works
1. Read a plain-language requirement.
2. Apply the workflow policy in `agent/instructions.md`.
3. Draft a user story, assumptions, Given/When/Then acceptance criteria, and test cases.
4. Return JSON and mark human review as required.
5. Separately run deterministic checks against the synthetic XML sample.

**Transparency:** the included requirement workflow uses local template/heuristic logic and does not call an LLM. This makes the starter demo reproducible without credentials. Add a real model adapter only after selecting and testing a provider.

## Example output shape
```json
{
  "user_story": {
    "role": "payment operations analyst",
    "need": "flag invalid payment messages before submission",
    "benefit": "correct them"
  },
  "assumptions": [],
  "acceptance_criteria": [
    {
      "given": "a payment message is missing a required field",
      "when": "the message is validated",
      "then": "the validator reports the missing field"
    }
  ],
  "test_cases": [],
  "human_review_required": true
}
```

## Project structure
```text
requirements-to-test-agent/
├── agent/instructions.md
├── examples/payment.xml
├── tests/test_xml_validator.py
├── main.py
├── workflow.py
├── xml_validator.py
├── requirements.txt
└── README.md
```

## Using Argon or another coding agent
In the coding-agent environment you actually use:
1. Ask it to read `agent/instructions.md`.
2. Ask it to improve `workflow.py` while preserving the JSON output structure.
3. Ask it to run `python -m unittest discover -s tests -v`.
4. Inspect the diff and test output before accepting changes.
5. Document the real tool and configuration you used.

Do not claim an Argon integration, MCP server, hook, or automated agent execution unless you configure and test it in your own environment.

## Limitations and responsible use
- XML checks are illustrative business-rule checks, not XSD validation or full CBPR+ compliance.
- The local requirement workflow is not LLM-powered.
- No payments are sent or processed against real customer data.
- Human review is required before generated stories or tests are used downstream.
- Do not upload confidential requirements or production payment data to unapproved services.

## Demo script
1. Run the requirement example.
2. Explain the story, criteria, and test cases.
3. Validate `examples/payment.xml`.
4. Run unit tests.
5. Empty a required XML element and rerun validation to show a failure.
6. Explain the role of agent instructions and human approval.

## Roadmap
- [ ] Validate output against JSON Schema
- [ ] Add an optional LLM adapter with explicit provider configuration
- [ ] Add a small interactive UI
- [ ] Add official ISO 20022 XSD validation
- [ ] Add CI for pull requests

## License
MIT. See `LICENSE`.
