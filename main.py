from src.conversor import Convert
from src.interact_s3 import BucketS3

bucket_name = "datalake-my-lucas-bucket"
s3_bucket = BucketS3(bucket_name)

# Download from bucket to local
a1 = s3_bucket.download("'raw-data/MICRODADOS_ENEM_2020.csv'", "DADOS/MICRODADOS_ENEM_2020.csv")
a2 = s3_bucket.download("raw-data/ITENS_PROVA_2020.csv", "DADOS/ITENS_PROVA_2020.csv")

convert = Convert(bucket_name)

# Reading a CSV file and obtaining a Spark dataframe
df1 = convert.spark_read_csv("DADOS/MICRODADOS_ENEM_2020.csv")
df2 = convert.spark_read_csv("cDADOS/ITENS_PROVA_2020.csv")
