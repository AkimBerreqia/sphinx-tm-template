# 1. Outils interactifs avec quasar

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

