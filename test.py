from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from sklearn.metrics import confusion_matrix
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.ml.feature import StringIndexer
import pandas as pd

df=pd.read_csv("./data/data_for_DT.csv")
print(df.head())
columns = ['Région','Profession','Groupe politique (complet)','label']


schema = StructType([ \
    StructField("Région",StringType(),False), \
    StructField("Profession",StringType(),False), \
    StructField("Groupe politique (complet)",StringType(),False), \
    StructField("label", IntegerType(), False) \
  ])

sc = SparkContext().getOrCreate()
sqlContext = SQLContext(sc)

data = sqlContext.createDataFrame(data=df,schema=schema)
print(data.printSchema())

data.show()


Region_indexer = StringIndexer(inputCol="Région", outputCol="Regionindex")
data = Region_indexer.fit(data).transform(data)

Profession_indexer = StringIndexer(inputCol="Profession", outputCol="Professionindex")
data = Profession_indexer.fit(data).transform(data)

Groupe_indexer = StringIndexer(inputCol="Groupe politique (complet)", outputCol="GPindex")
data = Groupe_indexer.fit(data).transform(data)
data.show()

va = VectorAssembler(inputCols = ['Regionindex','Professionindex','GPindex'], outputCol='features')

va_df = va.transform(data)
va_df = va_df.select(['features', 'label'])
va_df.show()

(train, test) = va_df.randomSplit([0.8, 0.2])
print(type(train))


"""
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

"""