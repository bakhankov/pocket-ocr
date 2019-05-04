import asyncio
from collections import namedtuple
from unittest import TestCase

from cli import CLI


class TestCLI(TestCase):
    def setUp(self):
        self.cli = CLI()

    async def _test_ocr_local_file(self):
        Case = namedtuple('Case', ('path', 'text'))
        cases = [
            Case(path='tests/test_data/test_text_123.png',
                 text='Test Text 123'),
            Case(path='tests/test_data/TRansperent_987_654.png',
                 text='TRansperent\n987 654'),
        ]
        for case in cases:
            res = await self.cli.ocr_local_file(case.path)
            self.assertEqual(res, case.text)

    def test_all(self):
        asyncio.run(self._test_ocr_local_file())
