"""Local, transparent prototype; this module does not call an LLM."""
import re

def _split_requirement(text):
    cleaned = re.sub(r"\s+", " ", text).strip().rstrip(".")
    match = re.match(r"As an?\s+(.+?),\s*I want\s+(.+?)(?:\s+so that\s+(.+))?$",
                     cleaned, flags=re.IGNORECASE)
    if match:
        role, need, benefit = match.groups()
        return role.strip(), need.strip(), (benefit or "achieve the intended business outcome").strip()
    return "business user", cleaned, "achieve the intended business outcome"

def draft_from_requirement(requirement):
    if not requirement or not requirement.strip():
        raise ValueError("Requirement must not be empty.")
    role, need, benefit = _split_requirement(requirement)
    target = "required payment fields" if any(
        word in need.lower() for word in ("payment", "debtor", "creditor", "message", "xml")
    ) else "required information"
    return {
        "source_requirement": requirement.strip(),
        "user_story": {
            "role": role, "need": need, "benefit": benefit,
            "formatted": f"As a {role}, I want {need}, so that {benefit}."
        },
        "assumptions": [
            "The business owner will confirm scope, terminology, and applicable rules.",
            "The draft is not approved until reviewed by a responsible person."
        ],
        "acceptance_criteria": [
            {"id": "AC-001", "given": f"a user submits a requirement related to {target}",
             "when": "the workflow prepares a draft",
             "then": "the output includes a user story and explicit assumptions"},
            {"id": "AC-002", "given": "a requirement is ambiguous or lacks a measurable outcome",
             "when": "the draft is reviewed",
             "then": "the reviewer resolves the ambiguity before approval"},
            {"id": "AC-003", "given": "a draft has been generated",
             "when": "the output is returned",
             "then": "the output includes test scenarios and marks human review as required"}
        ],
        "test_cases": [
            {"id": "TC-001", "scenario": "Valid requirement supplied",
             "steps": ["Submit a non-empty requirement", "Inspect the JSON output"],
             "expected_result": "A user story, assumptions, criteria, and test cases are present"},
            {"id": "TC-002", "scenario": "Ambiguous requirement supplied",
             "steps": ["Submit a requirement without a clear benefit", "Review assumptions"],
             "expected_result": "The need for human clarification is visible"},
            {"id": "TC-003", "scenario": "Human approval control",
             "steps": ["Generate a draft", "Inspect the review flag"],
             "expected_result": "human_review_required is true"}
        ],
        "human_review_required": True,
        "generation_mode": "local_template_prototype_not_an_llm"
    }
