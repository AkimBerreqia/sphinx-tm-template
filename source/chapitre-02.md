# 2. Concepts de base utilisés avec *Quasar* et *Vue.js*

```{admonition} Information
Il était nécessaire de se servir de plusieurs technologies de programmation pour que l'utilisateur puisse interagir avec une panoplie de possibilités. Il y a donc plusieurs outils *Quasar* et *Vue.js* qui ont été exploités pour cela.
```

*Vue.js* et *Quasar* sont des outils de fabrication de site qui pour le premier, simplifie la manière d'écrire le code. Par exemple, la directive *v-model* sert à donner une identité à l'élément auquel elle appartient.

```HTML
<input v-model="réponse" placeholder="Veuillez écrire la réponse ici">
<p>Votre réponse est {{réponse}}.</p>
```
[^vueSource]

Dans ce cas de figure, *v-model* correspond à ce que l'utilisateur écrit dans la zone de texte. L'élément "p" va reprendre le *v-model* pour l'intégrer à l'emplacement *{{réponse}}*. De ce fait, si l'utilisateur écrit "merveilleuse", le texte affichera : "Votre réponse est merveilleuse".

Pour le second, *Quasar* rend le code plus dynamique, en pré-fabricant des composants qui permettent d'avoir, par exemple, un bouton, avec une certaine taille, un certain contour, etc.

```HTML
<q-btn label="Clique" />
```
[^quasarSource]

```{figure} ../source/figures/btn.png
figure n°3
```

Dans l'exemple ci-dessus, le bouton a déjà une forme et un contour définis. Le label est affiché à l'intérieur du bouton, uniquement avec des lettres majuscules.

Avec *q-btn*, il n'est pas nécessaire de définir une classe ou un style dans l'élément, car le bouton a déjà ces informations définies par défaut. Il reste le label à indiquer, ou alors la couleur, mais ce n'est pas obligatoire, pour que le bouton apparaisse à l'écran.

```{Admonition} A savoir
*Quasar* met à disposition des composants libres de droit, qui peuvent être modifiés pour plaire à chacun (lien du site : [https://quasar.dev/](https://quasar.dev/)).
```

```{Warning}
Tout le code de cette section provient d'un dépôt *GitHub*, que Monsieur Cédric Donner a mis à disposition, pour coder le projet. Ce dépôt a été créé par Allen Lau. (lien vers le dépôt *GitHub* d'Allen Lau : [https://github.com/fyeeme/vite-quasar](https://github.com/fyeeme/vite-quasar))
Cependant, il y a quelques changements qui ont été apportés pour permettre au site interactif d'avoir l'aspect qu'il a aujourd'hui.
```

Le site *Vue3* comporte de base des outils qui permettent d'avoir une page d'accueil et un menu déroulant sur le côté de l'écran.

L'image ci-dessous représente la page d'accueil par défaut qui est faite par Allen Lau.

```{figure} ../source/figures/homePageBefore.png
figure n°4
```

C'est à partir de là que le site interactif se forme.

Dans les fichiers de base de la page *Vue3*, il y a le fichier "default.vue", qui se trouve dans le dossier "layouts".

```{Admonition} A savoir
Le code qui suit dans la prochaine section a déjà été modifié, pour convenir aux besoins du site interactif, mais la base du code provient de *Vue3*.
```

C'est à partir de ce fichier que les éléments généraux par défaut du site sont générés, comme la taille du texte, les marges, la couleur du font de la page, etc.

```{figure} ../source/figures/homePageNow.png
figure n°5
```

Voici, ci-dessus le rendu final de la page d'accueil, pour le site interactif.

Les premiers composants *Quasar* qui nous intéressent, servent à former l'aspect visuel du site, comme l'en-tête du site, ainsi que le menu déroulant sur la gauche de l'écran. Il y a également les liaisons pour naviguer entre les différentes sections du cours.

## Composants *Quasar* du fichier *default.vue*

Le fichier *default.vue* se situe à l’emplacement 'src/layouts/default.vue'.

#### *q-layout*

