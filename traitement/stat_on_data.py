
from pyspark.sql.functions import countDistinct, count, col
from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .master("local") \
        .appName("Data Exploration") \
        .getOrCreate()

def count_homme_femme():


    df = spark.read.option("header",True) \
     .csv("./data/depute_homme_femme.csv")

    df2=df.groupBy('sexe_parlementaire').count()
    femmes=df2.select("count").collect()[0][0]
    hommes=df2.select("count").collect()[1][0]
    return hommes,femmes



def count_groupe_politique():

    df = spark.read.option("header",True) \
     .csv("./data/liste_deputes_libre_office.csv")
    return df.groupBy('Groupe politique (complet)').count()




def count_region():

    df = spark.read.option("header",True) \
     .csv("./data/liste_deputes_libre_office.csv")
    return df.groupBy('Région').count()




def get_page_depute(motcle):

    df = spark.read.option("header",True) \
     .csv("./data/depute_homme_femme.csv")
    return df.filter(df.parlementaire == motcle).collect()[0][4]


