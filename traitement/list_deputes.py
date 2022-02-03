from pyparsing import col
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit





spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()


df = spark.read.option("header",True) \
     .csv("../data/liste_deputes_libre_office.csv")


df.printSchema()
df.show()
df2=df.drop("identifiant","Prénom","Nom","Département","Numéro de circonscription","Groupe politique (abrégé)")
df2=df2.withColumn("bonus_percent", lit(1))
#df2=df2.withColumn("bonus_percent", lit(1))
df2.printSchema()
df2.show()
