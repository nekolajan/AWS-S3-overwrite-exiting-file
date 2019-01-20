import boto3

KEY_ID = ''
ACCESS_KEY = ''
bucket_name =''
file_name =''

s3 = boto3.resource(
    's3',
    aws_access_key_id= KEY_ID,
    aws_secret_access_key= ACCESS_KEY
)
content="Text in the body of the txt file."
s3.Object(bucket_name, file_name).put(Body=content)
