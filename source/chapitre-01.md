# 1. Outils interactifs

```{admonition} Information
Il fallait plusieurs moyens pour que l'utilisateur puisse interagir avec une panoplie de possibilité. Il y a donc plusieurs outils qui ont été faits pour cela.
```

## Carousel

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
        class="bg-info text-white shadow-1 rounded-borders"
      >
        <q-carousel-slide name="cryptographie1" class="column no-wrap flex-center text-center">
            <!-- ... -->
        </q-carousel-slide>

        <q-carousel-slide name="cryptographie2" class="column no-wrap flex-center text-center">

            <!-- ... -->

        </q-carousel-slide>
      </q-carousel>