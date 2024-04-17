#coding=utf-8

import csv

vocabulary = []
#apro il file csv e cerco i film in cui compare "Italy"
with open("netflix_titles.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countries = row
        #uso il metodo split per dividere la stringa in una lista di stringhe, dove la virgola sta ad indicare lo stato successivo, altrimenti tipo "united states" varrebbero come due stati
        ['country'].split(',')
        if 'Italy' in countries:
            #vado ad inserire nella variabile vocabolario i titoli dei film che contengono "Italy"
            vocabulary.append(row['title'])

print(vocabulary)

