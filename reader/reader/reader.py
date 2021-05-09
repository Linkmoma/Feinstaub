import csv
csv.list_dialects()
['excel', 'excel-tab', 'unix']

extra_list = [] 

reader = csv.reader(open("2021-04-26_dht22_sensor_3660.csv"), delimiter=";")
for row in reader:
    extra_list.append(row)
    print('Zeit', row[5], 'tempreatur:', row[6], 'C')
  
print('\nBonusaufgabe (Liste aus Liste ausgeben)','\n', extra_list)
