# backend/app/agents/agent2_jd_parser/url_processor.py
from playwright.sync_api import sync_playwright
from .jd_cleaner import JDCleaner
from .jd_section_extractor import JDSectionExtractor
class URLProcessor:
    @staticmethod
    def extract_text(url: str) -> str:
        if not url.startswith(("http://", "https://")):
            raise ValueError("Invalid URL")
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(
                    headless=True
                )
                page = browser.new_page()
                page.goto(
                    url,
                    wait_until="networkidle",
                    timeout=60000
                )

                raw_text = page.locator("body").inner_text()

                browser.close()

            if not raw_text.strip():
                raise ValueError(
                    "No text could be extracted from the URL."
                )

            cleaned_text = JDCleaner.clean(
                raw_text
            )

            blocked_patterns = [
                "access denied",
                "permission to access",
                "errors.edgesuite.net",
                "akamai",
                "forbidden",
                "request blocked",
                "security check",
                "captcha",
            ]

            lower_text = cleaned_text.lower()

            if any(
                pattern in lower_text
                for pattern in blocked_patterns
            ):
                raise ValueError(
                    "This website blocks automated access. Please upload the JD PDF, DOCX, image, or paste the job description text."
                )

            jd_text = JDSectionExtractor.extract(
                cleaned_text
            )

            if not jd_text.strip():
                raise ValueError(
                    "Unable to identify a job description on this page."
                )

            return jd_text

        except Exception as e:

            raise ValueError(
                f"Unable to fetch URL content: {str(e)}"
            )