from pyspark.sql import *

class Convert:
    '''
    Converts CSV to Parquet.
    '''
    def __init__(self):
        '''
        Connect to spark.
        '''
        global spark
        spark = SparkSession.builder.getOrCreate()

    def read_csv(self, path_to_file_csv, sep=';'):
        '''
        Read csv file and attribute returns a DF
        '''
        self.df = spark.read.option("delimiter", f'{sep}').csv(path_to_file_csv)
        return self.df
    
    def csv_to_parquet(self, path):
        '''
        converting...
        Parameters: path (string) path of your converted archive
        Returns: new parquet archive
        '''
        parquet = self.df.write.parquet(f"{path}")
        return parquet
    