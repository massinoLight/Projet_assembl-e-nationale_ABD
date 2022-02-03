from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
import pandas as pd

df=pd.read_csv("../data/data_for_DT.csv")

iris = load_iris()
df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['label'] = pd.Series(iris.target)

print(df_iris['label'])

sc = SparkContext().getOrCreate()
sqlContext = SQLContext(sc)

data = sqlContext.createDataFrame(df_iris)
print(data.printSchema())

print(type(data))
features = iris.feature_names
print(features)

va = VectorAssembler(inputCols = features, outputCol='features')

va_df = va.transform(data)
va_df = va_df.select(['features', 'label'])
va_df.show(3)

(train, test) = va_df.randomSplit([0.7, 0.3])

dtc = DecisionTreeClassifier(featuresCol="features", labelCol="label")
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



