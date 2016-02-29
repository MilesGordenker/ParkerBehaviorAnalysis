__author__ = 'Miles Gordenker'


class UniqueParker:

    def __init__(self, firstZoneRecord):
        # Hashtable backed. Zone numbers map to an integer of times parked
        # Ex: Zone 101 has been parked in 3 times. {101, 3}
        self.table = dict()
        self.table[firstZoneRecord] = 1

        # Class variables used for cheap calculations of what % of time user parked in mode zone
        self.currentMostCommonZone = firstZoneRecord
        self.timesParkedInMostCommonZone = 1
        self.timesParkedTotal = 1

        # Cheap calculations of what method user parked with
        self.timesPaidWithCard = 0
        self.timesPaidWithZoneCash = 0
        self.timesPaidWithValidation = 0
        self.timesPaidWithFree = 0
        self.timesPaidWithPayPal = 0

    def addZoneParked(self, zone):
        self.timesParkedTotal += 1

        if zone in self.table:
            # previous records indicate parker has used this zone before
            currentTimesParkedInZone = self.table.get(zone) + 1
            assert currentTimesParkedInZone <= currentTimesParkedInZone
            self.table[zone] = currentTimesParkedInZone

            if currentTimesParkedInZone > self.timesParkedInMostCommonZone:
                # We have a new most common zone!
                self.currentMostCommonZone = zone
                self.timesParkedInMostCommonZone = currentTimesParkedInZone

        else:
            # first time records indicate the parker using this zone
            self.table[zone] = 1

    def modeZonePercentage(self):
        # Returns the % time parker used the most common zone
        return self.__convertToPercentage__(self.timesParkedInMostCommonZone, self.timesParkedTotal)

    def percentagePaidWithCard(self):
        return self.__convertToPercentage__(self.timesPaidWithCard, self.timesParkedTotal)

    def percentagePaidWithZoneCash(self):
        return self.__convertToPercentage__(self.timesPaidWithZoneCash, self.timesParkedTotal)

    def percentagePaidWithValidation(self):
        return self.__convertToPercentage__(self.timesPaidWithValidation, self.timesParkedTotal)

    def percentagePaidWithPaypal(self):
        return self.__convertToPercentage__(self.timesPaidWithPayPal, self.timesParkedTotal)

    def percentagePaidWithFree(self):
        return self.__convertToPercentage__(self.timesPaidWithFree, self.timesParkedTotal)

    def uniqueZonesParked(self):
        return len(self.table)

    def logPaymentMethod(self, billingtype, billingtype_id):
        # Breaking naming conventions here so I can put in exact column name
        if billingtype=='Credit/Debit Card' and billingtype_id == '1':
            self.timesPaidWithCard += 1
            return

        if billingtype=="Zone Cash" and billingtype_id=='2':
            self.timesPaidWithZoneCash += 1
            return

        if billingtype=='Validation' and billingtype_id=='3':
            self.timesPaidWithValidation += 1
            return

        # Database does not contain payment methods corresponding with ID 4 or 5

        if billingtype=='Paypal' and billingtype_id=='5':
            self.timesPaidWithPayPal += 1
            return

        if billingtype=='Free' and billingtype_id=='6':
            self.timesPaidWithFree += 1
            return

        raise SystemError("billingtype does not match billingtype_id")

    def __convertToPercentage__(self, dividend, divisor):
        rawPercentage = float(dividend/divisor)
        roundedPercentage =round(rawPercentage, 2)
        return roundedPercentage*100

    def __str__(self):
        print('Declared mode zone %: ' + str(self.modeZonePercentage()))
        for key, timesParked in self.table.items():
            print('Zone: ' + str(key) + ' Times Parked: ' + str(timesParked))
        return ''