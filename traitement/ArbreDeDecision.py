
from pyspark.sql import SparkSession
from pyspark import SparkFiles
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator



spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()

df = spark.read.options(delimiter=",", header=True, inferSchema=True).csv("./data/data_for_DT.csv")

def show_accuracy(predictions):
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Accuracy = {:.2f} %".format(accuracy*100))


df.show(5)
indexer1 = StringIndexer(inputCol=df.columns[0], outputCol="rg_index", handleInvalid='keep')
indexer2 = StringIndexer(inputCol=df.columns[1], outputCol="pr_index", handleInvalid='keep')
indexer3 = StringIndexer(inputCol=df.columns[2], outputCol="gp_index", handleInvalid='keep')
pipeline = Pipeline(stages=[indexer1, indexer2, indexer3])
data = pipeline.fit(df).transform(df)
data = VectorAssembler(inputCols=["rg_index","pr_index","gp_index"], outputCol="features").transform(data).select('label','features')

data.show(5)



# Split the data into training and test sets (30% held out for testing)
(trainingData, testData) = data.randomSplit([0.7, 0.3])


dtree = DecisionTreeClassifier(maxDepth=5, impurity='gini', maxBins=280)
model = dtree.fit(trainingData)
predictions = model.transform(testData)

show_accuracy(predictions)

