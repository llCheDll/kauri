import json
from src import parser

from FakeResponse import FakeResponse
from unittest.mock import patch
from unittest import TestCase


class JsonTest(TestCase):
    def test_json_parser(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value = FakeResponse()

            with open('../resources/data.json', 'r') as file:
                fake_data = json.loads(file.read())

            url = parser.BASE_URL.format(parser.URI)
            self.assertEqual(parser.json_parser(url), fake_data)
