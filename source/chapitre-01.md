# 1. Cheminement projet

## Présentation du projet

#### Parcours de l'étudiant

L'étudiant n'aura pas besoin de savoir beaucoup de notions sur la cryptographie pour participer au cours. Il devra seulement avoir les notions de base des cours d'informatique sur la programmation en python.

Le chiffre de César, l'attaque par force brute, ainsi que le chiffrement par substitution monoalphabétique seront abordés au fur et à mesure que l'étudiant avance dans le cours.

Le travail de l'élève sera de traverser les différentes pages théoriques et pratiques, qui seront illustrées par des exercices interactifs.

#### Procédure

Les technologies de développement du projet comportent *le Javascript*, *l'HTML*, *le CSS*, et *Quasar* au travers de *VueJS* qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents *.vue*, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée depuis GitPod.io avec le langage de programmation LaTeX, qui suit la documentation Sphinx. Il y a également un dépôt GitHub, qui sert à suivre l'évolution du projet.

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionne les composants *VueJS* et *Quasar*.

Ce sont des outils de fabrication de site qui pour le premier, simplifie la manière d'écrire le code à écrire, tout en prenant en charge plusieurs langage de programmation sur le même document (*HTML*, CSS et *Javascript*), et pour le second, *Quasar* rend le code plus dynamique.

Pour *Quasar*, l'outil met à disposition des composants libre de droit, qui peuvent être modifier pour plaire à chacun.

# 2. Objectifs

Le projet a pour but d'apporter un aspect plus neuf au site de Donner Cédric, pour le cours sur la cryptologie, afin qu'il soit plus simple aux élèves du Collège du Sud d'apprendre ce domaine, de manière plus ludique.

# 3. Concepts de base utilisés avec Quasar et VueJS

Le site *VueJS* comporte de base des outils qui permettent d'avoir une page d'accueil et un menu déroulant sur le côté de l'écran.

L'image ci-dessous représente la page d'accueil par défaut qui est faite par VueJS.

<img src="~/source/figures/homePageBefore.png"></img>

C'est à partir de la que le site interactif commence.

Dans les fichiers de base de la page *VueJS*, il y a le fichier "default.vue", qui se trouve dans le dossier "layouts".

```HTML
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
      <div v-if="false" class="py-2 mx-auto text-center text-sm">[Default Layout]</div>
      <pre v-if="false">
      {{generatedRoutes}}
      </pre>
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

  const pages = generatedRoutes.sort((p1, p2) => {
    if (p1.name < p2.name) {
      
    }
  })

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

<img src="~/source/figures/homePageNow.png"></img>

Voici, ci-dessus le rendu final de la page d'accueil, pour le site interactif.

Les premiers composants quasar qui nous intéressent, servent à former l'aspect visuel du site, comme par exemple l'en-tête du site, ainsi que le menu déroulant sur la gauche de l'écran. Il y a également les liaisons pour naviguer entre les différentes sections du cours.

## Composants *Quasar* pour former les paramètre par défaut du site

### En-tête

#### *q-layout*

Le document *default.vue* contient, tout d'abord le plan de la page. C'est à dire, que le composant va former la page, comme si elle est séparée en un tableau de trois parties sur trois.

<img src="~/source/figures/layout.png"></img>

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

#### *q-header*

Ensuite, le composant *q-header* permet de configurer l'en-tête comme ceci :

```HTML
<q-header elevated class="bg-primary text-white text-left">
  <!-- ... -->
</q-header>
```

Dans ce cas de figure, le contenu qui se trouve entre les guillemets de *class*, exprime les propriétés de l'en-tête. Par exemple, *bg-primary* est la couleur de l'arrière plan. *text-white* donne la couleur du texte et *text-left* donne l'alignement du texte de l'en-tête.

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

Le lien du routeur, *router-link* permet, lorsque la constante *drawerLeft* est vrai, de changer de page, sans devoir recharger le site, grâce au paramètre :
```HTML
to="..."
```

Dans ce cas, la destination est "/". Il est configuré que "/" est la page d'index du site, autrement dit, la page d'accueil."

### Menu déroulant

#### *q-drawer*



#### *q-list*



#### *q-item/q-item-section*



### Contenu de la page

#### *q-page-container*



#### *q-page-scroller*



## Q-carousel/q-carousel-slide

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