__author__ = 'Miles Gordenker'

import csv
from UniqueParker import UniqueParker
from ZoneFilter import ZoneFilter
import sys

"""
When fed an iterable record of Passport parking  transactions, builds a dictionary of Unique Parkers.
Transactions from certain operators may be ignored by passing a ZoneFilter object
Also contains some handy helper methods for making the analysis easier.
"""

OUTLIER_IF_SESSIONS_EXCEED = 400 # Constant to help filter out test users with lots of sessions. TODO: improve filtering

class ParkerList:

    def __init__(self, csvFiles, filter=ZoneFilter(filterManyZoneOperators=False, filterTestOperators=True)):

        # Hashtable backed. Parker ID maps to a UniqueParker instance generated from CSV
        self.table = dict()
        
        # Variables for stat calculations
        self.totalZonesParked = 0
        self.totalParkingSessions = -0
        self.mostParkingSessions = -1
        self.mostFrequentParkerId = ''

        # payment method calculations
        self.totalCardTransactions = 0
        self.totalZoneCashTransactions = 0
        self.totalPaypalTransactions = 0
        self.totalValidationTransactions = 0
        self.totalFreeTransactions = 0

        # Loop through all the files received to fill the ParkerList with UniqueParkers
        for pathToCsv in csvFiles:
            csvFile = open(pathToCsv, newline='')
            reader = csv.DictReader(csvFile, delimiter=',')
            for transaction in reader:
                #reject data that will skew analysis
                operatorIdForRecord = transaction['operator_id']
                if not filter.isOperatorValid(operatorIdForRecord):
                    continue

                #Datum is valid, add to table
                parkerIdForRecord = transaction['parker_id']
                zoneForRecord = transaction['zone_id']
                billingtypeForRecord = transaction['billingtype']
                billingtypeIdForRecord = transaction['billingtype_id']

                if parkerIdForRecord in self.table:
                    #TODO: check how many times this parker has used the system and remove outliers
                    #TODO: Outliers should be replaced withs some blank data
                    # we previously built a UniqueParker instance for this customer
                    parker = self.table[parkerIdForRecord]
                    parker.addZoneParked(zoneForRecord)
                    parker.logPaymentMethod(billingtypeForRecord, billingtypeIdForRecord)
                else:
                    # This parker has not yet appeared in the records. Add a UniqueParker
                    newParker = UniqueParker(zoneForRecord)
                    newParker.logPaymentMethod(billingtypeForRecord, billingtypeIdForRecord)
                self.table[parkerIdForRecord] = newParker

    # Method that iterates through the table gathering stats for multiple methods
    def gatherParkerStats(self):
        for key, parker in self.table.items():
            self.totalParkingSessions += parker.timesParkedTotal
            self.totalZonesParked += parker.uniqueZonesParked()

            # most Parking sessions
            if parker.timesParkedTotal > self.mostParkingSessions:
                self.mostParkingSessions = parker.timesParkedTotal
                self.mostFrequentParkerId = key

            # payment methods
            self.totalCardTransactions += parker.percentagePaidWithCard()
            self.totalZoneCashTransactions += parker.percentagePaidWithZoneCash()
            self.totalPaypalTransactions += parker.percentagePaidWithValidation()
            self.totalFreeTransactions += parker.percentagePaidWithFree()
            self.totalFreeTransactions += parker.percentagePaidWithValidation()


    # % of the time the average parker uses their most frequently visited zone
    def avgModeZonePercentage(self, userParkedAtLeastXTimes=2, userParkedAtMostYTimes=OUTLIER_IF_SESSIONS_EXCEED):
        percentagesSummmed = 0
        qualifyingParkersInTable = 0 # we don't care about parkers who don't meet conditions

        for key, parker in self.table.items():
            # filter out everyone who parked less than x times or more than Y times
            if userParkedAtLeastXTimes > parker.timesParkedTotal or parker.timesParkedTotal > userParkedAtMostYTimes:
                continue
            qualifyingParkersInTable += 1
            percentagesSummmed += parker.modeZonePercentage()

        return percentagesSummmed/qualifyingParkersInTable

    def uniqueZonesParkedForSubset(self, userParkedAtLeastXTimes, userParkedAtMostYTimes=OUTLIER_IF_SESSIONS_EXCEED ):
        uniqueZonesTotal = 0
        qualifyingParkersInTable = 0 # we don't care about parkers who don't meet conditions

        for key, parker in self.table.items():
            # filter out everyone who parked less than x times or more than Y times
            if userParkedAtLeastXTimes >= parker.timesParkedTotal or parker.timesParkedTotal > userParkedAtMostYTimes:
                continue
            qualifyingParkersInTable += 1
            uniqueZonesTotal += parker.uniqueZonesParked()

        return uniqueZonesTotal/qualifyingParkersInTable

    # How many different zones the average parker has used
    def avgUniqueZonesParked(self):
        if self.totalZonesParked == 0:
            self.gatherParkerStats()
        return self.totalZonesParked / self.parkersInTable()

    def avgTimesParkedTotal(self):
        if self.totalParkingSessions == 0:
            self.gatherParkerStats()
        return self.totalParkingSessions / self.parkersInTable()

    def mostTimesParked(self):
        if self.mostParkingSessions == -1:
            self.gatherParkerStats()
        return 'ParkerID {} with {} sessions'.format(self.mostFrequentParkerId, self.mostParkingSessions)

    def parkersInTable(self):
        return len(self.table)

    # returns percentage of transactions paid for with a credit card
    def avgCardPaymentPercentage(self):
        if self.totalCardTransactions == 0:
            self.gatherParkerStats()
        return self.totalCardTransactions / self.parkersInTable()


def main():
    targetData = ParkerList('../CsvData/6mo All Transactions minus ImaginaryCity etc.csv')
    print(targetData.avgModeZonePercentage())


if  __name__ =='__main__':
    main()