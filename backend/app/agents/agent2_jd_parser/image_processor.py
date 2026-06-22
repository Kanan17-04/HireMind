import pytesseract
from PIL import Image
class ImageProcessor:
    @staticmethod
    def image_to_text(file_path: str):
        image = Image.open(file_path)
        text = pytesseract.image_to_string(
            image
        )
        return text.strip()