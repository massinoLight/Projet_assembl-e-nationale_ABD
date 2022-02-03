

import pandas as pd
from nbconvert.preprocessors import Preprocessor
from pyspark import SparkContext, SQLContext
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml import Pipeline
from pyspark.sql import SparkSession

spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()

df = spark.read.option("header",True) \
     .csv("./data/dataVector_for_DT.csv")



df.show()
(trainingData, testData) = df.randomSplit([0.7, 0.3])

dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
pipeline = Pipeline(stages=[df.select("label"), df.select("features"), dt])

model = pipeline.fit(trainingData)



