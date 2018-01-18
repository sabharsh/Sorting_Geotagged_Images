import csv
import re

#Returns the time of the video in seconds and coordinates of the drone provided in DJI_0301.SRT
def get_srt_data():
	with open('videos\DJI_0301.SRT') as csvfile:
		count=0
		start_times=[]
		end_times=[]
		latitudes=[]
		longitudes=[]
		readCSV = csv.reader(csvfile, delimiter=' ')
		for row in readCSV:
			count += 1
			if (count%4 == 2):
				#print(row[0],row[2])
				start_times.append(row[0])
				end_times.append(row[2])
			elif (count%4 == 3):
				coordinates = re.split(',',str(row)[2:-2])
				longitudes.append(coordinates[0])
				latitudes.append(coordinates[1])
		# for index in range(int(count/4)):
			# print("time:\t",   str(start_times[index]), "\t", str(end_times[index]))
			# print("coord.:\t", (str(latitudes[index])), "\t", str(longitudes[index])) 
			# print("\n")
	return [start_times, end_times, latitudes, longitudes]
			
#get_srt_data()