Le document *default.vue* contient, tout d'abord le plan de la page, autrement dit, le "layout". C'est à dire, que le composant va former la page, comme si elle est séparée en un tableau de trois parties sur trois.

```{figure} ../source/figures/layout.png
figure n°6
```

Les lettres majuscules signifient que l'élément de la page a une position fixe, sur l'écran. C'est à dire que si la page défile vers le bas, ces éléments apparaissent toujours à l'endroit où ils sont de base. Pour le site interactif, le composant *q-layout* défini le plan comme ceci :

```HTML
<template>
  <q-layout view="hHh lpr fFf">
    <!-- layout content -->
  </q-layout>
</template>
```
[^defaultSource]

Chaque bloc de lettres correspond à une ligne du tableau. Les lettres *h* et *H* configurent la forme de l'en-tête. Le *l* et le *L* sont pour le menu déroulant de gauche. Le *p* ne change jamais. Le *r* et le *R* donnent la position du menu déroulant de droite. Finalement, le *f* et le *F* représentent le bas de page.

```{Admonition} A savoir
Il n'est pas obligatoire d'avoir de menus déroulants pour faire un site. Dans ce cas, il ne faut pas rajouter de composants *q-drawer* à la suite de l'instruction du plan du site. De cette manière, les instructions données dans le *q-layout* pour les menus déroulants n'impactent pas la suite du code.
```

### En-tête

#### *q-header*

Ensuite, le composant *q-header* permet de configurer l'en-tête comme ceci :

```HTML
<q-header elevated class="bg-primary text-white text-left">
  <!-- header content -->
</q-header>
```
[^defaultSource2]

Dans ce cas de figure, le contenu qui se trouve entre les guillemets de *class*, exprime les propriétés de l'en-tête. Par exemple, *bg-primary* est la couleur de l'arrière-plan. La couleur *primary* est la couleur de référence du site.

Dans le fichier *quasar-variables.sass* à l'emplacement 'src/assets/style/quasar-variables.sass', il est possible de définir une infinité de couleurs en se servant à chaque fois d'un certain mot pour lui attribuer une couleur. Dans ce cas de figure, *primary* fait référence à la couleur #33abd6, générée en hexadécimal. Voici ci-dessous toutes les couleurs du site :

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
[^quasarSaasSource]

Pour *text-white*, il donne la couleur du texte et pour *text-left*, il donne l'alignement du texte de l'en-tête.

```{Admonition} Important
Sans ce composant, le site n'affichera pas d'en-tête, car *q-header* définit, en quelque sorte, que le site doit contenir un en-tête. Il y a également d'autres composants qui jouent le même rôle. Par exemple, *q-page-container* définit le contenu de la page, *q-page-sticky* définit les éléments qui gardent la même position, si la page défile, *q-toolbar* définit le contenu de la barre d'outils, etc. Ces composants sont développés plus en détail, par la suite.
```

#### *q-toolbar et q-toolbar-title*

Ces composants servent à définir le titre principal du site, qui apparait constamment dans l'en-tête :

```HTML
<q-toolbar>
  <q-btn dense flat round icon="menu" @click="drawerLeft = !drawerLeft" />
  <q-toolbar-title>
    <router-link to="/">1 Cryptologie et codage de l’information</router-link>
  </q-toolbar-title>
</q-toolbar>
```
[^defaultSource3]

*q-toolbar* contient toutes les informations qui apparaissent dans l'en-tête. Il y a tout d'abord un bouton, *q-btn*, qui permet de faire apparaitre le menu déroulant. Ce bouton a comme propriété d'avoir l'icône *menu*, qu'il est rond, qu'il doit inverser la valeur de *drawerLeft* s'il est pressé, etc. Les autres propriétés sont moins importantes.

Pour ce qui est du titre de la barre d'outils *q-toolbar-title*, il est nommé comme étant : "1 Cryptologie et codage de l’information".

Le lien du routeur, *router-link* permet, lorsque l'utilisateur appuie sur le titre, de changer de page, sans devoir recharger le site, grâce au paramètre :

```HTML
to="..."
```

Dans ce cas, la destination est "/". Cette destination est attribuée à la page d'index du site, autrement dit, la page d'accueil."

