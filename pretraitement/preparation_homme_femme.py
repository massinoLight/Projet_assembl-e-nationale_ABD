import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit





spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()






df = spark.read.option("header",True) \
     .csv("../data/liste_deputes_collaborateurs.csv")



df.show()
df2=df.drop("collaborateur","nom_collaborateur","prénom_collaborateur","sexe_collaborateur","url_api_RC","information complémentaire")




df2.printSchema()
df2.show()


dropDisDF = df2.dropDuplicates(["parlementaire"])
dropDisDF.printSchema()
dropDisDF.show()

dropDisDF.toPandas().to_csv('../data/depute_homme_femme.csv',index=False)


