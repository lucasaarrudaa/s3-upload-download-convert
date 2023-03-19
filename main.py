from conversor import Convert
from interact_s3 import BucketS3

# Download from bucket to local
b1 = BucketS3('datalake-my-lucas-bucket')
b1.download('raw-data/MICRODADOS_ENEM_2020.csv',
            'DADOS/MICRODADOS_ENEM_2020.csv')

b2 = BucketS3('datalake-my-lucas-bucket')
b2.download('raw-data/ITENS_PROVA_2020.csv',
            'DADOS/ITENS_PROVA_2020.csv')

# Converting MICRODADOS_ENEM_2020 from csv to parquet
df1 = Convert()
df1.read_csv('DADOS\MICRODADOS_ENEM_2020.csv')
df1.csv_to_parquet('DADOS\MICRODADOS_ENEM_2020.parquet')

# # Converting ITENS_PROVA_2020 from csv to parquet
df2 = Convert()
df2.read_csv('DADOS\ITENS_PROVA_2020.csv')
df2.csv_to_parquet('DADOS\ITENS_PROVA_2020.parquet')