### Menu déroulant

#### *q-drawer*

Ce composant contient tous les éléments qui définissent le menu déroulant.

```HTML
<q-drawer show-if-above v-model="drawerLeft" side="left" overlay class="bg-grey-5 text-white" bordered>
  <!-- drawer content -->
</q-drawer>
```
[^defaultSource4]

La directive *v-model* donne comme référence au tiroir la constante *drawerLeft*. Si cette constante change, le tiroir est influencé.

C'est ici que le bouton de l'en-tête est utilisé. La valeur de la constante *drawerLeft* est assignée comme étant fausse, par défaut. A chaque fois que le bouton est pressé, sa valeur varie entre vrai et faux. Si sa valeur est vraie, alors le menu déroulant apparait à l'écran.

```JavaScript
import {ref} from 'vue'
const drawerLeft = ref<boolean>(false)
```
[^defaultSource5]

*Overlay* signifie que lorsque le menu apparait, il n'influence pas la position du texte présent sur la page.

L'instruction ci-dessous permet d'avoir le menu du côté gauche de l'écran.

```HTML
side="left"
```
[^defaultSource6]

*Bordered* sert à mettre des bordures pour les éléments du menu.

#### *q-list*

Ce composant fabrique une liste dans laquelle il est possible d'ajouter plusieurs éléments. Pour le site interactif, il s'agit des chapitres.

```HTML
<q-list bordered separator class="min-w-25 pa-4">
  <!-- list content -->
</q-list>
```
[^defaultSource7]

Entre chaque élément, il y a une séparation, faite à partir de *separator*.

Pour *class*, il est indiqué que chaque élément ne peut pas avoir de largeur plus petite que 25. C'est une manière de garder une mise en page correcte pour le site, même si l'onglet dans lequel se trouve la page est réduit, ou agrandi.

#### *q-item et q-item-section*

Pour cette dernière partie sur le menu déroulant, le modèle ci-dessous fait pour chaque *item*, qui correspond à chaque page, un système qui permet d'accéder à la page souhaitée lorsque la section d'objets souhaités est appuyée avec le curseur.

```HTML
<template v-for="(item, index) in generatedRoutes">
  <q-item clickable :key="index" v-if="item.name != 'index'" class="flex-col">
    <q-item-section class="cursor-pointer" @click="router.push({ path: item.path })">
      {{ item.name }}
    </q-item-section>
  </q-item>
</template>
```
[^defaultSource8]

