from pyspark.sql import SparkSession
import pandas as pd

class Convert(BucketS3):
    '''
    Converts CSV files to Parquet using Spark.
    '''

    def __init__(self, bucket_name):
        '''
        Connects to Spark and S3 bucket.
            Parameters: 
                bucket_name (string): The name of the S3 bucket
        '''
        super().__init__(bucket_name)
        self.spark = SparkSession.builder.appName('spark').getOrCreate()

    def spark_read_csv(self, path_to_file_csv, sep=';'):
        '''
        Reads the CSV file and assigns it to the Spark dataframe.
            Parameters:
                path_to_file_csv (string): The full path of the CSV file
                sep (string): The delimiter used in the CSV file (default is ';')
            Returns: The Spark dataframe with the read CSV file
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
        Converts the Spark dataframe to Parquet format and saves it to the specified path.
            Parameters:
                path (string): The destination path for the Parquet file
        '''
        self.enem_parquet = (
            self.enem.
            write.mode("overwrite")
            .format("parquet")
            .partitionBy("year")
            .save(f"{path}.parquet")
        )
        return self.enem_parquet
