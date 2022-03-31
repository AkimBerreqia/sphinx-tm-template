# 1. Cheminement du projet

## Présentation du projet

#### Parcours de l'étudiant

L'étudiant n'a pas besoin de savoir beaucoup de notions sur la cryptologie pour participer au cours. Il doit seulement avoir les notions de base des cours d'informatique sur la programmation en python.

Le chiffre de César, l'attaque par force brute, ainsi que le chiffrement par substitution monoalphabétique sont abordés au fur et à mesure que l'étudiant avance dans le cours.

Le travail de l'élève est de traverser les différentes pages théoriques et pratiques, qui sont illustrées par des exercices interactifs.

#### Procédure

Les technologies de développement du projet comportent *le Javascript*, *l'HTML*, *le CSS*, et *Quasar* au travers de *VueJS*, qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents *.vue*, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée dans des fichiers *markdown*, depuis GitPod.io avec le langage de programmation LaTeX, qui suit la documentation Sphinx. Il y a également un dépôt GitHub, qui sert à suivre l'évolution du projet.

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionnent les directives *Vue*, ainsi que les composants *Quasar*.

##### Première version du site (prototype)

Le site est passé par plusieurs étapes. Depuis la réédition de la version intérmédiaire, il a fallu se familiariser avec la technologie *Vue*.

Monsieur Donner Cédric m'a demandé de suivre un cours en ligne pour apprendre à me servir de *Vue.js* (lien du cours : https://vuejs.org/tutorial/#step-1).

A partir de ce point, le projet a réellement commencé à prendre forme.

Tout le texte est écrit à l'intérieur des fichiers, ce qui prend beaucoup de place.

