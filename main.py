from src.conversor import Convert
from src.interact_s3 import BucketS3

# Download from bucket to local
b1 = BucketS3('datalake-my-lucas-bucket')
b1.download('raw-data/MICRODADOS_ENEM_2020.csv',
            'DADOS/MICRODADOS_ENEM_2020.csv')

b2 = BucketS3('datalake-my-lucas-bucket')
b2.download('raw-data/ITENS_PROVA_2020.csv',
            'DADOS/ITENS_PROVA_2020.csv')

# Converting from csv to parquet
df1 = Convert()
df1.spark_read_csv('data\MICRODADOS_ENEM_2020.csv')
df1.spark_csv_to_parquet('s3-upload-download-convert\staging\enem\microdados')

df2 = Convert()
df2.spark_read_csv('data\ITENS_PROVA_2020.csv')
df2.spark_csv_to_parquet('s3-upload-download-convert\staging\enem\itens_prova')



