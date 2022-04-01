# 1. Cheminement du projet/Introduction

## Présentation du projet

### Motivations personnelles



### Structure du site/description du projet

#### Objectifs initiaux

Le projet a pour but d'apporter un aspect plus neuf au site de Monsieur Donner Cédric, pour le cours sur la cryptologie, afin qu'il soit plus simple aux élèves du Collège du Sud d'apprendre ce domaine, de manière plus ludique. Bien évidemment, il s'agit surtout d'une base de site, alors il est également possible de reprendre le code présent pour ajouter, à tout moment, des chapitres supplémentaires.

#### Technologies utilisées

Les technologies de développement du projet comportent *le Javascript*, *l'HTML*, *le CSS*, et *Quasar* au travers de *VueJS*, qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents *.vue*, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée dans des fichiers *markdown*, depuis GitPod.io avec le langage de programmation LaTeX, qui suit la documentation Sphinx. Il y a également un dépôt *GitHub*, qui sert à suivre l'évolution du projet.

#### Sommaire du site

Le site est composé de six pages : "1.1 Introduction", "1.2 Le chiffre de César", "1.3 Attaque par force brute", "1.4 Systèmes de substitution monoalphabétique", "1.5 Attaque par fréquence" et "1.6 Petit lexique de la cryptologie".

#### Principales difficultés rencontrées



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

# ReadMe

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

[^layoutSource]: [https://github.com/fyeeme/vite-quasar/commits/main](https://github.com/fyeeme/vite-quasar/commits/main)