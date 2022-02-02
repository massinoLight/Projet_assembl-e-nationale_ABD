
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('fr')

def recherche(nom_prenom_depute):

    page_wiki = wiki_wiki.page(nom_prenom_depute)
    print(page_wiki.title)
    print( page_wiki.summary)


recherche("Véronique Louwagie")