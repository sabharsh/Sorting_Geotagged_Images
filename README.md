# Sorting_Geotagged_Images

## Introduction

This code performs to the following two main tasks:

1) Creates a CSV file that lists all the given geotagged images that fall with 35m of the drone path. The drone path was provided ina an SRT file format.

2) Creates a CSV file that lists all the given geotagged images that fall with 50m of the given points of interest.

## Requirements

There are two requirements to run this code. These requirements are as follow:

1) Install Python 3.6 from https://www.python.org/downloads/ (and adding it to the path to run code from command prompt for Windows)

2) Install Pillow by running the following command in command prompt/bash:
		
	pip install pillow
		
## Running the code

The code can be run simply by opening the directory containing the python files in command prompt/bash and running the following command:

	python main.py
		
This will create two files called "images_for_video.csv" and "images_for_poi.csv" which contains the appropriate data.
