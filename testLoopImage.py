import os 
import boto3
import cv2
import sys 
import subprocess
from subprocess import call

foldercheck=sys.argv[1]	#Folder of images to loop through
folderpath = foldercheck + "/"
for filename in os.listdir(foldercheck): 
	if filename.endswith(".jpg"):
		newfilename = "new_" + filename
		#call(["python testCSearch.py ersp-test-1 'Benedict Wong'", folderpath+filename, folderpath+newfilename])
