import boto3
import pandas as pd
from pathlib import Path

class BucketS3:

    def __init__(self, name):
        '''
        Connecting to archive in s3 bucket.

            Parameters: 
                    name (string): The name of the bucket
                    archive (string): The location of the archive
        '''
        global s3_client
        s3_client = boto3.client('s3')
        self.bucket_name = name

    def download(self, s3_path, local_path):
        '''
        Downloading the archive from bucket to local path.

            Parameters: 
                local_path (string): Your path without the last ' / '
                name (string): The name of archive
                type (string): The type of the archive (csv, json, xml...)

            Returns: The file from S3 to your destination folder.
        '''
        try:
            s3_client.download_file(
                f'{self.bucket_name}', f'{s3_path}', f'{local_path}')
        except:
            print("Was not posible to download archive from bucket")

        return s3_client.download_file(f'{self.bucket_name}', f'{s3_path}', f'{local_path}')

    def upload(self, local_file_path, bucket_path):
        '''
        Upload archive from local path to s3 bucket.

        Parameters: 
                local_file_path (string) all file path (with archive)
                bucket (string): nme of the bucket s3
                bucket_path (string): destiny path of s3
                name (string): name of new archive on s3
                type (string): csv, json, xml...
        '''
        try:
            s3_client.upload_file(f'{local_file_path}',
                                  f'{self.bucket_name}', f'{bucket_path}')
        except:
            print("Was not posible to upload archive to bucket")

            return s3_client.upload_file(f'{local_file_path}', f'{self.bucket_name}', f'{bucket_path}')

    def csv_to_df(self, file_path):
        '''
        Open the archive (CSV) downloaded from s3 with a DF

        Parameter:         
            file_path (string): copy file path imported from s3
        '''
        return pd.read_csv(f'{file_path}', sep=';')

    def json_to_df(self, file_path):
        '''
        Open the archive (JSON) downloaded from s3 with a DF

        Parameter:         
            file_path (string): copy file path imported from s3
        '''
        return pd.read_json(f'{file_path}')