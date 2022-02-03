
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.ml.feature import StringIndexer
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from sklearn.metrics import confusion_matrix
from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils

import pandas as pd



df=pd.read_csv("../data/dataVector_for_DT.csv")
sc = SparkContext().getOrCreate()
sqlContext = SQLContext(sc)
data = sqlContext.createDataFrame(data=df)


data.show()


(train, test) = data.randomSplit([0.7, 0.3])




dtc = DecisionTreeClassifier(featuresCol="features", labelCol="label",impurity='gini', maxDepth=5, maxBins=32)
dtc = dtc.fit(train)

"""
model = DecisionTree.trainClassifier(train, numClasses=2, categoricalFeaturesInfo={},
                                         impurity='gini', maxDepth=5, maxBins=32)


dtc = dtc.fit(train)

pred = dtc.transform(test)
pred.show(3)

evaluator = MulticlassClassificationEvaluator(predictionCol="prediction")
acc = evaluator.evaluate(pred)

print("Prediction Accuracy: ", acc)

y_pred = pred.select("prediction").collect()
y_orig = pred.select("label").collect()

cm = confusion_matrix(y_orig, y_pred)
print("Confusion Matrix:")
print(cm)

sc.stop()
"""
