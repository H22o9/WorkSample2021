import boto3

s3 = boto3.resource("s3")
BUCKET = "ml-worksample"

s3.Bucket(BUCKET).download_file( "Archivos Utilitarios/Testworksample.py", "Testworksamplecopy.py",)