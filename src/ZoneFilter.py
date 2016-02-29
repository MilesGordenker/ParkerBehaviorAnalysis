"""
Used to check whether a given zone matches certain criteria

When adding new categories to the ZoneFilter, be sure to:

add a new parameter
add a matching new internal variable
add a new method
add an if statement calling the new method to isZoneValid
"""

class ZoneFilter:

    def __init__(self, filterManyZoneOperators=False, filterTestOperators=True):
        self.filterManyZoneOperators = filterManyZoneOperators
        self.filterTestOperators = filterTestOperators
        self.onlyAllowImaginaryCity = False
        self.onlyAllowDummyCity = False
        self.onlyAllowFakeCity = False
        self.onlyAllowNotARealCity = False
        self.onlyAllowAtlantis = False
        self.onlyAllowEmeraldCity = False
        self.onlyAllowMordor= False
        self.onlyAllowKingsLanding = False
        self.onlyAllowCastamere = False
        self.onlyAllowOlympia = False

    # Checks operatorId against user preferences set during initialization
    def isOperatorValid(self, operatorId):
        if self.filterTestOperators:
            if operatorId in manyZoneList:
                return False

        if self.filterTestOperators:
            if operatorId in testOperatorList:
                return False

        if self.onlyAllowImaginaryCity:
            if operatorId == '64':
                return True

        if self.onlyAllowDummyCity:
            if operatorId == '212':
                return True

        if self.onlyAllowFakeCity:
            if operatorId == '225':
                return True

        if self.onlyAllowNotARealCity:
            if operatorId == '37':
                return True

        if self.onlyAllowAtlantis:
            if operatorId == '238':
                return True

        if self.onlyAllowEmeraldCity:
            if operatorId == '263':
                return True

        if self.onlyAllowMordor:
            if operatorId != '335':
                return True

        if self.onlyAllowKingsLanding:
            if operatorId == '396':
                return True

        if self.onlyAllowCastamere:
            if operatorId == '227':
                return True

        if self.onlyAllowOlympia:
            if operatorId == '284':
                return True

        #no more tests left
        return True



# ----------------------------- Operator Lists -----------------------------------

manyZoneList = [284, #Olympia
                212, #DummyCity
                64, #ParkImaginaryCity
                313 #Bingtown
                ]

testOperatorList = [9, #Alliance Parking
                    367, #CraigC Parking
                    71, #Divya
                    243, #Lucky Cache Reload
                    326, #zQA Operator
                    28 #zShannon Test Operator
                    ]


