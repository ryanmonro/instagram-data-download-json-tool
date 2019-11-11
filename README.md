# Instagram Data Download JSON Tool

Restores the date and time of photos downloaded from Instagram using the Data Download too.

## Background

Since Facebook went into PR crisis mode in early 2018, they have introduced a number of features that allow you to 'download all your data', to dissuade people from thinking the company is collecting data about you and you'll never find out what it is. Enter the reassuringly named Data Download feature of Instagram.

One good thing to do with the photos in the Data Download is to upload them to Google Photos, for safe keeping. Unfortunately, the metadata of all the photos is gone, and the file creation dates are set to whatever date you requested the Data Download. Which is useless. The download also contains a bunch of JSON files, one of which contains all the date/times of when the photos were uploaded through the Instagram app. 

This script reunites the photos with their long-lost date/times. It also puts the photo caption in the EXIF User Comment field, but Google Photos ignores this.

Coming soon: a solution for the video files.

## Installation

Install Python 3.

Create a virtual environment for the tool's packages:

`python3 -m venv venv`

Activate the virtual environment:

`source venv/bin/activate`

Install the packages:

`pip install -r requirements.txt`

## Usage

Activate the virtual environment (if you haven't already) as above.

Run the script, replacing `path` with the path to your folder containing media.json and the photos folder (ie `~/Downloads/ryanmonro_part_2`ß:

`python tool.py [path]`

It should spit out the images, in a new folder.