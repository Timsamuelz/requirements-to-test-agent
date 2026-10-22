import unittest
from workflow import _split_requirement


class WorkflowTests(unittest.TestCase):
    def test_standard_user_story_is_parsed_correctly(self):
        text = (
            "As a payments analyst, I want cross-border payment amounts "
            "and currency codes validated so that invalid payments are "
            "identified before processing."
        )

        role, need, benefit = _split_requirement(text)

        self.assertEqual(role, "payments analyst")
        self.assertEqual(
            need,
            "cross-border payment amounts and currency codes validated",
        )
        self.assertEqual(
            benefit,
            "invalid payments are identified before processing",
        )


if __name__ == "__main__":
    unittest.main()
