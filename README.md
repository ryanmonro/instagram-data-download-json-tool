# Instagram Data Download JSON Tool

Exports photos and videos from Instagram Data Download data, reuniting them with the dates/times they were uploaded.

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

You can also specify an output folder, but that's optional.

The script will copy all the images and videos it can find. They will have a `modified date` according to the `taken_at` attribute in the JSON file, and photos will also have dates and captions added to their EXIF data. 

My download came in three folders, and only folders 2 and 3 contained a media.json file. Your mileage may vary, especially if you posted more photos than I did.

As far as I can tell, any posts that are 'not found' are ones that you've deleted from inside the app. Instagram handily reminds you that they once existed, but reassuringly doesn't give you a copy of the thing you deleted.

## Problems?

Get in touch, I'd love this to be useful for everyone trying to make sense of their Instagram data.