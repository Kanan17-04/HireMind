import re
class JDCleaner:

    @staticmethod
    def clean(text: str) -> str:

        noise_patterns = [
            r"Home",
            r"Jobs Search Results",
            r"Sign in",
            r"Send feedback",
            r"Help link",
            r"Showing \d+ to \d+ of \d+ rows",
        ]

        cleaned = text

        for pattern in noise_patterns:
            cleaned = re.sub(
                pattern,
                "",
                cleaned,
                flags=re.IGNORECASE
            )

        cleaned = re.sub(
            r"\n{3,}",
            "\n\n",
            cleaned
        )

        return cleaned.strip()