from flask import Flask, render_template, request
from traitement.stat_on_data import count_homme_femme, count_groupe_politique, count_region, get_page_depute
from traitement.recherche_wiki import recherche_wikipedia
import random

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer
from pyspark.ml.classification import  DecisionTreeClassificationModel
from pyspark.ml.linalg import Vectors
from pyspark.ml import Pipeline


def get_predicion(row):
    spark = SparkSession.builder \
        .master("local") \
        .appName("Data Exploration") \
        .getOrCreate()
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

    test0 = data.collect()[random.randint(0, 1129)]

    t = spark.createDataFrame([(Vectors.dense(test0[1][0], test0[1][1], test0[1][2]),)], ["features"])
    t.show()
    return DTmodel.predict(t.head().features)

def rand_color(T):
  for i in range(0, T):
    color = []
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    color.append(hex_number)
  return color


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['motcle'] !="":
            resultat, image = recherche_wikipedia(request.form['motcle'] )
            page=get_page_depute(request.form['motcle'] )
            return render_template('resultat_Recherche.html', acteur=resultat.title,wiki=resultat.summary,img=image,page=page)
    return render_template('main.html')






@app.route('/contact')
def contact():
    return render_template('contact.html')




@app.route('/ia', methods=["GET", "POST"])
def IA():
    if request.method == 'POST':
            predict= get_predicion("")
            print(predict)
            if predict==1.0:
               return render_template('maybe.html')
            else :
               return render_template('no.html')
    return render_template('IA.html')


@app.route('/stat')
def stat():
    groupepolitique=[]
    membre=[]
    region=[]
    count=[]

    hommes,femmes=count_homme_femme()
    df=count_groupe_politique()
    for i in range(0,len(df.collect())):
        if df.collect()[i][0] == None:
            groupepolitique.append("inconnu")
        else:
            groupepolitique.append(df.collect()[i][0])
        membre.append(df.collect()[i][1])

    df=count_region()
    for i in range(0,len(df.collect())):
        region.append(df.collect()[i][0])
        count.append(df.collect()[i][1])


    return render_template('stat.html',homme=hommes,femme=femmes,values=membre,labels=groupepolitique,region=region,count=count)
