import pandas as pd
import googlemaps
import csv


f = open('clustering.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
data = []
for line in rdr:
    data.append(line)
f.close()   
address = []
googlemaps_key = "AIzaSyCAAhXyRQ4sQneyM-tI_YM4Echx8j7x3PY"
gmaps = googlemaps.Client(key=googlemaps_key)
for i in range(len(data)) :
    reverse_geocode_result = gmaps.reverse_geocode((float(data[i][1]), float(data[i][0])), language='ko')
    address.append(reverse_geocode_result[1]['formatted_address'])

with open("clustering_address.csv", "w") as f:
    for i in range(len(address)):
        f.write(address[i]+"\n")