Ce modèle/*template* va puiser dans chaque élément de *generateRoutes*, avec la directive *v-for*. Le *template* se sert de chaque document figurant en premier lieu dans le dossier *pages*, se situant dans le dossier *src* 'src/pages/(...).vue'.

```JavaScript
import { useRouter } from 'vue-router'

import generatedRoutes from 'virtual:generated-pages'
const router = useRouter()
```
[^defaultSource9]

Chaque section d'objets contient un nom différent, qui fait référence à la page, qui lui est attribuée.

Lorsque la souris passe sur un des objets du menu déroulant, le curseur change, grâce à *cursor-pointer*, se situant dans la classe de la section d'objets. Cela sert à indiquer à l'utilisateur qu'il peut cliquer à cet endroit.

L'élément ci-dessous :

```HTML
router.push({ path: item.path })
```
[^defaultSource10]

permet de changer l'url de la page, pour naviguer à travers les pages du site, lorsque l'utilisateur appuie sur la section.

```{Tip}
Pour le générateur d'itinéraires, il se sert également des documents 'index.vue', '1.1 Introduction.vue', '1.2 Le chiffre de César.vue', etc, qui contiennent la matière du cours de cryptologie, avec les outils interactifs fabriqués, au cours du travail de maturité.
```

### Contenu de la page

#### *q-page-container*

Ce composant *Quasar* permet de donner le contenu par défaut que toutes les pages que le site possède.

```HTML
<q-page-container>
  <router-view v-slot="{ Component }">
    <transition name="slide-fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>

  <!-- q-page-scroller content -->
</q-page-container>
```
[^defaultSource11]

Tout d'abord, chaque page a pour le menu déroulant une animation qui est faite, lorsque le bouton 'menu', de l'en-tête, est pressé.

Il y a une animation pour faire apparaitre et disparaitre le menu, grâce à l'intitulé *transition*.

*Transition* fait appel au code SCSS suivant :

```SCSS
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
[^defaultSource12]

Dans un premier temps, *.slide-fade-enter* donne les informations du menu, lorsque ce dernier doit apparaitre, avec une position d'arrivée, ainsi qu’avec l'opacité de départ. Pour *.slide-fade-leave-to*, le même processus a lieu, mais pour disparaitre.

Dans un second temps, *.slide-fade-enter-active* et *.slide-fade-leave-active* donnent le temps que la transition d'apparition et celle de disparition mettent pour exécuter l'action.

La couleur d'arrière-plan du site est la suivante :

```SCSS
html { 
  background-color: #e6e6e6;
}
```
[^defaultSource13]

Elle est présente, pour donner un côté sobre au site et également pour fatiguer le moins possible l'oeil lorsque l'utilisateur passe beaucoup de temps sur chaque page.

Le style du contenu de la page est influencé par les paramètres suivants :

```SCSS
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
[^defaultSource14]

Ce composant possède une marge automatique. Il a seulement une marge de cinquante pixels en haut, pour chaque page. Le contenu est centré au milieu de la page, mais le texte est aligné à gauche, avec une couleur d'arrière-plan qui se rapproche du blanc, *#dedcdc*, et avec un texte bleu, *#33abd6*. Le conteneur de page a une largeur maximale de quarante "em", pour rendre le texte plus lisible et pour ne pas avoir une surcharge de mots par ligne.

"Em" est une unité de mesure qui existe en *CSS*/*SCSS* et qui est aussi appelée, unité relative. Bien évidemment, ce n'est pas la seule unité qui est utilisée. Il faut distinguer les unités relatives et les unités absolues. Elles jouent chacune un rôle différent dans le style d'un site.

```{Warning}
Il existe également des unités relatives au *viewport*, mais la commande *viewport* est devenue obsolète, avec le temps. De ce fait, pour le reste du travail de maturité, les unités relatives au texte et au *viewport* sont identifiés comme étant des unités relatives.
```

Les différentes unités relatives sont "em", "rem", "ex", "ch", "lh", "vw", "vh", "vmin" et "vmax". L'unité "em" reste celle qui est le plus souvent utilisée.

Pour les unités absolues, il y a : "cm", "mm", "Q" (quart de millimètre), "in" (inche), "pc" (pica), "pt" (point) et "px". Cette fois-ci, l'unité "pixel" est la plus récurrente de cette gamme d'unités.

#### *q-page-scroller*

Chaque page a un *scroller* de page, sous forme de bouton pour pouvoir défiler vers le haut, grâce au composant *q-page-scroller* montré ci-dessous :

```HTML
<q-page-scroller position="bottom-right" :offset="[0, 0]" :scroll-offset="0">
  <div class="col cursor-pointer q-pa-sm text-white">
    <q-btn round icon="arrow_forward" class="rotate-270" color="positive"></q-btn>
  </div>
</q-page-scroller>
```
[^defaultSource15]

La *position* du *scroller* de page est en bas à droite de l'écran. La forme du bouton est ronde, grâce à l'appellation *round* L'icône du bouton est une flèche qui pointe vers le haut et ce bouton a une couleur "vert clair", qui lui est attribuée par le mot "positive".

## Composants *Quasar* du fichier *index.vue*

Le code de la page se trouve à l’emplacement 'src/pages/index.vue'.

#### q-carousel et q-carousel-slide

Ce sont les premiers composants qui apparaissent dans le code pour la page d'index, mais ils sont aussi présents dans les prototypes des pages du cours (1.1 Introduction, 1.2 Le chiffre de César, etc).

Le composant *q-carousel* va créer une zone qui est séparée en plusieurs pages / *q-carousel-slide*, se situant à l’intérieur du carrousel. De ce fait, il est possible de naviguer entre chaque *q-carousel-slide*.

```{figure} ../source/figures/indexCarousel.png
figure n°7
```

