# 1. Cheminement du projet/Introduction

## Présentation du projet

### Motivations personnelles

L'idée de base était de créer un jeu vidéo, avec Romain De Groote. Chacun devait apprendre un domaine lié à l'informatique. Romain s'occupait d'enseigner la compression de donnée, alors que je m'occupais d'enseigner la cryptologie. Malheureusement, il a fallu à plusieurs reprises modifier le travail, suite à des problèmes d'organisation.

Il a d'abord fallu laisser tomber le concept de jeu vidéo, pour se concentrer exclusivement sur la matière à enseigner, car le projet stagnait de plus en plus. Mais finalement, à cause du retard accumulé pendant la première partie de l'année et à cause des insuffisances scolaires de chacun, il a été préférable de séparer le groupe en deux nouveaux travaux de maturité différents, pour ne pas pénaliser l'autre. Pour chacun, le contenu à communiquer est resté le même, mais l'approche pour le faire apprendre a changé. De cette manière, le site de cours interactif sur la cryptologie est arrivé.

A ce moment, la situation était assez décourageante. L'option d'arrêter le travail de maturité était présente. Cependant, la décision prise a été de ne pas baisser les bras et de recommencer un projet, qui suit toujours l'idée de base, enseigner la cryptologie, mais il fallait faire un projet faisable dans le laps de temps qu'il me restait.

Suite à cela, la période qui s'est écoulé à partir du mois de février jusqu'à ce jour, m'a été bénéfique en ce qui concerne les connaissances acquisent dans le domaine de la création de site, ainsi que dans le domaine des langages de programmation appris.

### Structure du site/description du projet

#### Objectifs initiaux

Le projet a pour but d'apporter un aspect plus neuf au site de Monsieur Donner Cédric, pour le cours sur la cryptologie, afin qu'il soit plus simple aux élèves du Collège du Sud d'apprendre ce domaine, de manière plus ludique. Bien évidemment, il s'agit surtout d'une base de site, alors il est également possible de reprendre le code présent pour ajouter, à tout moment, des chapitres supplémentaires.

#### Technologies utilisées

Les technologies de développement du projet comportent *le Javascript*, *l'HTML*, *le CSS*, et *Quasar* au travers de *VueJS*, qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents *.vue*, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée dans des fichiers *markdown*, depuis GitPod.io avec le langage de programmation LaTeX, qui suit la documentation Sphinx. Il y a également un dépôt *GitHub*, qui sert à suivre l'évolution du projet.

#### Sommaire du site

Le site est composé de six pages :
- 1.1 Introduction
- 1.2 Le chiffre de César
- 1.3 Attaque par force brute
- 1.4 Systèmes de substitution monoalphabétique
- 1.5 Attaque par fréquence
- 1.6 Petit lexique de la cryptologie

```{Warning}
La page sur l'attaque par fréquence n'est pas encore finie. Elle sera prête pour l'oral, en tant que bonus.
```

#### Principales difficultés rencontrées

Au cours de ce travail, plusieurs difficultés se sont mises en place. Pour :

- respondAnswer afficher résultat (mettre une couleur rouge si faux et verte si juste)
- système de quiz (faire apparaitre un seul quiz, puis passer au suivant + affichage bouton)

- faire fonction *library*
- *1.6 Petit lexique ...* (problème pour cartes, taille des cartes, mise en page, gérer les listes avec code js)

- importer fichier json
- v-html (perdu trop de temps inutilement)
- router-link (path)

#### Parcours de l'étudiant

L'étudiant n'a pas besoin de savoir beaucoup de notions sur la cryptologie pour participer au cours. Il doit seulement avoir les notions de base des cours d'informatique sur la programmation en python.

Le chiffre de César, l'attaque par force brute, ainsi que le chiffrement par substitution monoalphabétique sont abordés au fur et à mesure que l'étudiant avance dans le cours.

Le travail de l'élève est de traverser les différentes pages théoriques et pratiques, qui sont illustrées par des exercices interactifs.

#### Procédure

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionnent les directives *Vue*, ainsi que les composants *Quasar*.

##### Première version du site (prototype)

Le site est passé par plusieurs étapes. Depuis la réédition de la version intérmédiaire, il a fallu se familiariser avec la technologie *Vue*.

Monsieur Donner Cédric m'a demandé de suivre un cours en ligne pour apprendre à me servir de *Vue.js* (lien du cours : [https://vuejs.org/tutorial/#step-1](https://vuejs.org/tutorial/#step-1)).

A partir de ce point, le prototype a commencé à prendre forme.

```{figure} ../source/figures/introProto.png
```

Pour le contenu du cours, tout le texte est écrit à l'intérieur des fichiers, dans lesquels le code de la page est développé. Cela rend le nombre de lignes de code assez grand, par document.

Chaque sous-chapitre (par exemple : "1.3.2 Activité 4") est contenu dans un carrousel/*q-carousel* (ce composant *Quasar* est développé plus en détail dans la suite du travail de maturité). C'est la grande différence qu'il y a entre le prototype et la version finale.

##### Deuxième version du site (version finale)

```{figure} ../source/figures/introVF.png
```

Pour la version finale du projet, Monsieur Donner m'a demandé de stoquer le texte dans un fichier *JSON*, pour la page "1.1" du prototype et de la version finale, pour comparer la différence entre les deux versions. Le nom de ce document est actuellement "introContent.json".

```{Tip}
Il reste encore à stoquer le reste du texte du projet dans le document "introContent.json". Mais cette procédure sera effectuée en tant que bonus et le nom du document changera sûrement.
```

## ReadMe

(Pour Mac et PC)

# 2. Outils interactifs avec *Quasar*

Les outils *Quasar* sont des outils utilisés en *HTML* et qui peuvent être combiner avec des outils *VueJS*.

## q-btn
C'est un bouton qui est préfabriqué par *Quasar*. Il est très utile pour avoir moins de code et pour gagner du temps. Il est très souvent combiné à d'autres outils *Quasar*.

```HTML

<q-btn
  label="Afficher la réponse"
  color="..."
  @click="..."
/>
```