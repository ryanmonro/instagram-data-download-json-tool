import sys
import os
import json
import piexif
import piexif.helper
from PIL import Image

if len(sys.argv) == 1:
	exit("Usage: exif [path/to/ig/data/download]")
path = sys.argv[1] + "/"
print("Using " + path)
try:
	fp = open(path + "/media.json")
except:
	exit("ERROR: media.json not found at path")
data = json.load(fp)
# for index in ['photos', 'videos']
try:
	photos = data['photos']
except KeyError:
	exit("ERROR: photos data not found in media.json")
found = 0
not_found = 0
index = 0
out_path = path + "/output/"
for photo in photos:
	try:
		image = Image.open(path + photo['path'])
		found += 1
		datetime = photo['taken_at'].replace('-', ':').replace('T', ' ')
		print(datetime)
		print(photo['path'])
		zeroth = {
			piexif.ImageIFD.DateTime: datetime
		}
		comment = piexif.helper.UserComment.dump(photo['caption'])
		exif = {
			piexif.ExifIFD.UserComment: comment
		}
		exif_dict = {"0th": zeroth, "Exif": exif}
		exif_bytes = piexif.dump(exif_dict)
		out_file = out_path + photo['path']
		os.makedirs(os.path.dirname(out_file), exist_ok=True)
		image.save(out_file, 'jpeg', exif=exif_bytes)
	except FileNotFoundError:
		not_found += 1
	index += 1
print("Written:", found, "photos")
print("Not found:", not_found, "photos")
print("Files available at", out_path)