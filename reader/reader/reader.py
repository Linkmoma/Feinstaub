import csv
csv.list_dialects()
['excel', 'excel-tab', 'unix']


reader = csv.reader(open("2021-04-26_dht22_sensor_3660.csv"), delimiter=";")
for row in reader:
    print(row)
    ['sensor_id','sensor_type','location','lat','lon','timestamp','P1','durP1','ratioP1','P2','durP2','ratioP2']

reader = csv.reader(open("2021-04-26_sds011_sensor_3659.csv"), delimiter=";")
for row in reader:
    print(row)
    ['sensor_id','sensor_type','location','lat','lon','timestamp','P1','durP1','ratioP1','P2','durP2','ratioP2']
