import unittest
import jacoco_parser.parser as parser


class TestParser(unittest.TestCase):

    def test_calc_pct(self):
        self.assertEquals(parser.calc_pct("100", "200"), 50.0)

    def test_cal_pct_comma(self):
        self.assertEquals(parser.calc_pct("1,000", "2,000"), 50.0)

    def test_get_missed_total(self):
        self.assertEquals(parser.get_missed_total("10 of 20"), ("10", "20"))

    def test_get_missed_total_invalid(self):
        self.assertEquals(parser.get_missed_total("10"), ())

    if __name__ == '__main__':
        unittest.main()
