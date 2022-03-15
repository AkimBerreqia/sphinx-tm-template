# 1. Cheminement projet

Pour arriver à ce projet, il a fallu passer par plusieurs étapes.

Tout d'abord, il a fallu apprendre comment fonctionne les composants VueJS et quasar.

Ce sont des outils de fabrication de site qui pour le premier, abrège le code à écrire, et pour le second, rend le code plus dynamique.

Pour quasar, l'outil met à disposition des composants libre de droit, qui peuvent être modifier pour plaire à chacun.

# 2. Outils interactifs avec quasar

```{admonition} Information
Il fallait plusieurs moyens pour que l'utilisateur puisse interagir avec une panoplie de possibilité. Il y a donc plusieurs outils quasar qui ont été exploités pour cela.
```

Les outils quasar sont des outils utilisés en html et qui peuvent être combiner avec des outils vue.

## q-btn
C'est un bouton qui est préfabriqué par quasar. Il est très utile pour avoir moins de code et pour gagner du temps. Il est très souvent combiné à d'autres outils quasar.

```html

<q-btn
  label="Afficher la réponse"
  color="..."
  @click="..."
/>
```

## q-carousel

Un "carousel" est une sorte de carte, dans laquelle il est possible de mettre ce que l'on souhaite.

```html

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

Quasar propose des banières et des menus personnalisables pour préfaire un site. Il ne manque plus qu'à rajouter le contenu.

Pour notre site de cours, il y a tout d'abord une entête, avec le nom du cours et un bouton qui affiche une barre de menu sur la gauche de l'écran.

<!--A modifier par rapport au site.-->

```html

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

Il est possible de trouver un template complet qui permet de commencer avec une base de site, qui contient plusieurs exemples quasar, pouvant être utilisés si nécessaire.

# 4. Structure du site

Pour la première page, il s'agit d'une introduction à la cryptographie. Il n'y a rien d'intéressant au niveau du code à présenter, car cette page est seulement écrite en html.

Pour ce qui est de la deuxième page, il y a déjà plus de matière. Cette section présente le chiffre César, en commençant par un exercice qui confronte l'utilisateur face à un texte chiffré et il doit écrire le texte clair, avec quelques indices.