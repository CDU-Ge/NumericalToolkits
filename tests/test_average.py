# -*- coding: utf-8 -*-
import unittest


class StatisticsCase(unittest.TestCase):
    def test_average(self):
        from NumericalToolkits import Average
        average1 = Average()
        for i in range(100):
            average1 += i
        print(average1)
        average2 = Average()
        for i in range(50):
            average2 -= i
        print(average2)
        print(average1 + average2 )
        print(average1 - average2)


if __name__ == '__main__':
    unittest.main()
