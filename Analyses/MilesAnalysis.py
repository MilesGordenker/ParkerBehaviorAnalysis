from ParkerList import ParkerList
from ZoneFilter import ZoneFilter
import time

csvDirectory = '../CsvData/'
oneYear = [csvDirectory + 'JAN.csv', csvDirectory + 'FEB.csv', csvDirectory + 'MAR.csv', csvDirectory + 'APR.csv',
           csvDirectory + 'MAY.csv', csvDirectory + 'JUN.csv', csvDirectory + 'JUL.csv', csvDirectory + 'AUG.csv',
           csvDirectory + 'SEP.csv']

def analyzeCsvForCities(filterArray, csvFiles):
    for message, filter in filterArray:
        print(message)
        parkerList = ParkerList(csvFiles, filter)
        print('Most times parked: ' + str(parkerList.mostTimesParked()))
        print('Parkers analyzed: ' + str(parkerList.parkersInTable()))
        print('Mode Zone Percentage for 5+ time parkers: ' + str(parkerList.avgModeZonePercentage(5,400)))
        print('Avg unique zones: ' + str(parkerList.avgUniqueZonesParked()))
        print('Avg unique zones for 33+ time parkers: ' + str(parkerList.uniqueZonesParkedForSubset(33,150)))
        print('Avg times parked: ' + str(parkerList.avgTimesParkedTotal()))

def main():
    stdCityFilter = ZoneFilter(True, True)
    stdCityTuple = ('Analyzing 2015s transactions outside many-zoned operators...\n', stdCityFilter)

    start_time = time.time()
    analyzeCsvForCities([stdCityTuple], oneYear)
    print("--- %s seconds ---" % (time.time() - start_time))


if  __name__ =='__main__':
    main()