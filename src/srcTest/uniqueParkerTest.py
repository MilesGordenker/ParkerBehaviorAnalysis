import unittest
from UniqueParker import UniqueParker

class UniqueParkerTest(unittest.TestCase):

    def test_unique_zones(self):
        parker = UniqueParker(101)
        parker.addZoneParked(200)
        parker.addZoneParked(300)
        parker.addZoneParked(400)
        self.assertEqual(parker.currentMostCommonZone, 101);
        self.assertEqual(parker.timesParkedTotal, 4)
        self.assertEqual(parker.timesParkedInMostCommonZone, 1)

    def test_first_zone_common(self):
        parker = UniqueParker(101)
        parker.addZoneParked(101)
        parker.addZoneParked(200)
        parker.addZoneParked(300)
        parker.addZoneParked(400)
        self.assertEqual(parker.currentMostCommonZone, 101)

    def test_multiple_shifts(self):
        parker = UniqueParker(101)
        # Make 202 the most common zone
        parker.addZoneParked(202)
        parker.addZoneParked(202)
        # make 303 the most common zone
        parker.addZoneParked(303)
        parker.addZoneParked(303)
        parker.addZoneParked(303)
        self.assertEqual(parker.currentMostCommonZone, 303)
        self.assertEqual(parker.timesParkedInMostCommonZone, 3)

    def test_shifts_backNForth(self):
        parker = UniqueParker(101)
        # Make 202 the most common zone
        parker.addZoneParked(202)
        parker.addZoneParked(202)
        # make 303 the most common zone
        parker.addZoneParked(303)
        parker.addZoneParked(303)
        parker.addZoneParked(303)
        # make 101 the most common again
        parker.addZoneParked(101)
        parker.addZoneParked(101)
        parker.addZoneParked(101)
        self.assertEqual(parker.currentMostCommonZone,101)
        self.assertEqual(parker.timesParkedInMostCommonZone, 4)
        # aaaand back to 202
        parker.addZoneParked(202)
        parker.addZoneParked(202)
        parker.addZoneParked(202)
        self.assertEqual(parker.currentMostCommonZone, 202)
        self.assertEqual(parker.timesParkedInMostCommonZone, 5)
        self.assertEqual(parker.timesParkedTotal, 12)
        self.assertEqual(parker.modeZonePercentage(), 42)

    def test_percentage_share(self):
        parker = UniqueParker(1)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        self.assertEqual(parker.modeZonePercentage(), 75)

    def test_rounded_percentage(self):
        parker = UniqueParker(1)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        self.assertEqual(parker.modeZonePercentage(), 67)

    def test_uniqueZoneCount(self):
        parker = UniqueParker(1)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(3)
        parker.addZoneParked(4)
        parker.addZoneParked(5)
        self.assertEqual(parker.uniqueZonesParked(), 5)

    def test_prettyPrint(self):
        parker = UniqueParker(1)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(2)
        parker.addZoneParked(3)
        parker.addZoneParked(4)
        parker.addZoneParked(5)
        print(parker)


if __name__ == '__main__':
    unittest.main();