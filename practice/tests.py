import unittest
from read_data_from_html import *

# HTML reading tests
class HTMLReadTests(unittest.TestCase):
    # Test the function to get a list of ints from a string
    def test_get_int_from_string(self):
        self.assertEqual(get_ints_from_string('10C'), [10])
        self.assertEqual(get_ints_from_string('10 rising to 12C inland.'), [10, 12])

    def test_get_average_int(self):
        self.assertEqual(get_average_int([20, 30, 70]), 40)
        self.assertEqual(get_average_int([1, 5, 7]), 4)
        # div 0, wrong type( eg av(1, 2, 3) - is not list)

    def test_strip_html(self):
        pass

    def test_get_temp_and_freezinf_level(self):
        # this needs to be online for urlopen to work
        # using live mwis - this test will need changing every day currently
        # test_page = 'TEST_forecast.html'
        test_page = 'http://www.mwis.org.uk/scottish-forecast/WH/'
        self.assertEqual(get_temp_and_freezing_level(test_page), ('Above the summits.', 10))
        get_temp_and_freezing_level(test_page)


unittest.main()