
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.mllib.linalg import DenseVector
from pyspark.sql.types import Row
from pyspark.sql import SparkSession


def show_accuracy(predictions):
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    accuracy = evaluator.evaluate(predictions)
    print("Accuracy = {:.2f} %".format(accuracy*100))

spark= SparkSession.builder \
    .master("local") \
    .appName("Data Exploration") \
    .getOrCreate()



row = Row(label=0, features=DenseVector([1.0,0.0, 0.0]))

DTmodel = DecisionTreeClassifier.load("./models/DT")
print(DTmodel.setPredictionCol(row))
