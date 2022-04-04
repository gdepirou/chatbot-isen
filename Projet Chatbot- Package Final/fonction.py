
import nltk

from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
#nettoyage

from nltk.stem.snowball import FrenchStemmer
import string
#vectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk import word_tokenize
# import our chat-bot intents file
import json


def extraction_data_X_y(jsonfile = None, testing = False, phrase : str = None): #permet d'obtenir les patterns (X_text) et les tags (y_text)
    
    ponctuation = [".", "?", "!", ",", ";", ":", "(",  ")", "[", "]", "«", "»", '"', "/", "}", "{", "'", "#","-","’"]

    if testing == False : #cas d'extraction des données du corpus
        #corpus = import_corpus(jsonfile)
    
        X_texte = []
        y_texte = []
        Responses = []

        dico_tag_responses = {}

        #ponctuation = [".", "?", "!", ",", ";", ":", "(",  ")", "[", "]", "«", "»", '"', "/", "}", "{", "'", "#","-","’"]
        try :
            for doc in corpus['intents']: #'intents
                #print(doc['tag']) #obtenir chaque tag
                for p in doc['patterns']: #'patterns'
                    #print(p) #obtenir chaque phrase/patterns par tags 

                    for element in ponctuation:
                        p = p.replace(element," ")

                    #filtered_phrase = clean_text(p)
                    filtered_phrase = p




                    #X_texte.append(" ".join(filtered_phrase)) Bonne version avec stemming
                    X_texte.append(filtered_phrase)

                    y_texte.append(doc['tag']) 
                    #y_texte.append(doc['tag']) #on rajoute un 2e même tag car on double le dataset

                    Responses.append(doc['responses'])
                    dico_tag_responses[doc['tag']] = doc['responses']

            X_train, X_test, y_train, y_test = train_test_split(X_texte,y_texte,train_size=0.8)

            #print(f"\ndico_tag_responses : \n {dico_tag_responses}")
            return X_texte, y_texte, X_train, X_test, y_train, y_test, dico_tag_responses
        except:
            print("l'extraction des patterns et tags n'a pas fonctionnée, allez voir la fonction extraction data_X_y")
            
    else: #cas en utilisation pour récupérer la phrase
        #new_phrase = []
        
        for element in ponctuation:
            phrase = phrase.replace(element," ")
        
        new_phrase = phrase
        return new_phrase




def clean_text(phrase): #fait du french stemming et du stop words sur une phrase
    """
    test = True indique que la phrase fait parti du dataset de test --> donc on rajoute aux stop_words TOUS les mots du dataset train
    """
    #print(f"----------------------Début clean_text ------------------")
    
    try:
        
        stemmer = FrenchStemmer()
        
        alphabet = list(string.ascii_lowercase)
        une_lettre = ["é", "â", "ê", "î", "ô", "û", "è", "ç", "ä", "ë", "ï", "ö", "ü", "ÿ"]
        for lettre in une_lettre:
            alphabet.append(lettre)
          
        stop_words=stopwords.words("French")
        
        for element in alphabet:
            stop_words.append(element)
        
        
        
        filtered_sentence=[]
             
        #enlever les stop words
        for mot in nltk.word_tokenize((phrase.lower())):
                    
                    #print(mot)
                    if mot not in stop_words:
                        filtered_sentence.append(mot)
        #print(filtered_sentence)

        #stemming en français
     #  print("dans cas données train")

        stemmed = [stemmer.stem(i) for i in filtered_sentence] #stemmer.stem(i) bonne version avec stemming 
        return stemmed
    
    except:
        print("stemming et stop_words n'ont pas fonctionnés")


def nettoyage(X_to_clean):
    X_cleaned=[]
    try :
        for phrase in X_to_clean:
             #   print(f"phrase: {phrase}")
            X_cleaned.append(clean_text(phrase))
            #print(f"X_cleaned : {X_cleaned}")
            
        return X_cleaned
    except : 
        print(f"nettoyage n'a pas marché sur {X_to_clean}")

def collage(X_to_merge):
    #print(f"taille debut : {len(X_to_merge)}")
    
    new_X = []
    phrase=""
    for phrase in X_to_merge :
        #print("phrase : ", phrase)
        new_X.append(" ".join(phrase))
        """for mot in phrase : 
            print('mot:',mot)
            new_X.append(" ".join(phrase))
           """ 
    #print(f"taille finale: {len(new_X)}")
    return new_X

def vectorizer(X_to_vect, train = True, encodeur = None):
    try :
        if train: #cas où on est sur les données d'entrainements : on doit donc créer notre encodeur
            
            enc1=CountVectorizer()
            #enc1=LabelEncoder()
            #enc1=LabelBinarizer()
            #enc1=TfidfVectorizer()
            #enc1=OneHotEncoder(handle_unknown='ignore')


            enc1.fit(X_to_vect) #enc1.fit(X_train) --> supprimer les mots inconnues de la base de test --> enc1.transform(X_train) & enc1.transform(X_test)
            X_train_vec = enc1.transform(X_to_vect)
            X_train_vec = X_train_vec.toarray()
            
            return X_train_vec, enc1
        
        else: #cas où on est avec les données tests, on doit donc récupérer l'encodeur utilisé sur les données d'entrainement pour tranform dessus
            X_test_vec = encodeur.transform(X_to_vect)
            
            X_test_vec = X_test_vec.toarray()
            
            return X_test_vec
            
    except :
        print("la fonction vectorizer n'a pas fonctionnée")