L'image ci-dessus contient deux encadrés blancs, qui représentent chacun un carrousel.

```HTML
<q-carousel
  v-model="action.slide1"
  animated
  padding
  height="250px"
  class="shadow-1 rounded-borders"
>
  <q-carousel-slide name="presentation" class="column no-wrap">
      <!-- carousel-slide content -->
  </q-carousel-slide>
</q-carousel>

<q-carousel
  v-model="action.slide2"
  animated
  padding
  height="250px"
  class="shadow-1 rounded-borders"
>
  <q-carousel-slide name="sommaire" class="column no-wrap">
      <!-- carousel-slide content -->
  </q-carousel-slide>
</q-carousel>
```
[^quasarSource2]

Dans le code ci-dessus, les deux carrousels ont une hauteur de deux-cent-cinquante pixels. Cette taille peut bien évidemment être changée pour que le contenu ne déborde pas du carrousel.

Chaque carrousel possède un *v-model* différent, ainsi qu'une option *animated*. De cette manière, dès que la page est chargée, le contenu du carrousel apparait à l'écran. Sans ces éléments, le carrousel apparaitrait vide.

```JavaScript
import { ref, reactive } from 'vue'

let action = reactive({
  slide1: ref('presentation'),
  slide2: ref('sommaire')
})
```
[^quasarSource3]

Pour cette page, il n'y a qu'une seule diapositive par carrousel. Cependant, il est possible de faire plusieurs diapositives par carrousel.

#### q-page-sticky

Ce composant apparait sur chaque fichier qui appartient au cours de cryptologie. Tout comme pour le *q-page-scroller*, le *q-page-sticky*, garde la même position à l'écran, même si l'utilisateur fait défiler la page.

Pour la page d'index, ce composant joue deux rôles.

```HTML
<q-page-sticky position="bottom-left" :offset="[5, 5]" class="bg-#cccccccc">
  <q-btn icon="keyboard_arrow_right" to="/1.1 Introduction">1.1 Introduction</q-btn>
</q-page-sticky>
```
[^quasarSource4]

La première fois, il sert à afficher un bouton qui permet de passer à la page suivante. La couleur d'arrière-plan des boutons est d'une teinte presque transparente. L'icône utilisée est une flèche qui pointe vers la droite, pour signaler que le bouton redirige vers la prochaine page.

```{admonition} Important
Pour chaque page, il y a des boutons qui ont des destinations différentes (un bouton qui renvoie à la page d'accueil, un autre pour accéder à la page précédente et un dernier pour passer à la page suivante), mais la base du code reste la même.
```

```HTML
<q-page-sticky position="top" expand class="bg-positive text-white text-center">
  <q-toolbar>
    <q-toolbar-title>1.0 Index</q-toolbar-title>
  </q-toolbar>
</q-page-sticky>
```
[^quasarSource5]

La deuxième fois, son rôle est d'afficher le titre de la page. Dans ce cas, "1.0 Index" est le titre de la page, qui se situe en dessous du titre de l'en-tête du site.

[^defaultSource]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource2]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource3]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource4]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource5]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource6]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource7]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource8]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource9]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource10]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource11]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource12]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource13]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource14]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^defaultSource15]: ALLEN LAU, "code pour la page par défaut du site", 2021, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0](https://github.com/AkimBerreqia/vite-quasar/commit/dd8b033a09c79167c66c5d90a6c7325dde1dd5d0)>

[^quasarSaasSource]: ALLEN LAU, "code pour les différente couleur du site", 2022, consulté le 3 avril 2022, <[https://github.com/AkimBerreqia/vite-quasar/commit/7fbe534dc6d95d63d8f41ec6a1d0855db3f11ce8](https://github.com/AkimBerreqia/vite-quasar/commit/7fbe534dc6d95d63d8f41ec6a1d0855db3f11ce8)>

[^quasarSource]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource2]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource3]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource4]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource5]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^vueSource]: VUE.JS, "documentation de directives vuejs", 2022, consulté le 27 mars 2022, <[https://vuejs.org/](https://vuejs.org/)>

