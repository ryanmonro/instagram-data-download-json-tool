import sys
import os
import json
import datetime
import time
import piexif
import piexif.helper
from PIL import Image

def create_dir(name):
	if name in dirs:
		return
	if os.path.exists(os.path.expanduser(out_path + name)):
		return
	os.system("mkdir " + out_path + name)
	dirs.append(name)


out_path = "~/instagram_data/"
if len(sys.argv) == 1:
	exit("Usage: exif [path/to/ig/data/download]")
path = sys.argv[1] + "/"
print("Using " + path + " as input path")
if len(sys.argv) == 3:
	out_path = sys.argv[2] + "/"
out_path = os.path.expanduser(out_path)
if not os.path.exists(out_path):
	os.system("mkdir " + out_path)
try:
	fp = open(path + "/media.json")
except:
	exit("ERROR: media.json not found at path")
data = json.load(fp)
dirs = []
for index in data:
	print("Processing " + index + "...")
	found = 0
	not_found = 0
	entries = data[index]
	for entry in entries:
		try:
			create_dir(index)
			file_path = entry['path']
			taken_at = entry['taken_at'].split('.')[0]
			try:
				caption = entry['caption']
			except KeyError:
				caption = ""
			filename = file_path.split('/')[-1]
			extension = filename.split('.')[-1]
			if extension == "mp4":
				result = os.system('cp ' + path + file_path + ' ' + out_path + "/" + index)
				if result != 0:
					not_found += 1
					continue
				dt = datetime.datetime.strptime(taken_at, '%Y-%m-%dT%H:%M:%S')
				atime = time.time()
				mtime = dt.timestamp()
				output_file_path = os.path.expanduser(out_path) + index + "/" + filename
				# print(filename, dt)
				os.utime(output_file_path, (atime, mtime))
				found += 1
			elif extension == "jpg":
				try:
					image = Image.open(path + file_path)
					found += 1
					dt = taken_at.replace('-', ':').replace('T', ' ')
					zeroth = {
						piexif.ImageIFD.DateTime: dt
					}
					comment = piexif.helper.UserComment.dump(caption)
					exif = {
						piexif.ExifIFD.UserComment: comment
					}
					exif_dict = {"0th": zeroth, "Exif": exif}
					exif_bytes = piexif.dump(exif_dict)
					out_file = out_path + index + "/" + filename
					os.makedirs(os.path.dirname(out_file), exist_ok=True)
					image.save(out_file, 'jpeg', exif=exif_bytes)
				except FileNotFoundError:
					not_found += 1
		except KeyError:
			continue
	print("Written:", found)
	print("Not found:", not_found)
	
print("Files available at", out_path)