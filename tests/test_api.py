from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from httpapi import WebApp


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = WebApp()
        app.router.add_post('/ocr', app.ocr)
        return app

    @unittest_run_loop
    async def test_example(self):
        url = ('https://kstatic.googleusercontent.com/files/02fe41696f4d70ede1'
               '7ef81e30a81997cdbbf55e6e9c6c63fc2f1b3603854a676a7b17c89bda0d1f'
               'b2954a1cf7b7eea8cd60b00426be3ae7c79c578b6a12bf46')
        resp = await self.client.request("POST", "/ocr", data={'url': url})
        assert resp.status == 200
        text = await resp.text()
        assert text == 'Doodle for\n\nGoogle'
