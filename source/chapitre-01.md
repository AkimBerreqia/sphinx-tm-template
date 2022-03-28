# 1. Cheminement projet

## Présentation du projet

#### Parcours de l'étudiant

L'étudiant n'aura pas besoin de savoir beaucoup de notions sur la cryptographie pour participer au cours. Il devra seulement avoir les notions de base des cours d'informatique sur la programmation en python.

Le chiffre de César, l'attaque par force brute, ainsi que le chiffrement par substitution monoalphabétique seront abordés au fur et à mesure que l'étudiant avance dans le cours.

Le travail de l'élève sera de traverser les différentes pages théoriques et pratiques, qui seront illustrées par des exercices interactifs.

#### Procédure

Les technologies de développement du projet comportent <i>le Javascript</i>, <i>l'<i>HTML</i></i>, <i>le CSS</i>, et <i><i>Quasar</i></i> au travers de <i>VueJS</i> qui sert également à héberger le projet. Une grande partie des recherches du développement du code a été faite à partir d'informations réunies sur internet et qui sont sourcées directement dans les documents <i>.vue</i>, ou à partir d'informations provenant de livres, qui abordent le domaine de la cryptologie.

La partie écrite du travail de maturité est rédigée depuis GitPod.io avec le langage de programmation LaTeX, qui suit la documentation Sphinx. Il y a également un dépôt GitHub, qui sert à suivre l'évolution du projet.

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionne les composants VueJS et <i>Quasar</i>.

Ce sont des outils de fabrication de site qui pour le premier, simplifie la manière d'écrire le code à écrire, tout en prenant en charge plusieurs langage de programmation sur le même document (<i>HTML</i>, CSS et <i>Javascript</i>), et pour le second, <i>Quasar</i> rend le code plus dynamique.

Pour <i>Quasar</i>, l'outil met à disposition des composants libre de droit, qui peuvent être modifier pour plaire à chacun.

# 2. Objectifs

Le projet a pour but d'apporter un aspect plus neuf au site de Donner Cédric, pour le cours sur la cryptologie, afin qu'il soit plus simple aux élèves du Collège du Sud d'apprendre ce domaine, de manière plus ludique.

# 3. Concepts de base utilisés Quasar/VueJS

## Q-layout/q-header/q-toolbar/q-drawer/router-link/to="..."/q-list/q-item/q-item-section/q-page-container/router-view/q-page-scroller

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



# 2. Outils interactifs avec <i>Quasar</i>

```{admonition} Information
Il fallait plusieurs moyens pour que l'utilisateur puisse interagir avec une panoplie de possibilité. Il y a donc plusieurs outils <i>Quasar</i> qui ont été exploités pour cela.
```

Les outils <i>Quasar</i> sont des outils utilisés en <i>HTML</i> et qui peuvent être combiner avec des outils <i>VueJS</i>.

## q-btn
C'est un bouton qui est préfabriqué par <i>Quasar</i>. Il est très utile pour avoir moins de code et pour gagner du temps. Il est très souvent combiné à d'autres outils <i>Quasar</i>.

```<i>HTML</i>

<q-btn
  label="Afficher la réponse"
  color="..."
  @click="..."
/>
```

## q-carousel

Un "carousel" est une sorte de carte, dans laquelle il est possible de mettre ce que l'on souhaite.

```<i>HTML</i>

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

<i>Quasar</i> propose des banières et des menus personnalisables pour préfaire un site. Il ne manque plus qu'à rajouter le contenu.

Pour notre site de cours, il y a tout d'abord une entête, avec le nom du cours et un bouton qui affiche une barre de menu sur la gauche de l'écran.

<!--A modifier par rapport au site.-->

```<i>HTML</i>

<q-layout view="hHh lpR fFf">

  <q-header elevated class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />

      <q-toolbar-title>
        <q-avatar>
          <img src="https://cdn.<i>Quasar</i>.dev/logo-v2/svg/logo-mono-white.svg">
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
          <img src="https://cdn.<i>Quasar</i>.dev/logo-v2/svg/logo-mono-white.svg">
        </q-avatar>
        <div>Title</div>
      </q-toolbar-title>
    </q-toolbar>
  </q-footer>

</q-layout>
```

Il est possible de trouver un template complet qui permet de commencer avec une base de site, qui contient plusieurs exemples <i>Quasar</i>, pouvant être utilisés si nécessaire.

# 4. Structure du site

Pour la première page, il s'agit d'une introduction à la cryptographie. Il n'y a rien d'intéressant au niveau du code à présenter, car cette page est seulement écrite en <i>HTML</i>.

Pour ce qui est de la deuxième page, il y a déjà plus de matière. Cette section présente le chiffre César, en commençant par un exercice qui confronte l'utilisateur face à un texte chiffré et il doit écrire le texte clair, avec quelques indices.