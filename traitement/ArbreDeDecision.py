from pyspark.mllib.linalg import DenseVector
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
def get_data_pipline():
    df = spark.read.options(delimiter=",", header=True, inferSchema=True).csv("../data/data_for_DT.csv")

    indexer1 = StringIndexer(inputCol=df.columns[0], outputCol="rg_index", handleInvalid='keep')
    indexer2 = StringIndexer(inputCol=df.columns[1], outputCol="pr_index", handleInvalid='keep')
    indexer3 = StringIndexer(inputCol=df.columns[2], outputCol="gp_index", handleInvalid='keep')
    pipeline = Pipeline(stages=[indexer1, indexer2, indexer3])
    data = pipeline.fit(df).transform(df)
    data = VectorAssembler(inputCols=["rg_index","pr_index","gp_index"], outputCol="features").transform(data).select('label','features')


    (trainingData, testData) = data.randomSplit([0.7, 0.3])
    return trainingData,testData

def show_accuracy(predictions):
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Accuracy = {:.2f} %".format(accuracy*100))



trainingData,testData=get_data_pipline()

testData.show(5)
print(type(testData))
print(testData.collect()[0])
print(type(testData.collect()[0]))
dtree = DecisionTreeClassifier(maxDepth=5, impurity='gini', maxBins=280)
model = dtree.fit(trainingData)
predictions = model.transform(testData)

show_accuracy(predictions)

#model.save("./models/DT")
print("model saved")

