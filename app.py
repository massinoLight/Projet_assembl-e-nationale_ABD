from flask import Flask, render_template, request

from traitement.count_homme_femme import count_homme_femme
from traitement.recherche_wiki import recherche_wikipedia
from pyspark.ml.classification import  DecisionTreeClassificationModel
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession


def get_predicion(row):
    spark = SparkSession.builder \
        .master("local") \
        .appName("Data Exploration") \
        .getOrCreate()
    test0 = spark.createDataFrame([(Vectors.dense(row[0], row[1], row[2]),)], ["features"])
    DTmodel = DecisionTreeClassificationModel.load(
        "/home/massino/Bureau/projetAssembleNationale/new/Projet_assemble_nationale_ABD/traitement/models/DT")
    print("model load")
    print(DTmodel.toDebugString)

    return DTmodel.predict(test0.head().features)



app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if request.form['motcle'] !="":
            resultat, image = recherche_wikipedia(request.form['motcle'] )
            return render_template('resultat_Recherche.html', acteur=resultat.title,wiki=resultat.summary,img=image)
    return render_template('main.html')






@app.route('/contact')
def contact():
    return render_template('contact.html')




@app.route('/ia')
def IA():
    return render_template('IA.html')


@app.route('/stat')
def stat():
    hommes,femmes=count_homme_femme()
    return render_template('stat.html',homme=hommes,femme=femmes)
