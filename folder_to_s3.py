from pathlib import Path
import os
import glob
import boto3

def upload_dir(localDir, awsInitDir, bucketName, prefix='/'):
    """
    from current working directory, upload a 'localDir' with all its subcontents (files and subdirectories...)
    to a aws bucket
    Parameters:
            localDir :   localDirectory to be uploaded, with respect to current working directory
            awsInitDir : prefix 'directory' in aws
            bucketName : bucket in aws
            tag :        tag to select files, like *png
                        NOTE: if you use tag it must be given like --tag '*txt', in some quotation marks... for argparse
            prefix :     to remove initial '/' from file names

    Returns: None
    """
    s3 = boto3.resource('s3')
    cwd = str(Path.cwd())
    p = Path(os.path.join(Path.cwd(), localDir))
    mydirs = list(p.glob('**'))
    for mydir in mydirs:
        fileNames = glob.glob(os.path.join(mydir))
        fileNames = [f for f in fileNames if not Path(f).is_dir()]
        rows = len(fileNames)
        for i, fileName in enumerate(fileNames):
            fileName = str(fileName).replace(cwd, '')
            if fileName.startswith(prefix):  # only modify the text if it starts with the prefix
                fileName = fileName.replace(prefix, "", 1) # remove one instance of prefix
            print(f"fileName {fileName}")

            awsPath = os.path.join(awsInitDir, str(fileName))
            s3.meta.client.upload_file(fileName, bucketName, awsPath)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--localDir", help="which dir to upload to aws")
    parser.add_argument("--bucketName", help="to which bucket to upload in aws")
    parser.add_argument("--awsInitDir", help="to which 'directory' in aws")
    args = parser.parse_args()

    