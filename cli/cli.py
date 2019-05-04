from image import ImageOpener
from ocrapi import OCRAPI


class CLI:
    def __init__(self):
        self.image = ImageOpener()
        self.ocr_api = OCRAPI()

    async def ocr_local_file(self, path):
        image = await self.image.open_local_file(path)
        return await self.ocr_api.image_to_string(image)

    async def print_local_file(self, path):
        print(await self.ocr_local_file(path))
