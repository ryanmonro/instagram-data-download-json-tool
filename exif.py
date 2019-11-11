import sys
import os
import json

if len(sys.argv) == 1:
	exit("Usage: exif [path/to/ig/data/download]")
path = sys.argv[1] + "/"
print("Using " + path)
try:
	fp = open(path + "/media.json")
except:
	exit("ERROR: media.json not found at path")
data = json.load(fp)
try:
	photos = data['photos']
except KeyError:
	exit("ERROR: photos data not found in media.json")
found = 0
not_found = 0
index = 0
for photo in photos:
	try:
		pfp = open(path + photo['path'])
		found += 1
		# os.system('chromium ' + path + photo['path'])
		# exit()
	except FileNotFoundError:
		print(index, " not found.")
		not_found += 1
	index += 1
print("Found: ", found, " photos")
print("Not found: ", not_found, "")