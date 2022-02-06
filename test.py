import random

from pyspark.ml import pipeline
from pyspark.sql import SparkSession
from pyspark import SparkFiles, Row
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer
from pyspark.ml.classification import  DecisionTreeClassificationModel
from pyspark.ml.linalg import Vectors
from pyspark.ml import Pipeline
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()

def get_data_pipline(row):
    data2 = [(row[0], row[1], row[2])]

    schema = StructType([ \
        StructField("Région", StringType(), True), \
        StructField("Profession", StringType(), True), \
        StructField("Groupe politique (complet)", StringType(), True) \
        ])

    df = spark.createDataFrame(data=data2, schema=schema)
    df.show()
    indexer1 = StringIndexer(inputCol=df.columns[0], outputCol="rg_index", handleInvalid='keep')
    indexer2 = StringIndexer(inputCol=df.columns[1], outputCol="pr_index", handleInvalid='keep')
    indexer3 = StringIndexer(inputCol=df.columns[2], outputCol="gp_index", handleInvalid='keep')
    pipeline = Pipeline(stages=[indexer1, indexer2, indexer3])
    data = pipeline.fit(df).transform(df)
    data = VectorAssembler(inputCols=["rg_index", "pr_index", "gp_index"], outputCol="features").transform(data)
    data.show()




def get_predicion(row):

    df = spark.read.options(delimiter=",", header=True, inferSchema=True).csv("./data/data_for_DT.csv")

    indexer1 = StringIndexer(inputCol=df.columns[0], outputCol="rg_index", handleInvalid='keep')
    indexer2 = StringIndexer(inputCol=df.columns[1], outputCol="pr_index", handleInvalid='keep')
    indexer3 = StringIndexer(inputCol=df.columns[2], outputCol="gp_index", handleInvalid='keep')
    pipeline = Pipeline(stages=[indexer1, indexer2, indexer3])
    data = pipeline.fit(df).transform(df)

    data = VectorAssembler(inputCols=["rg_index", "pr_index", "gp_index"], outputCol="features").transform(data).select(
        'label', 'features')

    DTmodel = DecisionTreeClassificationModel.load(
        "/home/massino/Bureau/projetAssembleNationale/new/Projet_assemble_nationale_ABD/traitement/models/DT")

    test0=data.collect()[random.randint(0, 1129)]


    t = spark.createDataFrame([(Vectors.dense(test0[1][0],test0[1][1],test0[1][2]),)], ["features"])
    t.show()
    return DTmodel.predict(t.head().features)



