# Description du Projet :
Ce projet a pour objectif de traiter les données de l’assemblée nationale 
proposéés par le gouvernement afin d’en tirer des conclusions intéressantes.
et d'y appliquer des methodes de ML ceci a l'aide de PySpark.

![alt text](https://databricks.com/wp-content/uploads/2018/12/PySpark-1024x164.png)




[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://spark.apache.org/docs/latest/api/python/)


# Jeux de données:
Données disponibles sur open data
[Source]
##Jeux1:
Ce jeu rassemble, pour les députés dont le mandat est actif au moment de la consultation,

- les données relatives à leur état civil  (noms, prénoms, dates et lieux de naissance, professions) ainsi que les numéros de téléphone, adresses postales et électroniques;

- les organes parlementaires  dont  ces députés sont membres  
- (Conférence des Présidents,  Bureau,  commissions, missions, délégations, office, comité, commissions mixtes paritaires, groupes d’amitié et d’étude et groupes politiques) 
- ainsi que les nominations à des assemblées parlementaires internationales et à des organismes extra-parlementaires où l’Assemblée nationale est représentée ;

- le rattachement des députés à un parti politique

- les collaborateurs par député.

source:[Députés en exercice]

##Jeux 2: 

Ce jeu comprend les données relatives à l’état civil 
des députés et anciens députés élus à partir du début de 
la XIème législature en juin 1997, à leur appartenance aux 
organes parlementaires, aux assemblées parlementaires 
internationales et à des organismes extra-parlementaires où 
l’Assemblée nationale est représentée 
ainsi que leur  rattachement à un parti politique. 

[Historique des députés]

##Jeux 3:

Ce jeu rassemble l’ensemble des questions posées au 
Gouvernement ainsi que les réponses de ce dernier lors des séances publiques 
dédiées les mardis et mercredis depuis le début de la quinzième législature 
(juin 2017). 
Ces données sont disponibles en format XML et JSON.

[Questions posées au gouvernement ]






## Tech & Plugins

pour l'utilisation de notre projet requiert une instalation préalable de certain outils (la majorité open source)

- [PySpark ] - Librérie python pour le traitement distribué!
- [Wikipedia] - l'API proposée par wikipedi utilisée pour faire du scraping!
- [Flask] -micro framework pour le déploiment de l'application
- [Selenium] -API utilisé pour faire du scraping d'image sur le web

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation



```sh
cd votre repertoire
pip install 
clear
```

For production environments...

```sh
$ export FLASK_APP=application.py
$ export FLASK_ENV=development
$ flask run
```







## Déploiement en local 

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   
   [PySpark ]: <https://spark.apache.org/docs/latest/api/python/#>
   [Wikipedia]: <https://pypi.org/project/Wikipedia-API/>
   [Flask]: <https://flask.palletsprojects.com/en/2.0.x/>
   [Selenium]: <https://selenium-python.readthedocs.io/>
  [Députés en exercice]:<https://data.assemblee-nationale.fr/static/openData/repository/15/amo/deputes_actifs_csv_opendata/liste_deputes_libre_office.csv>
  [Historique des députés]:<https://data.assemblee-nationale.fr/static/openData/repository/15/amo/tous_acteurs_mandats_organes_xi_legislature/AMO30_tous_acteurs_tous_mandats_tous_organes_historique.json.zip>
   [Questions posées au gouvernement ]:<https://data.assemblee-nationale.fr/static/openData/repository/15/questions/questions_gouvernement/Questions_gouvernement_XV.json.zip>
  [Source]:<https://data.assemblee-nationale.fr/>