Chaque sous-chapitre est contenu dans un carrousel/*q-carousel* (ce composant *Quasar* est développé plus en détail dans la suite du travail de maturité). C'est la grande différence qu'il y a entre le prototype et la version finale.

##### Deuxième version du site (version finale)



# 2. Objectifs

Le projet a pour but d'apporter un aspect plus neuf au site de Monsieur Donner Cédric, pour le cours sur la cryptologie, afin qu'il soit plus simple aux élèves du Collège du Sud d'apprendre ce domaine, de manière plus ludique. Bien évidemment, il s'agit surtout d'une base de site, alors il est également possible de reprendre le code présent pour ajouter, à tout moment, des chapitres supplémentaires.

# 3. Concepts de base utilisés avec Quasar et VueJS

Ce sont des outils de fabrication de site qui pour le premier, simplifie la manière d'écrire le code. Par exemple, la directive *v-model* sert à donner une identité à l'élément auquel elle appartient.

```HTML
<input v-model="réponse" placeholder="Veuillez écrire la réponse ici">
<p>Votre réponse est {{réponse}}.</p>
```

Dans ce cas de figure, *v-model* correspond à ce que l'utilisateur écrit dans la zone de texte. L'élément "p" va reprendre le *v-model* pour l'intégrer à l'emplacement *{{réponse}}*. De ce fait, si l'utilisateur écrit "merveilleuse", le texte affichera : "Votre réponse est merveilleuse".

Pour le second, *Quasar* rend le code plus dynamique, en préfabriquant des composants qui permettent d'avoir, par exemple, un bouton, avec une certaine taille, un certain contour, etc.

```HTML
<q-btn label="Clique">
```

Dans l'exemple ci-dessus, le bouton a déjà une forme et un contour défini Le label est affiché à l'intérieur du bouton.

Avec *q-btn*, il n'est pas nécessaire de définir une classe ou un style dans l'élément, car le bouton a déjà ces informations définies par défaut. Il reste le label à indiquer, ou alors la couleur, mais ce n'est pas obligatoire, pour que le bouton apparaisse à l'écran.

```{Admonition} A savoir
*Quasar* met à disposition des composants libre de droit, qui peuvent être modifier pour plaire à chacun (lien du site : https://quasar.dev/).
```

```{Warning}
Tout le code de cette section provient de VueJS, qui a préfabriqué le code du document. Cependant, il y a quelques changements qui ont été apportés pour permettre au site interactif d'avoir l'aspect qu'il a aujourd'hui.
```

Le site *VueJS* comporte de base des outils qui permettent d'avoir une page d'accueil et un menu déroulant sur le côté de l'écran.

L'image ci-dessous représente la page d'accueil par défaut qui est faite par VueJS.

```{figure} ../source/figures/homePageBefore.png
```

C'est à partir de là que le site interactif commence.

Dans les fichiers de base de la page *VueJS*, il y a le fichier "default.vue", qui se trouve dans le dossier "layouts".

```{Admonition} A savoir
Le code qui suit a déjà été modifié, pour convenir aux besoins du site interactif, mais la base du code provient de *Vue*.
```

```HTML
<template>
  <q-layout view="hHh lpr fFf">
    <q-header elevated class="bg-primary text-white text-left">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="drawerLeft = !drawerLeft" />
        <q-toolbar-title>
          <router-link to="/">1 Cryptologie et codage de l’information</router-link>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer show-if-above v-model="drawerLeft" side="left" overlay class="bg-grey-5 text-white" bordered>
      <!-- drawer content -->
      <q-list bordered separator class="min-w-25 pa-4">
        <template v-for="(item, index) in generatedRoutes">
          <q-item clickable :key="index" v-if="item.name != 'index'" class="flex-col">
            <q-item-section class="cursor-pointer" @click="router.push({ path: item.path })">
              {{ item.name }}
            </q-item-section>
          </q-item>
        </template>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view v-slot="{ Component }">
        <transition name="slide-fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>

      <q-page-scroller position="bottom-right" :offset="[0, 0]" :scroll-offset="0">
        <div class="col cursor-pointer q-pa-sm text-white">
          <q-btn round icon="arrow_forward" class="rotate-270" color="positive"></q-btn>
        </div>
      </q-page-scroller>
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'

  import generatedRoutes from 'virtual:generated-pages'
  const router = useRouter()

  const drawerLeft = ref<boolean>(false)
</script>

<style lang="scss">

  html { 
    background-color: #e6e6e6;
    }

  .slide-fade-enter {
    transform: translateX(10px);
    opacity: 0;
  }

  .slide-fade-enter-active,
  .slide-fade-leave-active {
    transition: all 0.2s ease;
  }

  .slide-fade-leave-to {
    transform: translateX(-10px);
    opacity: 0;
  }

  .q-page-container {
    margin: auto;
    margin-top: 50px;
    text-align: left;
    align: center;
    color: #33abd6;
    background-color: #dedcdc;
    max-width:40em;
    
  }
</style>
```

C'est à partir de ce fichier que les éléments généraux par défauts du site sont générés, comme par exemple la taille du texte, les marges, la couleur du font de la page, etc.

```{figure} ../source/figures/homePageNow.png
```

Voici, ci-dessus le rendu final de la page d'accueil, pour le site interactif.

Les premiers composants quasar qui nous intéressent, servent à former l'aspect visuel du site, comme par exemple l'en-tête du site, ainsi que le menu déroulant sur la gauche de l'écran. Il y a également les liaisons pour naviguer entre les différentes sections du cours.

## Composants *Quasar* utilisés pour former les paramètres par défaut du site

#### *q-layout*

Le document *default.vue* contient, tout d'abord le plan de la page, autrement dit, le "layout". C'est à dire, que le composant va former la page, comme si elle est séparée en un tableau de trois parties sur trois.

```{figure} ../source/figures/layout.png
```

Les lettres en majuscule signifient que l'élément de la page a une position fixe, sur l'écran. C'est à dire que si la page défile vers le bas, ces éléments apparaissent toujours à l'endroit où ils sont de base. Pour le site interactif, le composant *q-layout* définie le plan comme ceci :

```HTML
<template>
  <q-layout view="hHh lpr fFf">
    <!-- ... -->
  </q-layout>
</template>
```

Chaque bloque de lettres correspond à une ligne du tableau. Les lettres *h* et *H* configurent la forme de l'en-tête. Le *l* et le *L* sont pour le menu déroulant de gauche. Le *p* ne change jamais. Le *r* et le *R* donnent la position du menu déroulant de droite. Finalement, le *f* et le *F* représentent le bas de page.

```{Admonition} A savoir
Il n'est pas obligatoire d'avoir de menus déroulant pour faire un site. Dans ce cas, il ne faut pas rajouter de composants *q-drawer* à la suite de l'instruction du plan du site. De cette manière, les instructions données dans le *q-layout* pour les menus déroulant n'impactent pas la suite du code.
```

### En-tête

#### *q-header*

Ensuite, le composant *q-header* permet de configurer l'en-tête comme ceci :

```HTML
<q-header elevated class="bg-primary text-white text-left">
  <!-- ... -->
</q-header>
```

Dans ce cas de figure, le contenu qui se trouve entre les guillemets de *class*, exprime les propriétés de l'en-tête. Par exemple, *bg-primary* est la couleur de l'arrière plan. La couleur primary est la couleur de référence du site.

Dans le fichier *quasar-variables.sass* à l'emplacement 'src/assets/style/quasar-variables.sass', il est possible de définir une infinité de couleurs en se servant à chaque fois d'un certain mot pour lui attribuer une couleur. Dans ce cas de figure, *primary* fait référence à la couleur #33abd6, générée en hexadécimal. Voici ci-dessous tous les exemples disponibles pour le site :

```SASS
$primary   : #33abd6
$secondary : #5dd9cc
$accent    : #aa86b0

$dark      : #1D1D1D

$positive  : #9bd690
$negative  : #C10015
$info      : #cedbda
$warning   : #F2C037
```

Pour *text-white*, il donne la couleur du texte et pour *text-left*, il donne l'alignement du texte de l'en-tête.

```{Admonition} Important
Sans ce composant, le site n'affichera pas d'en-tête, car *q-header* définit, en quelque sorte, que le site doit contenir un en-tête. Il y a également d'autres composants qui joue le même rôle. Par exemple, *q-page-container* définit le contenu de la page, *q-page-sticky* définit les éléments qui gardent la même position, si la page défile, *q-toolbar* définit le contenu de la barre d'outils, etc. Ces composants sont développés plus en détail, par la suite.
```

#### *q-toolbar/q-toolbar-title*

Ces composants servent à définir le titre principale du site, qui apparait constamment dans l'en-tête :

```HTML
<q-toolbar>
  <q-btn dense flat round icon="menu" @click="drawerLeft = !drawerLeft" />
  <q-toolbar-title>
    <router-link to="/">1 Cryptologie et codage de l’information</router-link>
  </q-toolbar-title>
</q-toolbar>
```

*q-toolbar* contient toutes les informations qui apparaissent dans l'en-tête. Il y a tout d'abord un bouton, *q-btn*, qui permet de faire apparaitre le menu déroulant. Ce bouton a comme propriété d'avoir l'icone *menu*, qu'il est rond, qu'il doit inverser la valeur de *drawerLeft* s'il est pressé, etc. Les autres propriétés sont moyens importantes.

Pour ce qui est du titre de la barre d'outils, *q-toolbar-title*, il est nommé comme étant : "1 Cryptologie et codage de l’information".

Le lien du routeur, *router-link* permet, lorsque l'utilisateur appuie sur le titre, de changer de page, sans devoir recharger le site, grâce au paramètre :
```HTML
to="..."
```

Dans ce cas, la destination est "/". Il est configuré que "/" est la page d'index du site, autrement dit, la page d'accueil."

### Menu déroulant

#### *q-drawer*

Ce composant contient tous les éléments qui définissent le menu déroulant.

```HTML
<q-drawer show-if-above v-model="drawerLeft" side="left" overlay class="bg-grey-5 text-white" bordered>
  <!-- ... -->
</q-drawer>
```
La directive *v-model* donne comme référence au tiroir la constante *drawerLeft*. Si cette constante change, le tiroir est influencé.

C'est ici que le bouton de l'en-tête est utilisé. La valeur de la constante *drawerLeft* est assignée comme étant fausse, par défaut. A chaque fois que le bouton est pressé, sa valeur varie entre vrai et faux. Si sa valeur est vrai, alors le menu déroulant apparait à l'écran.

```JavaScript
import {ref} from 'vue'
const drawerLeft = ref<boolean>(false)
```
*Overlay* signifie que lorsque le menu apparait, il n'influence pas la position du texte présent sur la page.

L'instruction ci-dessous permet d'avoir le menu du côté gauche de l'écran.

```HTML
side="left"
```

*Bordered* sert à mettre des bordures pour les éléments du menu.

#### *q-list*

Ce composant fabrique une liste dans laquelle il est possible d'ajouter plusieurs éléments. Pour le site interactif, il s'agit des chapitres.

```HTML
<q-list bordered separator class="min-w-25 pa-4">
  <!-- ... -->
</q-list>
```

Entre chaque élément, il y a une séparation, faite à partir de *separator*.

Pour *class*, il est indiqué que chaque élément ne peut pas avoir de largeur plus petite que 25. C'est une manière de garder une mise en page correcte pour le site, même si l'onglet dans lequel se trouve la page est réduit, ou agrandi.

#### *q-item/q-item-section*

Pour cette dernière partie sur le menu déroulant, le modèle ci-dessous va faire pour chaque *item*, qui correspond à chaque page, un système qui permet de pouvoir accéder à la page souhaitée lorsque la section d'objets souhaitée est appuyée avec le curseur.

```HTML
<template v-for="(item, index) in generatedRoutes">
  <q-item clickable :key="index" v-if="item.name != 'index'" class="flex-col">
    <q-item-section class="cursor-pointer" @click="router.push({ path: item.path })">
      {{ item.name }}
    </q-item-section>
  </q-item>
</template>
```

Ce modèle/*template* va puiser dans chaque élément de *generateRoutes*, qui lui-même se sert de chaque document figurant en premier lieu dans le dossier *pages*, se situant dans le dossier *src*.

```JavaScript
import { useRouter } from 'vue-router'

import generatedRoutes from 'virtual:generated-pages'
const router = useRouter()
```

Chaque section d'objets contient un nom différent, qui fait référence à la page, qui lui est attribuée.

Lorsque la souris passe sur un des objets du menu déroulant, le curseur change, grâce à *cursor-pointer*, se situant dans la classe de la section d'objets. Cela sert à indiquer à l'utilisateur qu'il peut cliquer à cet endroit.

L'élément ci-dessous :

```HTML
router.push({ path: item.path })
```

permet de changer l'url de la page, pour naviguer à travers les pages du site, lorsque l'utilisateur appuie sur la section.

```{Tip}
Pour le générateur d'itinéraires, il se sert également des documents 'index.vue', '1.1 Introduction.vue', '1.2 Le chiffre de César.vue', etc, qui contiennent la matière du cours de cryptologie, avec les outils interactifs fabriqués, au cours du travail de maturité.
```

### Contenu de la page

#### *q-page-container*

Ce composant *Quasar* permet de donner le contenu par défaut que toutes les pages du site possèdent.

```HTML
<q-page-container>
  <router-view v-slot="{ Component }">
    <transition name="slide-fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>

  <!-- ... -->
</q-page-container>
```

Tout d'abord, chaque page a pour le menu déroulant une animation qui est faite, lorsque le bouton 'menu', de l'en-tête, est pressé.

Il y a une animation pour faire apparaitre et disparaitre le menu, grâce à l'intitulé *transition*.

*Transition* fait appel au code CSS suivant :

```CSS
.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.2s ease;
}

.slide-fade-leave-to {
  transform: translateX(-10px);
  opacity: 0;
}
```

Dans un premier temps, *.slide-fade-enter* donne les informations du menu, lorsque ce dernier doit apparaitre, avec une position d'arrivée, ainsi que l'opacité de départ. Pour *.slide-fade-leave-to*, le même processus a lieu, mais pour disparaitre.

Dans un second temps, *.slide-fade-enter-active* et *.slide-fade-leave-active* donnent le temps que la transition d'apparition et celle de disparition mettent pour exécuter l'action.

La couleur d'arrière plan du site est la suivante :

```CSS
html { 
  background-color: #e6e6e6;
}
```

Elle est présente, pour donner un côté sobre au site et également pour fatiguer le moins possible l'oeil lorsque l'utilisateur passe beaucoup de temps sur chaque page.

Le style du contenu de la page est influencé par les paramètres suivants :

```CSS
.q-page-container {
  margin: auto;
  margin-top: 50px;
  text-align: left;
  align: center;
  color: #33abd6;
  background-color: #dedcdc;
  max-width:40em;
}
```

Ce composant possède une marge automatique. Il a seulement une marge de cinquante pixels en haut, pour chaque page. Le contenu est centré au milieu de la page, mais le texte aligné à gauche, avec une couleur d'arrière plan qui se rapproche du blanc, *#dedcdc*, et avec un texte bleu, *#33abd6*. Le conteneur de page a une largeur maximale de quarante "em", pour rendre le texte plus lisible et pour ne pas avoir une surcharge de mots par ligne.

"Em" est une unité de mesure qui existe en *CSS* et qui est aussi appelée, unité relative. Bien évidemment, ce n'est pas la seule unité qui est utilisée. Il faut distinguer les unités relatives et les unités absolues. Elles jouent chacunes un rôle différent dans le style d'un site.

```{Warning}
Il existe également des unités relatives au viewport, mais la commande viewport est devenue obsolète, avec le temps. De ce fait, pour le reste du travail de maturité, les unités relatives au texte et au viewport sont identifiées comme étant des unités relatives.
```

Les différentes unités relatives sont "em", "rem", "ex", "ch", "lh", "vw", "vh", "vmin" et "vmax". L'unité "em" reste celle qui est le plus souvent utilisée.

Pour les unités absolues, il y a : "cm", "mm", "Q" (quart de millimètre), "in" (inche), "pc" (pica), "pt" (point) et "px". Cette fois-ci, l'unité "pixel" est la plus récurrente de cette gamme d'unités.

#### *q-page-scroller*

Chaque page a un défileur de page, sous forme de bouton pour pouvoir défiler vers le haut, grâce au composant *q-page-scroller* montré ci-dessous :

```HTML
<q-page-scroller position="bottom-right" :offset="[0, 0]" :scroll-offset="0">
  <div class="col cursor-pointer q-pa-sm text-white">
    <q-btn round icon="arrow_forward" class="rotate-270" color="positive"></q-btn>
  </div>
</q-page-scroller>
```

La *position* du défileur de page est en bas à droite de l'écran. La forme de ce bouton est ronde, avec l'appelation *round* L'icone du bouton est une flèche qui pointe vers le haut et ce bouton a une couleur vert clair, qui lui est attribuée par le mot "positive".

## Composants *Quasar* utilisés pour former la page d'accueil/*index.vue*



## Composants *Quasar* utilisés pour former les pages du site



#### Q-carousel/q-carousel-slide

Ces composants sont utilisés dans le document *index.vue*, qui forme la page d'accueil, mais aussi pour le prototype de chaque page du cours (1.1 Introduction, 1.2 Le chiffre de César, etc).

Le composant « q-carousel » va créer une zone qui est séparée en plusieurs pages (q-carousel-slide), se situant à l’intérieur du carousel. De ce fait, il est possible de naviguer entre chaque slide.

## Q-btn/q-btn-group/q-separator (valider section)

## Q-page-sticky (navigation btn/q-toolbar/q-toolbar-title)

## Q-dialog/q-card/q-card-section/q-card-actions

# 4. Développement d'outils interactifs

## V-html/import json file

## Q-input/v-model/respondAnswer(exercice, correctAnswer, maxLength)

## Quiz/myQuizQuestions

## Iframe

## Q-table/search/lexique/terme/signification/rows

## Library

# 5. Apports du travail

```{Tip}
Certains composants présentés auraient pu être implémentés dans les documents contenant l'ensemble du cours, depuis un autre document ".vue", car ils sont réutilisés plusieurs fois de la même manière, mais avec quelques paramètres qui changent. Ce système pourra être rajouté en tant que bonus d'ici la présentation orale du travail de maturité.
```

# 6. Conclusion



# 2. Outils interactifs avec *Quasar*

```{admonition} Information
Il fallait plusieurs moyens pour que l'utilisateur puisse interagir avec une panoplie de possibilité. Il y a donc plusieurs outils *Quasar* qui ont été exploités pour cela.
```

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

## q-carousel

Un "carousel" est une sorte de carte, dans laquelle il est possible de mettre ce que l'on souhaite.

```HTML

<q-carousel
  v-model="action.slide"
  transition-prev="scale"
  transition-next="scale"
  swipeable
  animated
  control-color="white"
  navigation
  padding
  arrows
  height="400px"
  class="bg-info text-white
  shadow-1 rounded-borders
  column no-wrap flex-center
  text-center"
>
  <q-carousel-slide
  name="cryptographie1">
      <!-- ... -->
  </q-carousel-slide>

  <q-carousel-slide
  name="cryptographie2">

      <!-- ... -->

  </q-carousel-slide>
</q-carousel>
```

Le composant "q-carousel" va créer une zone qui pourra être séparée en plusieurs pages (q-carousel-slide) à l'intérieur du carousel et il est possible de naviguer enter chaque slide.

## q-dialog

# 3. Aspect visuel du cours interactif

*Quasar* propose des banières et des menus personnalisables pour fabriquer un site. A partir de ces éléments, il est possible de les modifier à sa guise.

Pour notre site de cours, il y a tout d'abord une en-tête, avec le nom du cours et un bouton qui affiche une barre de menu sur la gauche de l'écran.

<!--A modifier par rapport au site.-->

```HTML
<q-layout view="hHh lpR fFf">

  <q-header elevated class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

      <q-toolbar-title>
        <q-avatar>
          <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
        </q-avatar>
        Title
      </q-toolbar-title>

      <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
    </q-toolbar>

    <q-tabs align="left">
      <q-route-tab to="/page1" label="Page One" />
      <q-route-tab to="/page2" label="Page Two" />
      <q-route-tab to="/page3" label="Page Three" />
    </q-tabs>
  </q-header>

  <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
    <!-- drawer content -->
  </q-drawer>

  <q-drawer show-if-above v-model="rightDrawerOpen" side="right" bordered>
    <!-- drawer content -->
  </q-drawer>

  <q-page-container>
    <router-view />
  </q-page-container>

  <q-footer elevated class="bg-grey-8 text-white">
    <q-toolbar>
      <q-toolbar-title>
        <q-avatar>
          <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
        </q-avatar>
        <div>Title</div>
      </q-toolbar-title>
    </q-toolbar>
  </q-footer>

</q-layout>
```

Il est possible de trouver un template complet qui permet de commencer avec une base de site, qui contient plusieurs exemples *Quasar*, pouvant être utilisés si nécessaire.

# 4. Structure du site

Pour la première page, il s'agit d'une introduction à la cryptographie. Il n'y a rien d'intéressant au niveau du code à présenter, car cette page est seulement écrite en *HTML*.

Pour ce qui est de la deuxième page, il y a déjà plus de matière. Cette section présente le chiffre César, en commençant par un exercice qui confronte l'utilisateur face à un texte chiffré et il doit écrire le texte clair, avec quelques indices.