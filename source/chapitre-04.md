# 4. Conclusion

## Contrat initial

De base, ce travail de maturité devait se consacrer au développement d'un jeu vidéo. Cependant, le développement d'un site interactif, avec la technologie *Vue* a été bénéfique. Les connaissances apprises au cours du projet sont pratiques pour un futur travail dans la programmation. Toutes les recherches faites sur les différents langages utilisés pendant le séminaire permettent d'avoir la bonne approche en programmation, pour ce qui concerne la manière de faire du code.

## Apports pédagogiques du site interactif

Il se trouve que le site fonctionne sur le serveur local de l'ordinateur. Les pages sont utilisables et les outils marchent. Le contenu du cours est intéressant et util dans le domaine. De ce point de vue, l'utilisateur est dans de bonnes conditions pour apprendre la cryptologie de manière interactive. De ce fait, le projet rempli son rôle.

## Principales difficultés rencontrées

Au cours de ce travail, plusieurs difficultés se sont mises en place.

### Développement des outils pédagogiques

Pour commencer, le système d'exercices, avec "respondAnswer" a causé plusieurs problèmes.

Il y avait un problème pour mettre une couleur différente si la réponse était juste ou fausse, car au départ, il devait y avoir une seule balise pour afficher le résultat. La solution qui a été trouvé, permet de séparer en deux balises et de choisir laquelle doit apparaitre.

Ensuite, pour le quiz, il y avait des problèmes pour afficher une seule question à la fois, à cause d'incohérences dans la valeur de l'index. De ce fait, la variable *counter* a été créée. Cela a également résolut les problèmes pour changer de question. 

Il y avait une contrainte pour afficher le résultat. Il fallait que les éléments qui composent le résultat soient constamment sur la page, mais cachés. Le problème était que lorsque le résultat était affiché, il fallait rappuyer sur le bouton "VALIDER", pour faire disparaitre le résultat. La solution qui m'est venue a été de rendre fausse la constante qui permet d'afficher le résultat, dès qu'un bouton est appuyé.

Pour le lexique, il a été compliqué d'insérer les bonnes définitions, avec les bon titres, car l'ajout de ces éléments dans la constante *rows*, ne se faisait pas dans un ordre précis. Il a donc fallut changer cela, pour que chaque titre et définition, qui vont ensembles, soit regroupés dans une même liste, à l'intérieur de *rows*.

Pour les problèmes plus esthétiques, la taille des cartes variée selon la longueur du texte.

La bibliothèque a quant à elle posé problème dans l'affichage du résultat. Il fallait que les éléments qui comportent le(s) mot(s) clé(s) s'affichent en liste pucée. Mais étant donné qu'il faille intégrer les éléments dans une variable, la syntaxe *HTML* posait soucis. Le but était de pouvoir intégrer dans une balise la variable *research*. Donc, pour pallier à ce problème, il a été décidé de mettre deux barres obliques, pour montrer la séparation entre chaque élément.

En ce qui concerne l'importation du fichier "introContent.json" dans la première page du cours, il a été compliqué d'importer le contenu *JSON* pour l'utiliser en *JavaScript*. Monsieur Donner a résolut le problème grâce la commande suivant, "import content from 'src/json/introContent.json'". Il suffisait d'importer le contenu du document *JSON*, comme étant un attribut du script *JavaScript*.

Puis, il fallait importer le contenu dans le modèle *HTML*. A partir de ce point, le problème a été le même que pour la bibliothèque. La directive *v-model* a permis d'intégrer du contenu contenant diverses balises.

Finalement, il a été compliqué de créer des outils permettant de changer de page, car il fallait citer le bon chemin menant à chaque document, dans les balises *router-link* ou certains boutons. En réalité, il ne faut pas écrire le vrai chemin du document, mais à la place il faut écrire ce qui doit figurer dans l'url, à la suite de celui qui correspond au site.

Il a également fallu savoir que le site ne peut pas se recharger pour changer de page, sinon ce dernier plante. C'est pourquoi, il n'a pas été simple de trouver la bonne méthode, permettant de changer de page. Mais *router-link* fonctionne parfaitement.

## Problèmes techniques

Pour les problèmes techniques, il y a eu des difficultés dans la documentation, pour trouver certaines informations qui auraient permis de résoudre certains blocage, mentionnés ci-dessus.

Le manque de connaissances a énormément ralentit l'avancement du projet, car la technologie a été apprise au sein du travail de maturité et dans délai assez court.

## Ajout à faire comme bonus pour l'oral du travail de maturité

Il reste encore quelques détails à développer pour finir entièrement le projet.

La page sur l'attaque par fréquence n'est pas encore finie. Elle sera prête pour l'oral.

Certains composants présentés auraient pu être utilisés comme des balises, car ils sont réutilisés plusieurs fois de la même manière au cours du projet, mais avec quelques paramètres qui changent. Un document avec de nouvelles balises pourra être rajouté, pour contenir par exemple une balise qui fabrique un pop-up, avec tous les paramètres présents dans le code qui seront dans le nouveau document.

Il faudra touver un moyen de lister les résultats obtenus avec l'outil *library*, ainsi que de l'intégrer dans le cours.

Il reste encore à stoquer le reste du texte du projet dans le document "introContent.json". Une fois fait, il faudra renommer le document, pour que le nom soit plus général, par exemple "cryptoContent.json".