from aiohttp import ClientSession


class HTTPClient:
    def __init__(self):
        self.session = ClientSession()

    async def get(self, url):
        async with self.session.get(url) as response:
            return await response.read()
