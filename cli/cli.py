from image import ImageOpener
from ocrapi import OCRAPI


class CLI:
    def __init__(self):
        self.image = ImageOpener()
        self.ocr_api = OCRAPI()

    async def ocr_local_file(self, path):
        image = await self.image.open_local_file(path)
        text = await self.ocr_api.image_to_string(image)
        print(text)
