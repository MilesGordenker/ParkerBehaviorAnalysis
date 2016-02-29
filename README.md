#ParkerBehaviorAnalysis
A python script I wrote for Passport published with the written consent of the CTO. The script can analyze 10.5 million transactions in under a minute using a Macbook Pro, and produce valuable insights that cannot be easily replicated using SQL queries due to the massive amount of data involved.

The algorithm runs in O(n) where n is the number of records being processed.

#Architecture

By Passport convention, all data is stored in ./CsvData, and all the analysis scripts in ./Analyses. To protect confidential information, I have removed everything but a usage sample (MilesAnalysis.py) and some dummy CSV data.

The complex components of the architecture were written using TDD methodologies. All unit tests may be found in ./srcTest.

##class UniqueParker

A representation of a single active parker in the Passport system. Dynamically keeps track of which zones the parker frequents, and can return useful stats about what percentage of the time they park in the most used zone without further computation.

##class ParkerList

Iterates through CSV parking records, constructing a hash table of UniqueParker instances so the data may be analyzed. I do simple outlier filtering by parker transaction and operator. 

In Passport's system, operators are specified by a unique numerical ID. Depending on the analysis, users may wish to restrict the analysis to a single zone, or exclude multiple zones of a cetain type. To avoid littering the code with unintelligible numbers, I provided for the use case with the ZoneFilter class. 

##class ZoneFilter

When passed to an instance of ParkerList during instantiation, the ZoneFilter instructs the ParkerList to ignore all parking transaction records that do not match the user-specified criteria. Currently only checks for certain operators, but can be easily extended using the embedded documentation.
