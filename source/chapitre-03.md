# 3. Développement d'outils interactifs

## Composants *Quasar* utilisés pour former les pages du site

#### Q-btn/q-btn-group/q-separator (valider section)

Le composant *q-btn* a plusieurs usages, pour le site interactif. Certains cas ont déjà été mentionnés, comme pour le bouton qui fait défiler vers le haut de la page, ou alors celui pour changer de page. Jusqu'à maintenant, *q-btn* a servit à mettre en mouvement la page. Pour les fonctions qui suivent, les deux prochains rôles du *q-btn* sont plutôt orientés sur un aspect de progression et de formation.

Pour ce qui est de l'aspect de progression, un système de validation de section est mis en place avec un nouveau bouton, "VALIDER LA SECTION".

```{figure} ../source/figures/validatorBtnInSection.png
---
width: 50%
---
```

Une fois que l'utilisateur appuie sur ce bouton bleu, ce dernier devient vert, avec comme label, "SECTION VALIDÉE".

```{figure} ../source/figures/twoValidatorBtn.png
```

En réalité, il y a constamment deux boutons.

```html
<template>
    <q-btn unelevated rounded label="Valider la section" v-if="section === false" class="align-right" color="primary" @click="section = !section"/>
    <q-btn unelevated rounded label="Section validée" v-if="section === true" class="align-right" color="green" @click="section = !section"/>
</template>

<script setup lang="ts">
import { ref } from 'vue'

let section = ref(false)
</script>
```

En se servant de la directive *v-if*, il est possible de choisir quand est-ce que l'un des deux boutons doit apparaitre à l'écran.

Dès que l'utilisateur clique sur le bouton visible, la valeur de *section* est inversée, pour cacher le bouton visible et inversément pour le bouton invisible.

En ce qui concerne le dernier aspect basé sur la formation, il est combiné à d'autres outils, pour composer dans exercices, dans lesquels, l'utilisateur doit écrire du texte.

#### Q-dialog/q-card/q-card-section/q-card-actions

L'usage de ce dernier type de bouton est illustré dans cette section, avec le composant *q-dialog*, qui permet de faire apparaitre une fenêtre/un "pop-up" à l'écran.

```{figure} ../source/figures/respondAnswerExo.png
---
width: 50%
---
```

Dans l'image ci-dessus, les boutons "INDICES" et "AFFICHER LA RÉPONSE" vont faire apparaitre un "pop-up" différent, suivant lequel des deux est enclenché.

```{figure} ../source/figures/indices.png
---
width: 50%

---
```

```{figure} ../source/figures/reponse.png
---
width: 50%
---
```

Chacun des deux *dialog*, ils ont une couleur différente qui leur a été attribuée de manière arbitraire

## Directives *VueJS* utilisées pour former les pages du site

### V-html/import json file



### Q-input/v-model/respondAnswer(exercice, correctAnswer, maxLength)



### Quiz/myQuizQuestions



### Iframe



### Q-table/search/lexique/terme/signification/rows



### Library

