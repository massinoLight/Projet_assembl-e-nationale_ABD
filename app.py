from distributed.http.utils import redirect
from flask import Flask, render_template, request, url_for, redirect
from datetime import  timedelta, datetime

from traitement.recherche_wiki import recherche_wikipedia
from traitement.scraping_google_images import _get_random_image

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







