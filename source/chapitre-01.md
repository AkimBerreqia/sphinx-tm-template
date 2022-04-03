# 1. Cheminement du projet / Introduction

## Présentation du projet

### Motivations personnelles

L'idée de base était de créer un jeu vidéo, avec Romain De Groote. Chacun devait apprendre un domaine lié à l'informatique. Romain s'occupait d'enseigner la compression de donnée, alors que je m'occupais d'enseigner la cryptologie. Malheureusement, il a fallu à plusieurs reprises modifier le travail, suite à des problèmes d'organisation.

Il a d'abord fallu laisser tomber le concept de jeu vidéo, pour se concentrer exclusivement sur la matière à enseigner, car le projet stagnait de plus en plus. Mais finalement, à cause du retard accumulé pendant la première partie de l'année scolaire et à cause des insuffisances scolaires de chacun, il a été préférable de séparer le groupe en deux nouveaux travaux de maturité différents, pour ne pas pénaliser l'autre. Pour chacun, le contenu à communiquer est resté le même, mais l'approche pour le faire apprendre a changé. De cette manière, le site de cours interactif sur la cryptologie a démarré.

A ce moment, la situation était assez décourageante. L'option d'arrêter le travail de maturité était présente. Cependant, la décision prise a été de ne pas baisser les bras et de recommencer un projet, qui suit toujours l'idée de base, enseigner la cryptologie, mais il fallait faire un projet dans le laps de temps restreint.

Suite à cela, la période qui s'est écoulée, à partir du mois de février jusqu'à ce jour, m'a été bénéfique en ce qui concerne les connaissances acquises dans le domaine de la création de site, ainsi que dans le domaine des langages de programmation appris.

### Structure du site et description du projet

#### Objectifs initiaux

Le projet a pour but d'apporter un aspect plus neuf au site de Monsieur Cédric Donner, pour le cours sur la cryptologie, afin qu'il soit plus simple d'apprendre ce domaine aux élèves du Collège du Sud et de manière plus ludique. Bien évidemment, il s'agit surtout d'une base de site, alors il est également possible de reprendre le code présent pour ajouter, à tout moment, des chapitres supplémentaires.

#### Technologies utilisées

Les technologies de développement du projet comportent *le Javascript*, *l'HTML*, *le CSS*, et *Quasar* au travers de *VueJS*, qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents *.vue*, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée dans des fichiers *markdown*, depuis *GitPod.io* avec le langage de programmation *LaTeX*, qui suit la documentation *Sphinx*. Il y a également un dépôt *GitHub*, qui sert à suivre l'évolution du projet.

#### Sommaire du site

Le site est composé de six pages :
- 1.1 Introduction
- 1.2 Le chiffre de César
- 1.3 Attaque par force brute
- 1.4 Systèmes de substitution monoalphabétique
- 1.5 Attaque par fréquence
- 1.6 Petit lexique de la cryptologie

#### Difficultés envisagées

Il y a certaines difficultés qui étaient à craindre, en février.

La première était le temps que devrait prendre les recherches, pour écrire le contenu du cours.

La deuxième était tous les différents problèmes de développement des outils du site. Par exemple, s'il y a une erreur qui empêche la page de se lancer.

Il y avait également des craintes au niveau du manque de connaissances en la matière. Cela pourrait provoquer un manque d'efficacité lors de la création du projet.

Il y aurait possiblement une prise de retard, pour pouvoir trouver certaines solutions, en se documentant. Mais il pourrait aussi y avoir des soucis dans la documentation. Il suffit de ne pas bien savoir se documenter pour perdre du temps.

#### Parcours de l'étudiant

L'étudiant n'a pas besoin d'avoir beaucoup de notions sur la cryptologie pour participer à ce cours. Il doit seulement avoir les notions de base des cours d'informatique sur la programmation en python.

Le chiffre de César, l'attaque par force brute, ainsi que le chiffrement par substitution monoalphabétique sont abordés au fur et à mesure que l'étudiant avance dans le cours.

Le travail de l'élève est de parcourir les différentes pages théoriques et pratiques, qui sont illustrées par des exercices interactifs.

#### Procédure

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionnent les directives *Vue*, ainsi que les composants *Quasar*.

##### Présentation du site (prototype et version finale)

Le site est passé par plusieurs étapes. Depuis la réédition de la version intermédiaire, il a fallu se familiariser avec la technologie *Vue*.

Monsieur Cédric Donner m'a demandé de suivre un cours en ligne pour apprendre à me servir de *Vue.js* (lien du cours : [https://vuejs.org/tutorial/#step-1](https://vuejs.org/tutorial/#step-1)).

A partir de ce point, le prototype a commencé à prendre forme.

```{figure} ../source/figures/introProto.png
```

Pour le contenu du cours, tout le texte est écrit à l'intérieur des fichiers, dans lesquels le code de la page est développé. Cela rend le nombre de lignes de code assez grand, par document.

Chaque sous-chapitre (par exemple : "1.3.2 Activité 4") est contenu dans un carrousel/*q-carousel* (ce composant *Quasar* est développé plus en détail dans la suite du travail de maturité). C'est la grande différence qu'il y a entre le prototype et la version finale.

Quant à la version finale, elle reprend les mêmes éléments que le prototype, mais en diminuant considérablement le nombre de carrousels. Les seuls carrousels qui restent, sont dans l'index du cours.

```{figure} ../source/figures/introVF.png
```

## Comment accéder au projet ?

Pour accéder au projet, il suffit d'aller sur le dépôt *GitHub* qui suit : [https://github.com/AkimBerreqia/vite-quasar](https://github.com/AkimBerreqia/vite-quasar). A partir de cela, il suffit de rejoindre le dépôt *GitPod* qui correspond au projet.

Ensuite, pour générer le site, il faut entrer les commandes suivantes.

```
yarn install
yarn dev
```

La première sert à installer l'extension "yarn" et la seconde sert à lancer le site sur le serveur local de l'ordinateur que l'utilisateur utilise.