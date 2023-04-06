import boto3

class BucketS3:

    def __init__(self, bucket_name):
        '''
        Connects to the S3 bucket.
            Parameters: 
                    bucket_name (string): The name of the S3 bucket
        '''
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name

    def download(self, s3_path, local_path):
        '''
        Downloads a file from the bucket to a local path.
            Parameters: 
                s3_path (string): The path of the file in the bucket
                local_path (string): The destination local path
            Returns: The file from S3 to the local destination folder.
        '''
        try:
            self.s3_client.download_file(
                self.bucket_name, s3_path, local_path)
        except Exception as e:
            print(f"Failed to download file from the bucket: {e}")

    def upload(self, local_file_path, bucket_path):
        '''
        Uploads a file from a local path to the S3 bucket.
            Parameters: 
                local_file_path (string): The full path of the local file
                bucket_path (string): The destination path in the S3 bucket
        '''
        try:
            self.s3_client.upload_file(local_file_path, self.bucket_name, bucket_path)
        except Exception as e:
            print(f"Failed to upload file to the bucket: {e}")
