from agents.agent2_jd_parser.url_processor import URLProcessor

url = input("Enter URL: ")

text = URLProcessor.extract_text(url)

print(text[:5000])