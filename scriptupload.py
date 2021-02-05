import boto3

s3 = boto3.resource("s3")
BUCKET = "ml-worksample"

s3.Bucket(BUCKET).upload_file("Testworksample.py", "Archivos utilitarios/Testworksample.py")
