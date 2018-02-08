import boto3
import cv2
import sys
import subprocess
from subprocess import call
import awscli

BUCKET="ersp-test-1"
KEY=sys.argv[1]


s3 = boto3.resource('s3')
s3.meta.client.upload_file(KEY, BUCKET, KEY)

img = cv2.imread(KEY)
propertics = img.shape

height=float(propertics[0])
width=float(propertics[1])

FEATURES_CHOOSELIST = ("BoundingBox")

textfileName = "result.txt"
sys.stdout = open(textfileName,'w')

def recognize_celebrities (bucket,key, attributes=['ALL'], region="us-east-2"):
	rekognition = boto3.client("rekognition",region)
	response = rekognition.recognize_celebrities(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
	#Attributes=attributes
	)
	return response['CelebrityFaces']
	#return response['FaceDetails']


print	KEY.strip(".jpg")

for face in recognize_celebrities(BUCKET,KEY):

	print "{Name}".format(**face)

	for feature, data in face.iteritems():
			if feature in FEATURES_CHOOSELIST:
				#print " Width: {data[Width]}".format(data=data)
				#print " Height: {data[Height]}".format(data=data)
				#print " Left: {data[Left]}".format(data=data)
				#print " Top: {data[Top]}".format(data=data)

		
				stringWidth = "{data[Width]}".format(data=data)
				WidthC = float(stringWidth)

				stringHeight = "{data[Height]}".format(data=data)
				HeightC = float(stringHeight)
				
				stringLeft = "{data[Left]}".format(data=data)
				LeftC = float(stringLeft)
	
				stringTop = "{data[Top]}".format(data=data)
				TopC = float(stringTop)

				borderLength = HeightC*height
				borderWidth = WidthC*width
				yLeft = TopC*height	#top and bottom left y coordinate
				xTop = LeftC*width	#top left and right x coordinate
				
				x = int(xTop)
				y = int(yLeft)
				x1 = int(xTop+borderLength)
				y1 = int(yLeft+borderWidth)

				img = cv2.rectangle(img, (x,y), (x1,y1),(0,255,0),3)
				cv2.imwrite(KEY,img)

print("\n")


