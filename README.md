# Chatbot pour l'école IA Microsoft et l'école ISEN Brest
> Ce projet a été réalisé dans le cadre de la formation d’ingénieur à l’ISEN Brest. Les étudiants
en charge de ce projet sont : Guillaume Depirou & Charles Depontieu.
Le but de ce projet n’est pas unique. En effet, une multitude d’objectifs sont au cœur de celuici allant de l’appropriation des exigences liés au domaine de l’intelligence artificielle à la rapide
mise à disposition d’informations précises et cohérentes pour l’utilisateur du chatbot.
De plus amples informations sont disponibles dans le "Rapport de Recherche.pdf" dans ce Github.

> Live demo [_here_](https://www.example.com). <!-- If you have the project hosted somewhere, include the link here. -->

## Sommaire
* [Informations générales](#general-information)
* [Librairies utilisées](#Librairies-utilisées)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Pour aller plus loin](#Pour-aller-plus-loin)
* [Remerciements](#Remerciements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Pour la bonne réalisation du chatbot, il a été décidé d’utiliser certaines technologies,
sélectionnées pour leurs avantages par rapport au projet réalisé.
- Python
- html/css/js
- Flask
- Jupyter Notebook
Le choix de ces technologies est justifié dans la partie "7.6.Technologies utilisées" du "Rapport de Recherche.pdf".
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->





## Librairies utilisées
Voici la liste des librairies utilisées :
- deep_translator==1.8.3
- Flask==1.0.2
- joblib==1.1.0
- nltk==3.6.5
- numpy==1.19.2
- pandas==1.3.4
- scikit_learn==1.0.2

Ceux-ci sont disponibles dans le "requirements.txt"


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Le projet est actuellement terminé. En effet, celui-ci étant cadré dans le temps (cadre scolaire), il n'est actuellement pas prévu de poursuivre son développement.


## Pour aller plus loin
Include areas you believe need improvement / could be improved. Also add TODOs for future development.
Plusieurs axes d’améliorations sont observables 
- Sur le site web, le premier serait l’intégration sur un serveur distant, et non local.
De plus, une version mobile pourrait être pensée, avec un point de rupture permettant une
meilleure adaptation du site sur téléphone. Une version plein écran du chatbot pourrait
également être envisagée.
- D’autres améliorations sont également envisageables, la première serait d’intégrer un
apprentissage par renforcement au chatbot. L’utilisateur pourrait indiquer quelle réponse il
attendait si le chatbot n’a pas ou mal compris sa question. Une suggestion de question à poser
pourrait également être affichée selon la question précédente de l’utilisateur, notamment à
l’aide de l’élément « context » compris dans le jeu de donnée. De plus, l'utilisation des probabilités de prédictions du chatbot (visible dans "Test_IA/Chatbot_ISEN_IAMicrosoft.ipynb" dans la fonction "predict") peut être une piste pour ajuster les réponses du chatbot.
- Une autre piste d'amélioration serait l'agrandissement de la base de données. Sa construction "à la main" ne permet pas de dépasser les 90% de précisions. Son automatisation via "web-scrapping" par exemple, peut être une bonne idée.


## Remerciements
Le développement de ce projet a impliqué de nombreux interlocuteurs que nous souhaitons
remercier pour leur temps et leur accompagnement.
Dans un premier temps, nous tenons à saluer la bienveillance de Madame Abdallah Saab qui a
su nous accompagner tant sur le point de vue technique que sur le point de vue gestion de projet.
Un remerciement particulier s’impose pour Monsieur Derrien dont les conseils avisés nous ont
permis de définir la charte graphique de notre projet.
Nous tenons aussi à remercier vivement les auteurs de l’ensemble des informations sur
lesquelles nous avons pu nous appuyer durant le rapport tels que python engineer et machine
learnia.
Nous voulons exprimer notre reconnaissance sincère à Madame Kusberg pour le temps qu’elle
a consacré à nous informer sur l’école IA Microsoft. Ces informations nous ont été précieuses
pour comprendre et adapter notre projet au public souhaitant se renseigner sur cette école.
Ensuite, nous voulons adresser notre gratitude à Monsieur Mourchid qui nous a grandement
aidé grâce à son implication par le biais d’un suivi régulier de notre avancement


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
