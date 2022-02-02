from pyspark.sql import SparkSession




spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()


df2 = spark.read.option("header",True) \
     .csv("../data/liste_deputes_libre_office.csv")

print(type(df2))
df2.printSchema()
df2.show()