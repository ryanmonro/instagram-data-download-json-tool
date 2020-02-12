import sys
import os
import time
import datetime
import json

if len(sys.argv) == 1:
	exit("Usage: python videos [path/to/ig/data/download]")
path = sys.argv[1] + "/"
print("Using " + path)
try:
	fp = open(path + "/media.json")
except:
	exit("ERROR: media.json not found at path")
data = json.load(fp)
try:
	videos = data['videos']
except KeyError:
	exit("ERROR: videos data not found in media.json")

found = 0
not_found = 0
# out_path = '~/instagram_videos/'
out_path = '~/Desktop/out/'
for video in videos:
	result = os.system('cp ' + path + video['path'] + ' ' + out_path)
	if result != 0:
		not_found += 1
		continue
	taken_at = video['taken_at']
	dt = datetime.datetime.strptime(taken_at, '%Y-%m-%dT%H:%M:%S')
	atime = time.time()
	mtime = dt.timestamp()
	filename = video['path'].split('/')[-1]
	filepath = os.path.expanduser(out_path) + filename
	print(filename)
	os.utime(filepath, (atime, mtime))
	found += 1

print("Written:", found, "photos")
print("Not found:", not_found, "photos")
print("Files available at", out_path)