__author__ = 'Miles Gordenker'

import unittest
from ParkerList import ParkerList

"""
Notes on the dataset used for testing

3 parkers qualify by having more than one transaction, of those 2 parked in the same spot over 90% of time
"""

list = ParkerList(['../../CsvData/parkerList_dummyData.csv'])

class ParkerListTest(unittest.TestCase):

    def test_number_of_parkers_correct(self):
        self.assertEqual(len(list.table), 4)

    def test_avg_percentage_correct(self):
        self.assertEqual(list.avgModeZonePercentage(), 75)

    def test_avgTimesParkedTotal(self):
        self.assertEqual(list.avgTimesParkedTotal(), 2.5)

    def test_avgUniqueZones(self):
        self.assertEqual(list.avgUniqueZonesParked(), 1.5)

    def test_uniqueZonesParkedForSubset(self):
        self.assertEqual(list.uniqueZonesParkedForSubset(2), 1.5)

    def test_mostTimesParked(self):
        self.assertEqual(list.mostTimesParked(), 'ParkerID 4 with 4 sessions')

    def test_UniqueParker_percentagePaidWith(self):
        parker1 = list.table['1']
        self.assertEqual(parker1.percentagePaidWithCard(), 100)
        self.assertEqual(parker1.percentagePaidWithZoneCash(), 0) # Check for false positives
        self.assertEqual(parker1.percentagePaidWithValidation(), 0)
        self.assertEqual(parker1.percentagePaidWithPaypal(), 0)
        self.assertEqual(parker1.percentagePaidWithFree(), 0)
        parker2 = list.table['2']
        self.assertEqual(parker2.percentagePaidWithCard(), 50)
        self.assertEqual(parker2.percentagePaidWithZoneCash(), 50)
        parker3 = list.table['3']
        self.assertEqual(parker3.percentagePaidWithPaypal(), 100)
        parker4 = list.table['4']
        self.assertEqual(parker4.percentagePaidWithZoneCash(), 50)
        self.assertEqual(parker4.percentagePaidWithValidation(), 25)
        self.assertEqual(parker4.percentagePaidWithFree(), 25)

    def test_paymentMethodPercentage(self):
        self.assertEqual(list.avgCardPaymentPercentage(), 37.5)


if __name__ == '__main__':
    unittest.main();