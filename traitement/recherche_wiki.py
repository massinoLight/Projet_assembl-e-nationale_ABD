import wikipedia
import random
from pyspark.sql import SparkSession

from traitement.scraping_google_images import _get_random_image

spark = SparkSession.builder.appName('Spark').getOrCreate()
sparkContext=spark.sparkContext


def recherche_wikipedia(nom_prenom_depute):
    wikipedia.set_lang("fr")
    page_wiki = wikipedia.page(nom_prenom_depute)

    return page_wiki,filtrer_image(page_wiki.images,page_wiki.title)


def filtrer_image(images,motcle):
    rdd=sparkContext.parallelize(images)
    l=[]
    for i in range (0,len(rdd.collect())):
       if ("jpg"  in rdd.collect()[i])and \
               ((motcle.split(" ")[0] in rdd.collect()[i])or(motcle.split(" ")[1] in rdd.collect()[i])  ):
         l.append(rdd.collect()[i])
    if l:
      rdd2=sparkContext.parallelize(l)
      r1 = random.randint(0,len(l))
      return rdd2.collect()[r1]
    else :
        return _get_random_image(motcle)




