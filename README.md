# Project: s3-upload-download-convert
## Description
This project includes functionality to upload and download files to/from an Amazon S3 bucket, as well as convert CSV files to Parquet format using Apache Spark. It is organized into several files and folders:

Root folder: s3-upload-download-convert
Files:
requirements.txt: Contains the list of Python packages required for this project.
main.py: Main Python script that uses classes from the src folder to interact with S3 and perform CSV to Parquet conversion.
README.md: Documentation file that provides instructions on how to use this project and best practices.
Folders:
src/: Contains Python modules with classes for S3 bucket interaction (interact_s3.py) and CSV to Parquet conversion using Spark (conversor.py).
Prerequisites
Before using this project, you need to set up your AWS credentials. Follow the steps below:

Log in to your AWS account.
Create an S3 bucket with a unique name, e.g., "datalake-my-lucas-bucket".
Note down the name of the S3 bucket, as it will be used in the main.py script.
Set up AWS credentials on your local machine using one of the following methods:
Option 1: AWS CLI - Run aws configure command in your terminal and provide the required AWS access key ID, secret access key, default region, and default output format.
Option 2: Environment variables - Set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, and AWS_DEFAULT_OUTPUT environment variables with your AWS credentials.
Usage
To use this project, follow the steps below:

Install the required Python packages listed in requirements.txt using pip or conda.
Update the bucket_name variable in main.py with the name of your S3 bucket created in the prerequisites step.
Run main.py script using Python to perform the following operations:
Download files from the S3 bucket to the local machine using BucketS3 class from interact_s3.py module.
Read CSV files using Spark and obtain Spark dataframes using Convert class from conversor.py module.
Convert Spark dataframes to Parquet format and save them to the specified path using Convert class from conversor.py module.
Note: Make sure you have the necessary permissions and valid credentials to perform operations on the S3 bucket.

Best Practices
Use appropriate error handling and logging in your code to handle exceptions and errors gracefully.
Follow the principle of least privilege while setting up AWS credentials, i.e., use IAM roles and policies to restrict permissions to the minimum necessary for the project.
Avoid hardcoding sensitive information like AWS access keys and secret access keys in your code. Use environment variables, AWS CLI, or other secure methods to store and access credentials.
Follow proper file organization and modularization of your code for better readability and maintainability.
Document your project with clear instructions on how to use, prerequisites, and best practices for future reference.
