from pyspark.sql import SparkSession
from src.interact_s3 import BucketS3


class Convert():
    '''
    Converts CSV to Parquet.
    '''

    def __init__(self):
        '''
        Connect to spark.
        '''
        self.spark = SparkSession.builder.appName('spark').getOrCreate()

    def spark_read_csv(self, path_to_file_csv, sep=';'):
        '''
        Read csv file and attribute
        '''
        self.enem = (
            self.spark
            .read
            .format("csv")
            .option("header", True)
            .option("inferSchema", True)
            .option("delimiter", f"{sep}")
            .load(f"{path_to_file_csv}")
        )
        return self.enem

    def spark_csv_to_parquet(self, path):
        '''
        converting...
        bucket-name: name of s3 bucket
        Parameters: path (string) path of your converted archive
        Returns: new parquet archive
        '''
        self.parquet = (
            self.enem
            .write
            .mode("overwrite")
            .format("parquet")
            .partitionBy("year")
            .save(f"{path}.csv")
        )
        return self.parquet
