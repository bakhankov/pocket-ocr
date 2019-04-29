import pytesseract


class OCRAPI:
    @staticmethod
    async def image_to_string(image, **kwargs):
        return pytesseract.image_to_string(image, **kwargs)
