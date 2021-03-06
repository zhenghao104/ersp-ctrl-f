import boto3
import cv2

BUCKET="ersp-test-1"
KEY="output.jpg"

img = cv2.imread('output.jpg')
propertics = img.shape

height=float(propertics[0])
width=float(propertics[1])

FEATURES_CHOOSELIST = ("BoundingBox")

def detect_faces (bucket,key, attributes=['ALL'], region="us-east-2"):
	rekognition = boto3.client("rekognition",region)
	response = rekognition.detect_faces(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
	Attributes=attributes
	)
	return response['FaceDetails']

for face in detect_faces(BUCKET,KEY):

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
				cv2.imwrite("resultoutput.jpg",img)


