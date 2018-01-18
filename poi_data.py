import csv
import re

#Returns names and coordinates of points on interest listed in the assets.csv
def get_poi_data():
	with open('assets.csv') as csvfile:
		asset_names=[]
		asset_longitudes=[]
		asset_latitudes=[]
		readCSV = csv.reader(csvfile, delimiter=',')
		first_line = True
		for row in readCSV:
			if (first_line):
				first_line = False
				continue
			asset_names.append(row[0])
			asset_longitudes.append(row[1])
			asset_latitudes.append(row[2])
		# for index in range(4):
			# print("asset:\t",     asset_names[index])
			# print("longitude:\t", asset_longitudes[index]) 
			# print("latitude:\t",  asset_latitudes[index]) 
			# print("\n")
	return [asset_names,asset_latitudes,asset_longitudes]
			
#get_poi_data()