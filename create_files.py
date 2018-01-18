from srt_data import *
from image_data import *
from poi_data import *
import math

VIDEO_DISTANCE_RANGE=35
POI_DISTANCE_RANGE=50

def create_file_for_video():
	srt_coordinate_data=get_srt_data()
	video_times=srt_coordinate_data[0]
	video_latitudes=srt_coordinate_data[2]
	video_longitudes=srt_coordinate_data[3]
	
	image_coordinate_data=get_image_data()
	image_names=image_coordinate_data[0]
	image_latitudes=image_coordinate_data[1]
	image_longitudes=image_coordinate_data[2]
	
	fh = open("images_for_video.csv", "w")
	fh.write("Time(seconds),Image Names,\n")
	
	video_list_pos=0
	for time in video_times:
		#print("Time: ", time, "\tLatitude: ", video_latitudes[video_list_pos], "\t\tLongitude: ", video_longitudes[video_list_pos], "\n")
		time_seconds = time[6:-4]+"."+time[9:]
		fh.write(time_seconds+",")
		
		image_list_pos=0
		for name in image_names:
			if (video_latitudes[video_list_pos] == "None" or video_longitudes[video_list_pos] == "None" or image_latitudes[image_list_pos] == "None" or image_longitudes[image_list_pos] == "None"):
				image_list_pos += 1
				continue
			else:
				lat1=float(video_latitudes[video_list_pos]) #http://edwilliams.org/avform.htm#Dist
				lon1=float(video_longitudes[video_list_pos])
				lat2=float(image_latitudes[image_list_pos])
				lon2=float(image_longitudes[image_list_pos])
				distance=1852*((180*60)/math.pi)*2*math.asin(math.sqrt(math.pow(math.sin(math.radians((lat1-lat2)/2)),2) + math.cos(lat1)*math.cos(lat2)*math.pow(math.sin(math.radians((lon1-lon2)/2)),2)))

				if(distance<=VIDEO_DISTANCE_RANGE):
					fh.write(image_names[image_list_pos]+"; ")
					#print("Image: ", name, "\nLatitude: ", image_latitudes[image_list_pos], "\nLongitude: ", image_longitudes[image_list_pos],"\n")
				
			image_list_pos += 1
		video_list_pos += 1
		fh.write("\n")
		
	print("CSV file for geotagged images created.")
	fh.close()
	
#create_file_for_video() 

def create_file_for_poi():
	poi_coordinate_data=get_poi_data()
	poi_names=poi_coordinate_data[0]
	poi_latitudes=poi_coordinate_data[1]
	poi_longitudes=poi_coordinate_data[2]

	image_coordinate_data=get_image_data()
	image_names=image_coordinate_data[0]
	image_latitudes=image_coordinate_data[1]
	image_longitudes=image_coordinate_data[2]
	
	fh = open("images_for_poi.csv", "w")
	fh.write("Asset Name,Longitude,Latitude,Image Names,\n")
	
	poi_list_pos=0
	for asset_name in poi_names:
		#print("Name: ", asset_name, "\tLatitude: ", poi_latitudes[poi_list_pos], "\t\tLongitude: ", poi_longitudes[poi_list_pos], "\n")
		fh.write(asset_name+","+poi_latitudes[poi_list_pos]+","+poi_longitudes[poi_list_pos]+",")
		
		image_list_pos=0
		for name in image_names:
			if (poi_latitudes[poi_list_pos] == "None" or poi_longitudes[poi_list_pos] == "None" or image_latitudes[image_list_pos] == "None" or image_longitudes[image_list_pos] == "None"):
				image_list_pos += 1
				continue
			else:
				lat1=float(poi_latitudes[poi_list_pos]) #http://edwilliams.org/avform.htm#Dist
				lon1=float(poi_longitudes[poi_list_pos])
				lat2=float(image_latitudes[image_list_pos])
				lon2=float(image_longitudes[image_list_pos])
				distance=1852*((180*60)/math.pi)*2*math.asin(math.sqrt(math.pow(math.sin(math.radians((lat1-lat2)/2)),2) + math.cos(lat1)*math.cos(lat2)*math.pow(math.sin(math.radians((lon1-lon2)/2)),2)))
				
				#print(distance)
				if(distance<=POI_DISTANCE_RANGE):
					fh.write(image_names[image_list_pos]+"; ")
					#print("Image: ", name, "\nLatitude: ", image_latitudes[image_list_pos], "\nLongitude: ", image_longitudes[image_list_pos],"\n")
				
			image_list_pos += 1
		poi_list_pos += 1
		fh.write("\n")
	
	print("CSV file for points of interest created.")
	fh.close()

#create_file_for_poi()