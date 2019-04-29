from io import BytesIO

import aiofiles
from PIL import Image


class ImageOpener:
    @staticmethod
    async def open_from_bytes(source):
        return Image.open(BytesIO(source))

    async def open_local_file(self, path):
        async with aiofiles.open(path, 'rb') as source:
            return await self.open_from_bytes(await source.read())
