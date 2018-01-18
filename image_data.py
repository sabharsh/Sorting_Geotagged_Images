from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import glob
import re

#Helper that returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags
def _get_exif_data(image):
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value

    return exif_data

#Helper that returns values of 
def _get_if_exist(data, key):
	return data.get(key, None)
	
#Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
def _convert_to_degress(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

#Helper that returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
def _get_lat_lon(exif_data):
    lat = None
    lon = None

    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]

        gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = _convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat

            lon = _convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return lat, lon

#Returns the image names, latitudes and longitudes for all the .JPG images contained in the images directory
def get_image_data():
	image_list = glob.glob("images\*.JPG")
	image_names=[]
	image_latitudes=[]
	image_longitudes=[]
	#print (image_list)
	for image_path in image_list:
		image_names.append(str(image_path)[7:])
		image = Image.open(str(image_path))#("images/DJI_0004.JPG")	# image.show()
		exif_data = _get_exif_data(image)
		coordinates= re.split(",",str(_get_lat_lon(exif_data)))
		#print (_get_lat_lon(exif_data))
		image_latitudes.append(str(coordinates[0])[1:])
		image_longitudes.append(str(coordinates[1])[1:-1])
		
	# i=0
	# for image_path in image_list:
		# print (image_names[i], image_latitudes[i], image_longitudes[i])
		# i += 1
	return [image_names, image_latitudes, image_longitudes]
	
#get_image_data()