import unittest
import main

class TestStockVisualizer(unittest.TestCase):

    def test_symbol_returnsOK_ifUpper_and_lenBetween1And7_and_isAlpha(self):
        self.assertEqual(main.isTickerSymbolUpper('GME'), 'GME')
        self.assertEqual(main.isTickerSymbolUpper('gme'), 'GME')
        self.assertEqual(main.isTickerSymbolLengthValid('A'), True)
        self.assertEqual(main.isTickerSymbolLengthValid('AAAAAAA'), True)
        self.assertEqual(main.isTickerSymbolLengthValid('AAAAAAAAAAA'), False)
        self.assertEqual(main.isTickerSymbolLengthValid(''), False)
        self.assertEqual(main.isTickerSymbolAlpha('AAA'), True)
        self.assertEqual(main.isTickerSymbolAlpha('GME'), True)
        self.assertEqual(main.isTickerSymbolAlpha('123'), False)
        self.assertEqual(main.isTickerSymbolAlpha('1AB'), False)

    def test_isChartValid_returnsOK_ifNot1Or2(self):
        self.assertEqual(main.isChartValid(1), False)
        self.assertEqual(main.isChartValid(2), False)
        self.assertEqual(main.isChartValid(3), True)
        self.assertEqual(main.isChartValid(-2), True)

    def test_time_series_returnsOK_ifNot123Or4(self):
        self.assertEqual(main.isTimeSeriesValid(1), False)
        self.assertEqual(main.isTimeSeriesValid(2), False)
        self.assertEqual(main.isTimeSeriesValid(0), True)
        self.assertEqual(main.isTimeSeriesValid(-1), True)

    def test_start_date(self):
        self.assertEqual(main.validate('2021-02-01'), True)
        self.assertEqual(main.validate('2022-03-04'), True)
        self.assertEqual(main.validate('02-03-2021'), False)
        self.assertEqual(main.validate('11/17/1998'), False)


    def test_end_date(self):
        self.assertEqual(main.validate('2021-02-01'), True)
        self.assertEqual(main.validate('2022-03-04'), True)
        self.assertEqual(main.validate('02-03-2021'), False)
        self.assertEqual(main.validate('11/17/1998'), False)

if __name__ == "__main__":
    unittest.main()
