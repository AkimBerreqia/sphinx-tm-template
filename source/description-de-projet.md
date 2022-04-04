# Description du projet

## Présentation du projet

```{admonition} Information
Le tutoriel consiste à confronter l'élève face à plusieurs algorithmes de chiffrement de données, pour qu'il soit capables de comprendre et de pouvoir utiliser la cryptanalyse, servant à trouver le fonctionnement d'un cryptosystème.
```

### Parcours de l'étudiant

L'étudiant n'a pas besoin de savoir beaucoup de notions de la cryptographie pour avancer dans le tutoriel. Il doit seulement avoir les notions de bases des cours d'informatique sur la programmation en python.

Le chiffrement César, celui de Vigenère, ainsi que des chiffrements de substitutions monoalphabétiques sont étudiés par l'élève, au cours de son apprentissage de la cryptologie. Il apprendra le rôle des clés de chiffrement, ainsi que les fréquences des groupes de lettres récurrentes en français, pour pouvoir déchiffrer un texte chiffré de moyenne taille (un paragraphe de quelques lignes).

Le travail de l'élève est également de traverser les différentes pages théoriques et pratiques, qui sont illustrées par des exercices personnalisés.

Il apprend à protéger des données, ainsi qu’à en décrypter d'autres, pour comprendre des messages codés avec le chiffrement César, celui de Vigenère et celui de substitution monoalphabétique. Il doit passer de pages en pages pour assimiler le thème enseigné. A chaque fin de section, l’étudiant est testé par le biais d’un QCM. Une fois la section terminée, il peut passer à la suite de son apprentissage.

```{Admonition} BONUS
L'étudiant gagnera des points, suivant le niveau de réussite de l’épreuve.
```

### Procédure

Les technologies de développement du projet comportent *Sublime Text* et pour le code, les langages de programmation sont *JavaScript*, *HTML* et *CSS*, servant également à développer la page de cours, au travers d'un document index.html et d'un document style.*CSS*, qui permet au serveur local du collège de démarrer la page. Une grande partie des recherches du développement du code se fait à partir d'informations réunies sur plusieurs morceaux de codes libres de droit, mis en ligne, ou à partir d'informations provenant de livres abordant le domaine de la cryptologie. Et bien évidemment, ces bouts de codes sont cités.

Il y a un dépôt *GitHub* pour la partie écrite du travail de maturité, qui est rédigée depuis *GitPod* en *LaTeX*, qui suit la documentation *Sphinx*. Il y a également un deuxième dépôt, qui sert à suivre l'évolution de l'écrit, au fur et à mesure que la rédaction du TM et que le code progressent.

## Apprentissage de méthodes pédagogiques pour l'enseignement de la matière

### Recherche

Il a fallu, tout d'abord, chercher s'il existe déjà des tutoriels qui existent, dans la même gamme, pour ne pas recopier la partie visuelle de ces cours.

Il se trouve que *Unity* possède plusieurs sources d'inspirations pour ce séminaire, à ce niveau. [^unitySource]

*Unity* est un moteur de jeu assez populaire qui exploite principalement les langages *C#* et *C++*, pour sa partie de programmation. [^unitySource]

Ces cours sont structurés en plusieurs chapitres, qui sont eux-mêmes composés de plusieurs sous-chapitres. De cette manière, il est possible de progresser sur une fenêtre déroulante, menant jusqu'à la fin du chapitre principal. [^unitySource]

Cette conception est assez intéressante, sachant que ces pages sont accompagnées d'illustrations pour le sujet présenté. [^unitySource]

### Développement de l'espace d'étude pour l'élève

Dans un premier temps, le contenu *HTML* de la page comprend des zones de texte pour que l'étudiant puisse répondre par lui-même aux différentes questions, les explications en tout genre de la matière, telles que de la théorie, des consignes d'exercices ou des indices pour ces derniers sont soutenues par des images et du code.

Suite à cela, la partie *CSS* servent à l'esthétique de la page et finalement le code en *JavaScript* supporte les différents algorithmes exploités par la page.

[^unitySource] : UNITY LEARN, "Tutoriels Unity". Consulté le 30 décembre 2021. <https://learn.unity.com/?_ga=2.135839737.951800538.1642373266-847038774.1640958251>