from pyspark import SparkContext, SparkConf


#conf = SparkConf().setAppName("appName").setMaster(local[0])
sc = SparkContext()

data = sc.textFile("../data/liste_deputes_libre_office.csv")
data.collect()