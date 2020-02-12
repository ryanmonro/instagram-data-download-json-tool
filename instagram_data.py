import sys
import os
import json
import datetime
import time
import piexif
import piexif.helper
from PIL import Image

# Get input path
if len(sys.argv) == 1:
	exit("Usage: python instagram_data path/to/ig/data/download [output_path]")
path = os.path.join(sys.argv[1], "")
print("Using " + path + " as input path")

# Get output path if specified
out_path = "~/instagram_data/"
if len(sys.argv) == 3:
	out_path = os.path.join(sys.argv[2], "")
out_path = os.path.expanduser(out_path)
os.makedirs(os.path.dirname(out_path), exist_ok=True)

# Open media.json if available
try:
	fp = open(path + "/media.json")
except:
	exit("ERROR: media.json not found at path")
data = json.load(fp)

# Work through indices of media.json
for index in data:
	print("Processing " + index + "...")
	found = 0
	not_found = 0
	entries = data[index]
	for entry in entries:
		# get attributes from JSON
		caption = entry.get('caption', '')
		taken_at = entry['taken_at'].split('.')[0]
		file_path = entry['path']
		filename = file_path.split('/')[-1]
		extension = filename.split('.')[-1]
		dt = datetime.datetime.strptime(taken_at, '%Y-%m-%dT%H:%M:%S')
		atime = time.time()
		mtime = dt.timestamp()
		input_file_path = os.path.join(path, file_path)
		output_file_path = os.path.join(out_path, index, filename)
		os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
		if extension == "mp4":
			# if a video, copy the file
			result = os.system('cp ' + input_file_path + ' ' + output_file_path)
			if result != 0:
				not_found += 1
				continue
		elif extension == "jpg":
			# if a photo, open it, add EXIF data, write to new location
			try:
				image = Image.open(input_file_path)
				exif_dt = taken_at.replace('-', ':').replace('T', ' ')
				zeroth = {
					piexif.ImageIFD.DateTime: exif_dt
				}
				comment = piexif.helper.UserComment.dump(caption)
				exif = {
					piexif.ExifIFD.UserComment: comment
				}
				exif_dict = {"0th": zeroth, "Exif": exif}
				exif_bytes = piexif.dump(exif_dict)
				image.save(output_file_path, 'jpeg', exif=exif_bytes)
			except FileNotFoundError:
				not_found += 1
				continue
		# change access/modified dates of new file
		os.utime(output_file_path, (atime, mtime))
		found += 1
	print("Written:", found)
	print("Not found:", not_found)
	
print("Files available at", out_path)