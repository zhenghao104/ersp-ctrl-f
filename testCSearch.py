import boto3
import cv2
import sys

BUCKET=sys.argv[1]
KEY=sys.argv[3]
NAMESELECT=sys.argv[2]
outputname=sys.argv[4]

img = cv2.imread(KEY)
FEATURES_CHOOSELIST= ("Face")
propertics = img.shape

height=float(propertics[0])
width=float(propertics[1])

def recognize_celebrities(bucket,key, region="us-east-2"):
	rekognition = boto3.client("rekognition",region)
	response = rekognition.recognize_celebrities(
		Image={
                        "S3Object": {
                                "Bucket": bucket,
                                "Name": key,
                        }
                }
	)

	return response['CelebrityFaces']

for face in recognize_celebrities(BUCKET,KEY):

	
	namecheck = "{Name}".format(**face)


	if namecheck==NAMESELECT:
		for feature, data in face.iteritems():
			if feature in FEATURES_CHOOSELIST:
				stringWidth = "{data[BoundingBox][Width]}".format(data=data)
                                WidthC = float(stringWidth)

                                stringHeight = "{data[BoundingBox][Height]}".format(data=data)
                                HeightC = float(stringHeight)

                                stringLeft = "{data[BoundingBox][Left]}".format(data=data)
                                LeftC = float(stringLeft)

                                stringTop = "{data[BoundingBox][Top]}".format(data=data)
                                TopC = float(stringTop)

                                borderLength = HeightC*height
                                borderWidth = WidthC*width
                                yLeft = TopC*height     #top and bottom left y coordinate
                                xTop = LeftC*width      #top left and right x coordinate

                                x = int(xTop)
                                y = int(yLeft)
                                x1 = int(xTop+borderLength)
                                y1 = int(yLeft+borderWidth)
				
				print namecheck	#Only print if it is working				

                                img = cv2.rectangle(img, (x,y), (x1,y1),(0,255,0),3)
                                cv2.imwrite(outputname,img)	

