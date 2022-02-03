from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.ml.feature import StringIndexer
import pandas as pd
import os

######################################################################################
#                                                                                    #
#  On va transformer les donnée et les mettre sous forme vecteur                     #
#                                                                                    #
######################################################################################


df=pd.read_csv("../data/data_for_DT.csv")

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
finale=va_df.select("label","features")
finale.show()
finale.toPandas().to_csv('../data/dataVectorInvers_for_DT.csv',index=False)


va_df.toPandas().to_csv('../data/dataVector_for_DT.csv',index=False)

