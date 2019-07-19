import unittest
from read_data_from_html import *
#from iterate_through_webpages import *

# works for the Record class, use generic obj_eq func later
def record_eq(record1, record2):
    if record1.freezing_level != record2.freezing_level:
        return False
    if record1.temp_at_900 != record2.temp_at_900:
        return False
    if record1.date_today != record2.date_today:
        return False
    if record1.area_id != record2.area_id:
        return False
    return True

# HTML reading tests
class HTMLReadTests(unittest.TestCase):
    # Test the function to get a list of ints from a string
    def test_get_int_from_string(self):
        self.assertEqual(get_ints_from_string('10C'), [10])
        self.assertEqual(get_ints_from_string('10 rising to 12C inland.'), [10, 12])

    def test_get_average_int(self):
        self.assertEqual(get_average_int([20, 30, 70]), 40)
        self.assertEqual(get_average_int([1, 5, 7]), 4)
        # This does not need to check for div by 0, as statistics lib mean()
        # will not work on empty list
        #with self.assertRaises(ZeroDivisionError):
        #   get_average_int([])
        #with self.assertRaises(TypeError):
        #    get_average_int(20, 30, 40)

    def test_strip_html_tags(self):
        html_line = '<div class="col-md-9"><p>Above the summits.</p></div>'
        html_line2 = '<div class="col-md-9"><p>Above<i> the</i> summits.</p></div>'
        self.assertEqual(strip_html_tags(html_line), 'Above the summits.')
        self.assertEqual(strip_html_tags(html_line2), 'Above the summits.')

    def test_create_record(self):
        # this needs to be online for urlopen to work
        # using live mwis - this test will need changing every day currently
        # need to make mock urlopen()
        #test_page = 'file://C:\Users\ruaridh.leary\Documents\winter_conditions_records\practice\TEST_forecast.html'
        test_page = 'http://www.mwis.org.uk/scottish-forecast/WH/'
        test_record = Record('Above the summits.', 9, date.today(), 'WH')
        self.assertIsInstance(create_record(test_page), Record)
        # Need to change this, assertEqual uses ==, on objects two instances are only equal
        # if they are the same object
        #self.assertEqual(create_record(test_page), test_record)
        self.assertTrue(record_eq(create_record(test_page), test_record))
        
if __name__ == '__main__':
    unittest.main()