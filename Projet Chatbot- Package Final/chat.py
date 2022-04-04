import joblib
import pickle
from fonction import collage, extraction_data_X_y, nettoyage, vectorizer

#chargement des modèles
loaded_model_ISEN = joblib.load("trained_model_SGD_ISEN.sav")
loaded_model_microsoft=joblib.load("trained_model_SGD_IA_MICROSOFT.sav")

#chargement dico ISEN
with open('dic_num_tag_ISEN.pkl','rb') as f:
    dic_num_tag_ISEN=pickle.load(f)

with open('dico_tag_responses_ISEN.pkl','rb') as f:
    dico_tag_responses_ISEN=pickle.load(f)

with open('encodeurX_ISEN.pkl','rb') as f:
    encodeur_X_ISEN=pickle.load(f)

#chargement dico IA Microsoft
with open('dic_num_tag_IA_MICROSOFT.pkl','rb') as f:
    dic_num_tag_microsoft=pickle.load(f)

with open('dico_tag_responses_IA_MICROSOFT.pkl','rb') as f:
    dico_tag_responses_microsoft=pickle.load(f)

with open('encodeurX_IA_MICROSOFT.pkl','rb') as f:
    encodeur_X_microsoft=pickle.load(f)

# fonction permettant de récupérer la réponse au message de l'utilisateur version ISEN
def predict(msg):
    
    msg = extraction_data_X_y(None, True ,msg)

    msg_clean=nettoyage([msg])
    
    msg_clean=collage(msg_clean)
    
    msg_vec=vectorizer(msg_clean,False,encodeur_X_ISEN)
    
    prediction = loaded_model_ISEN.predict(msg_vec)
    print(prediction)
    tag_predi = dic_num_tag_ISEN[prediction[0]]

    reponse=dico_tag_responses_ISEN[tag_predi]

    return reponse

# fonction permettant de récupérer la réponse au message de l'utilisateur version IA Microsoft
def predict2(msg):
    
    msg = extraction_data_X_y(None, True ,msg)
        
    msg_clean=nettoyage([msg])
    
    msg_clean=collage(msg_clean)
    
    msg_vec=vectorizer(msg_clean,False,encodeur_X_microsoft)
    
    prediction = loaded_model_microsoft.predict(msg_vec)
    
    tag_predi = dic_num_tag_microsoft[prediction[0]]
    
    reponse=dico_tag_responses_microsoft[tag_predi]

    return reponse

    