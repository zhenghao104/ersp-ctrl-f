import boto3

BUCKET="ersp-test-1"
KEY="output.jpg"

FEATURES_CHOOSELIST= ("Name")

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

	print "{Name}".format(**face)
