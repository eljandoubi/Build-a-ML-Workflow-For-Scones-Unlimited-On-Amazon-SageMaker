"""
___________________________________________________________________________________________________________________________
serializeImageData
___________________________________________________________________________________________________________________________
"""

import json
import boto3
import base64


s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input (You may also check lambda test)
    key = event['s3_key']                               
    bucket = event['s3_bucket']                         
    
    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, "/tmp/image.png")
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:          
        image_data = base64.b64encode(f.read())      

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    
   
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }




"""
______________________________________________________________________________________________________________________________
Image-Classification
______________________________________________________________________________________________________________________________
"""

import json
import base64
import boto3


runtime_client = boto3.client('sagemaker-runtime')                   


# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-08-04-09-25-37-691"


def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])

    # Instantiate a Predictor
    response = runtime_client.invoke_endpoint(
                                        EndpointName=ENDPOINT,    
                                        Body=image,               
                                        ContentType='image/png'
                                    )
                                    
    
    # Make a prediction
    inferences = json.loads(response['Body'].read().decode('utf-8'))
  
    
    # We return the data back to the Step Function    
    event['inferences'] = inferences                        
    return {
        'statusCode': 200,
        'body': event
    }





"""
______________________________________________________________________________________________________________________________
Filter-Low-Confidence-Inferences
______________________________________________________________________________________________________________________________
"""

import json

THRESHOLD = 0.7


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    inferences = event['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = max(inferences)>THRESHOLD
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event
    }
    
    