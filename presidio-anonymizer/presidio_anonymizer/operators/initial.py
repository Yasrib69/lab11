from typing import Dict
from .operator import Operator, OperatorType


class Initial(Operator):
    """
    An operator that converts words to initials, preserving any non-alphanumeric
    prefix characters and collapsing extra whitespace.

    Examples:
    - "John Smith" -> "J. S."
    - "  Eastern   Michigan   University  " -> "E. M. U."
    - "@abc" -> "@A."
    - "@G48A3" -> "@G."
    - "-*-abc" -> "-*-A."
    """

    def operate(self, text: str, params: Dict = None) -> str:
        if text is None:
            return text

        # Split the text on whitespace into words (collapses extra spaces)
        words = text.split()
        initials_words = []

        for word in words:
            if not word:
                continue

            # Find index of first alphanumeric character
            first_alnum_idx = None
            for i, ch in enumerate(word):
                if ch.isalnum():
                    first_alnum_idx = i
                    break

            # If no alphanumeric character exists, return whole word unchanged
            if first_alnum_idx is None:
                initials_words.append(word)
                continue

            prefix = word[:first_alnum_idx]              # non-alnum prefix (e.g. "@", "-*-")
            first_char = word[first_alnum_idx].upper()   # the initial

            initials_words.append(f"{prefix}{first_char}.")

        # Join initials with single spaces
        return " ".join(initials_words)

    def validate(self, params: Dict = None) -> None:
        return

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
