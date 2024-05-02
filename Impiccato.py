#coding=utf-8

import csv
import random
import string

vocabulary = []
#apro il file csv e cerco i film in cui compare "Italy"
with open("netflix_titles.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countries = row['country'].split(",")#uso il metodo split per dividere la stringa in una lista di stringhe, dove la virgola sta ad indicare lo stato successivo, altrimenti tipo "united states" varrebbero come due stati
        if 'Italy' in countries:
            #vado ad inserire nella variabile vocabolario i titoli dei film che contengono "Italy"
            vocabulary.append(row['title'])

#print(vocabulary)
letters = []
attempts = 5
guessed = ""

#Setto il seed per rendere replicabile gli esperimenti che facciamo
#random.seed(a=5)#il seed mi farà comparire sempre lo stesso risultato(stampato da print(word))
random_index = random.randrange(0,len(vocabulary))

word = vocabulary[random_index].lower()

    #print(word)
#con questa funzione inizializzo la parola con gli spazi e i trattini
def init_guessed(plaintext):
    w = ""
    for l in plaintext:
        #qui gli sto dicendo che se c'è uno spazio o una punteggiatura allora NON deve aggiungere un trattino, ma uno spazio
        if l.isspace() or l == string.punctuation:
            w += l
        else:
            #qui gli dico di aggiungere un trattino sempre che non sia uno spazio o una punteggiatura
            w += "-"

    return w

def check_letter(l, w):
    found = False
    for i in w:
        if l == i:
            found = True
            break
    return found

def find_occurrencies(l,w):
    occurrencies = []
    for i in range(0, len(w)):
        if l == w[i]:
            occurrencies.append(i)
    return occurrencies

#prende la stringa iniziale la trsforma in una lista e la sostituisce con la lettera scelta
def sub_letters(l, pos, g):
    letters_list = list(g)
    letters_list[pos] = l
    return "".join(letters_list)

guessed = init_guessed(word)
    #print(guessed)

game= True

while game:
    print("Prova ad indovinare!\nIl film misterioso è: {0}".format(guessed))

    print("Hai ancora {} tentativi".format(attempts))

    choice = input("Indovina qual è il film (0 per uscire)")

    if choice == "0":
        game = False
        print("Ti sei arreso!")
        print("Il film misterioso è: {}".format(word))
    elif choice.lower() == word:
        print("Hai indovinato!")
        game = False
    else:
        print("\n ---ERRORE---")
        print("Lettere già estratte: {}".format(letters))
        choice = input("Estrai una lettera:")
        choice = choice.lower()
        if check_letter(choice, letters):
            print("Lettera già scelta")
        else:
            letters.append(choice)
            if check_letter(choice,word):
                occ = find_occurrencies(choice, word)
                for pos in occ:
                    guessed = sub_letters(choice,pos,guessed)
                    print(guessed)

            else:
                print("Lettera non presente! Errore")
                attempts -= 1
                if attempts <= 0:
                    print("Hai perso!")
                    print("Il film misterioso era:{}".format(word))
                    game = False
        print(check_letter(choice, word))
        

