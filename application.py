# -*- coding: utf-8 -*-

import requests
import urllib.parse
import json

HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}


def select_query(query):
    query = "query=" + urllib.parse.quote_plus(query)
    # query = urllib.parse.quote_plus(query)
    result=requests.post('http://localhost:3030/dataset_datamining/query', query, headers=HEADERS).content
    result2=result.decode('utf-8')
    print(result2)
    #result2=json.loads(result2)
    
    
        #print(result2["results"]["bindings"][0]["gare"]["value"])
    print


def query_choice():
    print("Bienvenue. Quel type de requête voulez-vous appliquer ?\n \n 1) afficher les noms des bibliothèques publiques et d'enseignement supérieur dans une ville de votre choix")
    print("\n 2) afficher le nom des gares situées dans une région de votre choix")
    print("\n 3) afficher le nom des gares et bibliothèques situées dans un département de votre choix")
    print("\n 4) afficher le nom des gares et bibliothèques situées dans une région de votre choix")




def main():
    query_choice()
    query=""" """
    x=input()
    if x=="1":
        ville=input("Saisissez le nom d'une ville ")
        query = """
        prefix ont:<http://www.owl-ontologies.com/unnamed.owl#>

        SELECT ?public ?ensup ?ville
        WHERE {
        ?sub ont:biblies ?bib1 .
        ?sub2 ont:biblip ?bib2 .
        ?bib1 ont:Libelle ?ensup .
        ?bib2 ont:Libelle ?public .
        ?bib1 ont:Ville ?ville .
        ?bib1 ont:Ville '"""+ ville+"""' .
        ?bib2 ont:Ville '"""+ ville+"""' .
        
        }
        LIMIT 5
        """
    if x=="2":
        reg=input("Saisissez le nom d'une région ")
        query="""prefix ont:<http://www.owl-ontologies.com/unnamed.owl#>

        SELECT ?nomgare ?nomregion
        WHERE {
        ?subject ont:Gare ?obj .
        ?obj ont:Libelle ?nomgare .
        ?obj ont:Region ?nomregion .
        ?obj ont:Region '"""+reg+"""'. 
        }
        LIMIT 10"""
        
    
    if x=="3":
        dep=input("Saisissez le nom d'un département ")
        query="""prefix ont:<http://www.owl-ontologies.com/unnamed.owl#>

        SELECT ?bib_ens_sup ?nomgare ?nomdep
        WHERE {
        ?subject ont:Gare ?g .
        ?g ont:Libelle ?nomgare .
        ?g ont:Departement ?nomdep .
        ?g ont:Departement '"""+dep+"""'. 
        ?sub2 ont:biblies ?b .
        ?b ont:Libelle ?bib_ens_sup .
        ?b ont:Departement '"""+dep+"""' .
        }
        
        LIMIT 10
        """
        
    if x=="4":
        reg=input("Saisissez le nom d'un région ")
        query="""prefix ont:<http://www.owl-ontologies.com/unnamed.owl#>

        SELECT ?bib_ens_sup ?nomgare ?nomreg
        WHERE {
        ?subject ont:Gare ?g .
        ?g ont:Libelle ?nomgare .
        ?g ont:Region ?nomreg .
        ?g ont:Region '"""+reg+"""'. 
        ?sub2 ont:biblies ?b .
        ?b ont:Libelle ?bib_ens_sup .
        ?b ont:Region '"""+reg+"""' .
        }
        
        LIMIT 10
        """
    print(query)
    select_query(query)


if __name__ == '__main__':
    main()
