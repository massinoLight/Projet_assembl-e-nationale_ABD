from pyspark.sql import SparkSession




spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()


df2 = spark.read.option("header",True) \
     .csv("/home/massino/Bureau/projetAssembleNationale/Projet_assembl-e-nationale_ABD/data/liste_deputes_libre_office.csv")

df2.printSchema()
df2.show()