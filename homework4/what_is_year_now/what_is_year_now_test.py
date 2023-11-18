from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch

class TestWhatYearIsNow(unittest.TestCase):
    @patch("json.load")
    def test_format_1(self, mock_load):
        year_now = 2023
        mock_load.return_value = {"currentDateTime": "2023-01-01"}
        obtained = what_is_year_now()
        self.assertEquals(obtained, year_now)


    @patch("json.load")
    def test_format_2(self, mock_load):
        year_now = 2023
        mock_load.return_value = {"currentDateTime": "05.11.2023"}
        obtained = what_is_year_now()
        self.assertEquals(obtained, year_now)

    @patch("urllib.request.urlopen")
    def test_response(self, mock_urlopen):
        self.assertNotEqual(mock_urlopen.getcode(), 404)

