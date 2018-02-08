import os 
import boto3
import cv2
import sys 
import subprocess
from subprocess import call

#foldercheck=sys.argv[1]	#Folder of images to loop through
#folderpath = './' + foldercheck + "/"
#newfolderpath = "./processed_images/"
for filename in os.listdir("."):
	if filename.endswith(".jpg"):
		call(["python", "testCSearch.py", "ersp-test-1", '"Benedict Wong"', filename, filename])
