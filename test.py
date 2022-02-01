
import pandas as pd
from pyspark.sql import SparkSession

url = 'https://data.assemblee-nationale.fr/static/openData/repository/15/amo/deputes_actifs_csv_opendata/liste_deputes_libre_office.csv'


df=pd.read_csv(url)




spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()

SparkDF=spark.createDataFrame(df)
SparkDF.printSchema()
SparkDF.show()



