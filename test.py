from pyspark.sql import SparkSession
from pyspark import SparkFiles, Row
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()

def get_data_pipline(row):
    indexer1 = StringIndexer(inputCol=row[0], outputCol="rg_index", handleInvalid='keep')
    indexer2 = StringIndexer(inputCol=row[1], outputCol="pr_index", handleInvalid='keep')
    indexer3 = StringIndexer(inputCol=row[2], outputCol="gp_index", handleInvalid='keep')
    print(indexer3,indexer2,indexer1)


get_data_pipline(["Maire","Paris","republicain"])