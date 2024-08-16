# Description
Ce projet consiste en un système de recommandation de films développé en Python à l'aide de Jupyter Notebook. L'objectif principal est de fournir des suggestions de films à un utilisateur basé sur ses préférences ou ses films visionnés précédemment. Le projet exploite différentes techniques de filtrage, telles que le filtrage collaboratif et le filtrage basé sur le contenu, pour générer des recommandations pertinentes.

# Fonctionnalités
- Chargement des données : Le projet permet de charger des ensembles de données de films, de notes d'utilisateurs et de métadonnées associées.
- Exploration des données : Des analyses exploratoires sont réalisées pour comprendre la distribution des films, les préférences des utilisateurs, etc.
- Filtrage collaboratif : Implémentation d'un algorithme de filtrage collaboratif utilisant des techniques telles que la factorisation matricielle ou les k plus proches voisins (k-NN).
- Filtrage basé sur le contenu : Recommandations basées sur les attributs des films, tels que le genre, le réalisateur, ou les acteurs.
- Évaluation des performances : Utilisation de métriques comme la précision, le rappel et le score F1 pour évaluer les performances du modèle de recommandation.
- Interface utilisateur : Création d'une interface simple permettant à l'utilisateur de recevoir des recommandations en fonction de ses préférences.

# Prérequis
Avant de pouvoir exécuter ce projet, assurez-vous d'avoir installé les éléments suivants :

- Python 3.7 ou plus récent
- Jupyter Notebook
Les bibliothèques Python suivantes :
pandas
    - numpy
    - scikit-learn
    - matplotlib
    - seaborn
    - surprise (optionnel pour filtrage collaboratif)

Vous pouvez installer toutes les dépendances nécessaires en exécutant :

pip install -r requirements.txt

# Installation
1- Clonez ce dépôt sur votre machine locale :
git clone https://github.com/Arambarrix/recommander_system_for_movies.git

2- Accédez au répertoire du projet :
cd projet-recommandation-films

3- Lancez Jupyter Notebook :
jupyter notebook

4- - Ouvrez le fichier based_recommender_system_for_films.ipynb pour commencer à explorer et exécuter les blocs de code.

# Utilisation
- Préparation des données : Suivez les instructions dans le notebook pour charger et explorer les ensembles de données.
- Modélisation : Exécutez les sections du notebook correspondant aux algorithmes de filtrage collaboratif et de filtrage basé sur le contenu.
- Évaluation : Comparez les résultats des différents modèles de recommandation en utilisant les métriques disponibles.
- Personnalisation : Modifiez les paramètres du modèle ou ajoutez de nouvelles fonctionnalités pour améliorer la qualité des recommandations.

# Structure du Projet
- data/ : Contient les ensembles de données utilisés dans le projet.
- notebooks/ : Contient les notebooks Jupyter avec le code et les analyses.
- src/ : Contient les scripts Python pour les fonctions auxiliaires et les modèles.
- requirements.txt : Liste des dépendances nécessaires pour exécuter le projet.
- README.md : Ce fichier.
# Auteur
William Touré - Développeur principal

.

# Remerciements
Merci aux contributeurs des bibliothèques open-source utilisées dans ce projet.
Merci aux créateurs des ensembles de données utilisés pour tester et valider le modèle.
Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à nous contacter directement. Bonne exploration ! 🎬📽️