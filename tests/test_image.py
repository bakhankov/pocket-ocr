import asyncio
from collections import namedtuple
from unittest import TestCase

from image import ImageOpener


class TestImageOpener(TestCase):
    def setUp(self):
        self.image_opener = ImageOpener()

    async def _test_open_local_file(self):
        Case = namedtuple('Case', ('path', 'info', 'format', 'size'))
        cases = [
            Case(path='tests/test_data/test_text_123.png',
                 info={'dpi': (96, 96)}, format='PNG', size=(200, 100)),
            Case(path='tests/test_data/TRansperent_987_654.png',
                 info={'dpi': (96, 96)}, format='PNG', size=(200, 100)),
        ]
        for case in cases:
            res = await self.image_opener.open_local_file(case.path)
            self.assertEqual(res.info, case.info)
            self.assertEqual(res.format, case.format)
            self.assertEqual(res.size, case.size)

    def test_all(self):
        asyncio.run(self._test_open_local_file())
