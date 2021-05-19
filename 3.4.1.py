import csv
import datetime
from datetime import datetime, date, time

crime_dict = {}
with open('test_3.4.1/Crimes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = datetime.strptime(row['Date'],  "%m/%d/%Y %H:%M:%S %p")
        if date.year == 2015:
            crime_type = row['Primary Type']
            if crime_type in crime_dict.keys():
                crime_dict[crime_type] = crime_dict[crime_type] + 1
            else:
                crime_dict[crime_type] = 0

print(crime_dict)
max_crime_type = ''
max_crime_type_value = max(crime_dict.values())
for key in crime_dict.keys():
    if crime_dict[key] == max_crime_type_value:
        max_crime_type = key
        break
print(max_crime_type)