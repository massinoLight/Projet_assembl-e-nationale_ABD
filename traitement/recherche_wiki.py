import wikipedia
import random
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Spark').getOrCreate()
sparkContext=spark.sparkContext


def recherche_wikipedia(nom_prenom_depute):
    wikipedia.set_lang("fr")
    page_wiki = wikipedia.page(nom_prenom_depute)
    return page_wiki,filtrer_image(page_wiki.images)


def filtrer_image(images):
    rdd=sparkContext.parallelize(images)
    l=[]
    for i in range (0,len(rdd.collect())):
       if "jpg"  in rdd.collect()[i]:
         l.append(rdd.collect()[i])

    rdd2=sparkContext.parallelize(l)
    l=[]
    for i in range (0,len(rdd2.collect())):
      if "Macron"  in rdd.collect()[i]:
         l.append(rdd.collect()[i])

    rdd3=sparkContext.parallelize(l)
    r1 = random.randint(0,len(rdd3.collect()))
    return rdd3.collect()[r1]


resultat,image=recherche_wikipedia("Emmanuel Macron")

print(resultat.summary)
print(image)


