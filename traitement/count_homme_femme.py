
from pyspark.sql.functions import countDistinct, count, col
from pyspark.sql import SparkSession


def count_homme_femme():
    spark = SparkSession.builder \
        .master("local") \
        .appName("Data Exploration") \
        .getOrCreate()

    df = spark.read.option("header",True) \
     .csv("./data/depute_homme_femme.csv")

    df2=df.groupBy('sexe_parlementaire').count()
    femmes=df2.select("count").collect()[0][0]
    hommes=df2.select("count").collect()[1][0]
    return hommes,femmes

