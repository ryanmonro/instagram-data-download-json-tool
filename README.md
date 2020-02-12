# Instagram Data Download JSON Tool

Exports photos and videos from Instagram Data Download data, reuniting them with the dates/times they were uploaded.

## Background

Since Facebook went into PR crisis mode in early 2018, they have introduced a number of features that allow you to 'download all your data', to dissuade people from thinking the company is collecting data about you and you'll never find out what it is. Enter the reassuringly named Data Download feature of Instagram.

One good thing to do with the photos in the Data Download is to upload them somewhere else, such as Google Photos, for safe keeping. Unfortunately, the metadata of all the photos is gone, and the file creation dates are set to whatever date you requested the Data Download. Which is useless. The download also contains a bunch of JSON files, one of which contains all the date/times of when the photos were uploaded through the Instagram app. 

This script outputs the photos with the date and caption in their EXIF data, and the videos are written with the correct modified date. Google Photos (and possible other photo managers) will recognise these as the dates of the photos/videos. Reunited and it feels so good.

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

Run the script, replacing `path` with the path to your folder containing media.json (ie `~/Downloads/markzuckerberg_part_2`:

Run the script, specifying the path:
`python instagram_data.py [path]`

It will spit out all the images and videos it can find. You can also specify an output folder, but that's optional.

My download came in three folders, and only folders 2 and 3 contained a media.json file. Your mileage may vary, especially if you posted more photos than I did.

## Problems?

Get in touch, I'd love this to be useful for everyone trying to make sense of their Instagram data.