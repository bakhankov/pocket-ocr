from aiohttp import web

from httpclient import HTTPClient
from ocrapi import OCRAPI
from image import ImageOpener


class WebApp(web.Application):
    def __init__(self):
        super().__init__()
        self.http_client = HTTPClient()
        self.ocr_api = OCRAPI()
        self.image = ImageOpener()

    async def ocr(self, request):
        data = await request.post()
        url = data.get('url')
        if not url:
            return web.HTTPError()

        source = await self.http_client.get(url)
        image = await self.image.open_from_bytes(source)
        text = await self.ocr_api.image_to_string(image)
        return web.Response(text=text)

    def run_app(self):
        self.router.add_post('/ocr', self.ocr)
        web.run_app(self)
