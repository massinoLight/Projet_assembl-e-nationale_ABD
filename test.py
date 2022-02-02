
import wikipedia
import random

wikipedia.set_lang("fr")

def recherche(nom_prenom_depute):
    page_wiki = wikipedia.page(nom_prenom_depute)
    print(page_wiki.summary)
    print(page_wiki.url)
    n = random.randint(3, len(page_wiki.images))
    print(page_wiki.images[n])
#'https://upload.wikimedia.org/wikipedia/commons/7/7e/Circle-icons-profile.svg'


recherche("Véronique Louwagie")