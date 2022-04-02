# 3. Développement d'outils interactifs

## Composants *Quasar* utilisés pour former les pages du site

#### Q-btn/q-separator (valider la section)

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

Pour conclure de façon visuelle, il y a une barre de séparation, qui est mise à la suite du dernier bouton de validation.

```HTML
<q-separator inset />
```

En ce qui concerne le dernier aspect basé sur la formation, il est combiné à d'autres outils pour composer des exercices, dans lesquels, l'utilisateur doit écrire du texte. Cet utilité est développé dans la prochaine section.

### Système d'exercices "respondAnswer"

Voici un des exercices, qui figure au chapitre "1.2 Le chiffre de César" du site :

```{figure} ../source/figures/respondAnswerExo.png
---
width: 50%
---
```

```HTML
<template>
  <q-page class="pa-4">
    <p>
    Rodolphe utilise la même méthode de chiffrement que Robert pour chiffrer un message. 
    Voici le message chiffré qu’il envoie à Julie. 
    Essayez de déchiffrer ce message:
    </p><br>
    
    <p class="text-center bg-info rounded-borders">
    KFUJOWJUFBVDJOFNBEFNBJOTPJSBWJOHUIFVSFTSFKPJOTNPJBMBHBSF
    </p><br>

    <div class="q-pa-md">
      <div class="q-gutter-y-md column" style="max-width: 1050px">
        <q-input bottom-slots v-model="myQuestions.rodolphe" label="Réponse :" counter maxlength="56" :dense="dense" style='text-transform:uppercase'>
          <template v-slot:hint>
            <p>{{respondAnswer(myQuestions.rodolphe, myQuestions.rodolpheCorrectAnswer, 56)}}</p>
          </template>
        </q-input>
      </div>
    </div>
    
    <q-btn-group unelevated rounded>
      <q-btn label="INDICES" color="accent" @click="dialogVisible.indice1 = true" />

      <q-dialog v-model="dialogVisible.indice1" @hide="onHide">
      <q-card>
        <q-card-section class="row items-center q-pb-none">
        <strong class="text-h6" style="color:accent;">Q-Rodolphe: Indices</strong>
        <q-space />
        </q-card-section>

        <q-card-section style="color:accent;">
        <ul style="color:accent;">
          <li>Toutes les lettres se suivent sans espace.</li><br>
          <li>Il te sera plus simple de décrypter cette phrase en te servant d'une feuille et d'un crayon.</li><br>
          <li>Le début du texte en clair est : "<strong>JETINVITE</strong>".</li>
        </ul>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="ok" color="primary" v-close-popup @click="dialogVisible.indice1 = false" />
        </q-card-actions>
      </q-card>
      </q-dialog>

      <q-btn label="AFFICHER LA RÉPONSE" color="orange" @click="dialogVisible.respond2 = true" />

      <q-dialog v-model="dialogVisible.respond2" @hide="onHide">
      <q-card>
        <q-card-section class="row items-center q-pb-none">
        <strong class="text-h6" style="color:orange;">Q-Rodolphe: Réponse</strong>
        <q-space />
        </q-card-section>

        <q-card-section style="color:orange;">
        <strong>JETINVITEAUCINEMADEMAINSOIRAVINGTHEURESREJOINSMOIALAGARE</strong>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="ok" color="primary" v-close-popup @click="dialogVisible.respond2 = false" />
        </q-card-actions>
      </q-card>
      </q-dialog>
    </q-btn-group>
  </q-page>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'

let dialogVisible = reactive({
  respond2: ref(false),
  indice1: ref(false)
})

function onHide(order) {
  dialogVisible.order.value = false
}

const dense = ref(false)

const myQuestions = reactive({
  rodolphe: '',
  rodolpheCorrectAnswer: 'JETINVITEAUCINEMADEMAINSOIRAVINGTHEURESREJOINSMOIALAGARE'
})

function respondAnswer(exercice, correctAnswer, maxLength){

  if (exercice.length === maxLength) {
    if (exercice.toUpperCase() === correctAnswer) {
      return "Bonne réponse"
    }
    else if (exercice.toUpperCase() !== correctAnswer) {
      return "Mauvaise réponse"
    }
  }

  else if (exercice.length !== maxLength) {
    return "..."
  }
}
</script>
```

Cette outil fonctionne de la manière suivante, l'utilisateur peut rentrer un nombre limité de caractères à l'intérieur de la zone de texte. Dans ce cas ci-dessus, il peut rentrer au maximum cinquante-six caractères. Pour l'exercice, la réponse est écrite directement en majuscule, grâce à la fonction *.toUpperCase()*. La réponse de l'étudiant ne doit pas contenir d'espace, sinon il n'aura pas suffisamment de place pour écrire toute la réponse. Si l'élève a des difficultés, il peut se servir du bouton "INDICES" pour s'aider. Une fois que la réponse est complète, l'utilisateur peut voir si sa réponse est correcte.

```{figure} ../source/figures/goodAnswer.png
```

```{figure} ../source/figures/wrongAnswer.png
```

#### Q-dialog/q-card/q-card-section/q-card-actions

#### Q-btn-group

L'usage de ce dernier type de bouton est illustré avec le composant *q-dialog*, qui permet de faire apparaitre une fenêtre/un "pop-up" à l'écran.

```{figure} ../source/figures/btnGroup.png
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

Chacun des deux *dialogs* a une couleur différente qui leur a été attribuée de manière arbitraire, pour différencier l'utilité de chaque bouton.
Les boutons oranges sont destinés au réponse et ceux qui sont violets servent à donner des indices.



## Directives *VueJS* utilisées pour former les pages du site

### V-html/import json file



### Q-input/v-model/respondAnswer(exercice, correctAnswer, maxLength)



### Quiz/myQuizQuestions



### Iframe



### Q-table/search/lexique/terme/signification/rows



### Library

