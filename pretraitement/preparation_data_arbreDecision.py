import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


######################################################################################
#                                                                                    #
#  On va injecter des données pour aider a entrainer le modéle d'arbre de décision   #
#                                                                                    #
######################################################################################

spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()


profession_non_autorise = ['Maire', 'membre du Parlement européen', 'président établissement public',
                       'vice-président établissement public ','président de conseil départemental','vice-président de conseil départemental',
                       'président de conseil régional','vice-président de conseil régional',
                       'président syndicat mixte','vice-président syndicat mixte','','autre']
region_non_autorise = ['UE','Etranger','etranger','ue','autre']
GroupePolitique_non_autorise = ['','','Les Républicains','Agir ensemble','autre']
columns = ['Région','Profession','Groupe politique (complet)','depute']

df = spark.read.option("header",True) \
     .csv("../data/liste_deputes_libre_office.csv")


print(type(df.schema))
df.show()
df2=df.drop("identifiant","Prénom","Nom","Département","Numéro de circonscription","Groupe politique (abrégé)")
df2=df2.withColumn("depute", lit(1))

for i in range(0,40):
    newRow = spark.createDataFrame([(profession_non_autorise[random.randint(0,len(profession_non_autorise)-1)],
                                     region_non_autorise[random.randint(0,len(region_non_autorise)-1)],
                                     GroupePolitique_non_autorise[random.randint(0,len(GroupePolitique_non_autorise)-1)],0)], columns)

    df2=df2.union(newRow)

#df2=df2.withColumn("bonus_percent", lit(1))
df2.printSchema()
df2.show()
#df2.write.csv("../data/data_for_DT.csv")


df2.toPandas().to_csv('../data/data_for_DT.csv',index=False)
