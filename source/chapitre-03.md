# 3. Développement d'outils interactifs

## Système de validation de section

### v-if, q-btn et q-separator

Le composant *q-btn* a plusieurs usages pour le site interactif. Certains cas ont déjà été mentionnés, comme pour le bouton qui fait défiler vers le haut de la page, ou alors celui pour changer de page. Jusqu'à maintenant, *q-btn* a servi à mettre en mouvement la page. Pour les fonctions qui suivent, les deux prochains rôles du *q-btn* sont plutôt orientés sur un aspect de progression et de formation.

Pour ce qui est de l'aspect de progression, un système de validation de section est mis en place avec un nouveau bouton, "VALIDER LA SECTION".

```{figure} ../source/figures/validatorBtnInSection.png
---
width: 50%
---
figure n°8
```

Une fois que l'utilisateur appuie sur ce bouton bleu, ce dernier devient vert, avec comme label, "SECTION VALIDÉE".

```{figure} ../source/figures/twoValidatorBtn.png
figure n°9
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
[^quasarSource]

En se servant de la directive *v-if*, il est possible de choisir quand est-ce que l'un des deux boutons doit apparaitre à l'écran.

Dès que l'utilisateur clique sur le bouton visible, la valeur de *section* est inversée, pour cacher le bouton visible et inversement pour le bouton invisible.

Pour conclure chaque section, il y a une barre de séparation, qui est mise à la suite du dernier bouton de validation.

```HTML
<q-separator inset />
```
[^quasarSource2]

En ce qui concerne le dernier aspect basé sur la formation, il est combiné à d'autres outils pour composer des exercices, dans lesquels, l'utilisateur doit écrire du texte. Cette utilité est développée dans la prochaine section.

## Système d'exercices "respondAnswer"

Voici un des exercices du site, qui figure au chapitre "1.2 Le chiffre de César" :

```{figure} ../source/figures/respondAnswerExo.png
---
width: 50%
---
figure n°10
```

Cet outil fonctionne de la manière suivante, l'utilisateur peut rentrer un nombre limité de caractères à l'intérieur de la zone de texte. Dans ce cas ci-dessus, il peut rentrer au maximum cinquante-six caractères. Pour ce type d'exercice, la réponse est écrite directement en majuscule, grâce à la fonction *.toUpperCase()*. La réponse de l'étudiant ne doit pas contenir d'espace, sinon il n'aura pas suffisamment de place pour écrire toute la réponse. Si l'élève a des difficultés, il peut se servir du bouton "INDICES" pour s'aider. Une fois que la réponse est complète, l'utilisateur peut voir si son résultat est correct.

```{figure} ../source/figures/goodAnswer.png
figure n°11
```

```{figure} ../source/figures/wrongAnswer.png
figure n°12
```

### q-btn-group, q-dialog, q-card, q-card-section et q-card-actions

Pour la partie formation, il y a deux choix possibles de boutons. Soit il s'agit d'un seul bouton, soit il s'agit d'un groupe de plusieurs boutons. Pour cette deuxième situation, le composant *q-btn-group* permet de regrouper plusieurs boutons dans un seul cadre.

```{figure} ../source/figures/btnGroupExemple.png
figure n°13
```

```HTML
<q-btn-group rounded elevated>
  <q-btn color="green" label="btn n° 1"></q-btn>
  <q-btn color="blue" label="btn n° 2"></q-btn>
</q-btn-group>
```
[^quasarSource3]

Dans l'image ci-dessous, les boutons "INDICES" et "AFFICHER LA RÉPONSE" font apparaitre un "pop-up" différent, suivant lequel des deux est enclenché.

```{figure} ../source/figures/btnGroup.png
figure n°14
```

Pour le cours, ce genre de boutons est combiné avec le composant *q-dialog*, qui fait apparaitre une fenêtre/un "pop-up" à l'écran. Cette fenêtre est une *q-card*.

```{figure} ../source/figures/indices.png
---
width: 50%
---
figure n°15
```

```{figure} ../source/figures/reponse.png
---
width: 50%
---
figure n°16
```

Chaque carte est composée d'un titre et d'explications. Ces parties sont des sections/*q-card-section*.

```HTML
<!-- ... -->

<!-- q-btn content -->

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
  
  <!-- q-card-actions content -->

</q-card>
</q-dialog>

<!-- q-btn content -->

<q-dialog v-model="dialogVisible.respond2" @hide="onHide">
<q-card>
  <q-card-section class="row items-center q-pb-none">
  <strong class="text-h6" style="color:orange;">Q-Rodolphe: Réponse</strong>
  <q-space />
  </q-card-section>

  <q-card-section style="color:orange;">
  <strong>JETINVITEAUCINEMADEMAINSOIRAVINGTHEURESREJOINSMOIALAGARE</strong>
  </q-card-section>

  <!-- q-card-actions content -->

</q-card>
</q-dialog>

<!-- ... -->
```
[^quasarSource4]

Lorsque l'un des deux boutons est pressé, la fonction "onHide" se lance et le dialogue se met en marche.

```JavaScript
let dialogVisible = reactive({
  respond2: ref(false),
  indice1: ref(false)
})

function onHide(order) {
  dialogVisible.order.value = false
}
```

Il reste encore les *q-card-actions* à aborder. Ce sont les boutons avec le label "OK", à l'intérieur des cartes. Ils servent à faire disparaitre la fenêtre ouverte, en rendant fausse la valeur de la variable qui est attribuée au dialogue concerné.

Chacune des deux cartes a une couleur différente qui leur a été attribuée de manière arbitraire, pour différencier l'utilité de chaque bouton.

Le bouton orange est destiné aux réponses et celui qui est violet sert à donner des indices. Ce sont les seules variétés de boutons qui existent dans le cours, pour afficher une fenêtre.

### q-input et fonction "respondAnswer"

Pour cette dernière partie de section, le composant *q-input* met en place une zone de texte qui renvoie à l'utilisateur si sa réponse est juste ou fausse, grâce à la fonction "respondAnswer".

Ce *q-input* provient d'un des exemples présents dans la documentation *Quasar*.

```{figure} ../source/figures/inputExemple.png
figure n°17
```

```HTML
<template>
  <q-input v-model="ph" label="Label" placeholder="Placeholder" hint="With placeholder" :dense="dense" />
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      text: ref(''),
      ph: ref(''),
      dense: ref(false)
    }
  }
}
<script>
```
[^inputSource]

L'exemple utilisé se nomme "Placholder", car il contient un emplacement intéressant pour renvoyer à l'élève sont résultat.

Le code ressemble maintenant à cela :

```HTML
<template>
  <!-- ... -->

  <q-input bottom-slots v-model="myQuestions.rodolphe" label="Réponse :" counter maxlength="56" :dense="dense" style='text-transform:uppercase'>
    <template v-slot:hint>
      <p>{{respondAnswer(myQuestions.rodolphe, myQuestions.rodolpheCorrectAnswer, 56)}}</p>
    </template>
  </q-input>

  <!-- ... -->
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'

// ...

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
[^quasarSource5]

La fonction prend ce que l'utilisateur écrit, pour contrôler le nombre de caractères qu'il y a. Pour la fonction, il s'agit "d'exercice". Si le nombre de caractères n'est pas égal au maximum requis, la fonction renvoie "..." dans l'espace réservé au résultat. Si la longueur maximale est atteinte, alors la fonction renvoie soit "Bonne réponse", si "correctAnswer" est pareil que "exercice". Mais si "correctAnswer" et "exercice" sont différents, alors la fonction renvoie "Mauvaise réponse". Pour l'exercice avec Rodolphe, "exercice" fait référence à "myQuestions.rodolphe", "correctAnswer" correspond à "myQuestions.rodolpheCorrectAnswer" et finalement "maxLength" fait cinquante-six caractères.

## Importer du texte avec *JSON*

Après avoir développé la version finale du projet, Monsieur Cédric Donner m'a demandé de stocker le texte dans un fichier *JSON*, pour la page "1.1" du prototype et de la version finale. Ceci permet de diminuer énormément le contenu de chaque document. Le nom du fichier qui stocke le texte du chapitre "1.1" se nomme actuellement "introContent.json".

```JSON
{
  "introduction": {
    "presentation": "La cryptologie est la science des codes secrets et utlise des techniques propres à l’informatique et aux mathématiques. Dans ce cours, nous n’aborderons pas les aspects mathématiques des techniques de cryptographie modernes. La cryptologie englobe d’une part la <b>cryptographie</b> qui consiste à développer des codes secrets permettant de chiffrer des messages pour qu’ils soient incompréhensibles pour les personnes à qui ils ne sont pas destinés et la <b>cryptanalyse</b> qui consiste à <i>casser les codes secrets</i> utilisés par d’autres personnes pour tenter d’accéder aux informations chiffrées.",

    "cryptographie1": "Les codes secrets sont utilisés depuis l’invention de l’écriture pour communiquer des informations de manière secrète et sécurisée, notamment lors des grandes campagnes militaires. Le code de César est un exemple assez simple utilisé dans l’Antiquité que nous allons aborder au cours.",

    "cryptographie2": "Plus le nombre d’informations représentées sous forme digitale a augmenté, plus les codes secrets ont gagné en importance. Depuis l’avènement des technologies de télécommunication telles que la radio ou le télégraphe, les codes secrets jouent un rôle majeur pour le commerce et sur le champ de bataille. Le commerce électronique (e-commerce) ou les réseaux sociaux ne seraient absolument pas possibles sans les avancées modernes de la cryptographie, notamment le code RSA. À chaque fois que vous vous rendez sur un réseau social ou que vous effectuez un achat en ligne, vous utilisez des techniques modernes de cryptographie pour chiffrer les communications avec le serveur, permettant d’éviter que des tiers se procurent les informations communiquées ou ne détournent le paiement effectué.",

    "cryptanalyse1": "Depuis l’avènement de la cryptographie, qui vise à communiquer ou stocker des informations sensibles de manière chiffrée pour les rendre inintelligibles, les personnes désireuses d’accéder à ces informations chiffrées ont du chercher des stratégies pour casser ces codes secrets. Comme nous le verrons, les codes secrets élaborés durant l’Antiquité sont tous relativement faciles à casser, du moins avec la puissance de calcul des ordinateurs actuels.",

    "cryptanalyse2": "Lors de la deuxième guerre mondiale, une des raisons principales de la victoire des alliés sur la Wehrmacht est que les Anglais ont réussi à casser le code Enigma utilisé par les Allemands dans toutes leurs communications militaires.",

    "cryptanalyse3": "Les techniques de cryptographie modernes permettent de créer des codes secrets beaucoup plus difficiles à casser. C’est la raison pour laquelle toutes les grandes puissances commerciales et militaires actuelles dépensent des sommes colossales pour engager les meilleurs mathématiciens, physiciens et informaticiens du monde et financer les services secrets responsables de percer les codes secrets utilisés par les adversaires pour en tirer un avantage commercial ou militaire.",

    "cryptanalyse4": "Dans ce cours, vous allez découvrir quelques-uns des codes secrets les plus célèbres inventés dans l’Antiquité. Vous pourrez ainsi renforcer les compétences de programmation avec les chaînes de caractères."
  }
}
```

### v-html

A partir de ce point, il faut importer le document *JSON* dans les fichiers "1.1". Pour cela, la démarche suivante est faite :

```JavaScript
import content from 'src/json/introContent.json'

const contentData = ref(content.introduction)
```

De cette manière, la directive *v-html* est utilisée.

```HTML
<p v-html="contentData.presentation"></p>
```
[^vueSource]

Cette directive remplie le même rôle que la fonction *innerHTML*.

Il aurait été plus facile de simplement écrire comme ci-dessous.

```HTML
<p>{{contentData.presentation}}</p>
```

Cependant, le problème est que dans le contenu *JSON*, il y a des balises *HTML*, comme : "\[...] la \<b>cryptanalyse\</b> qui consiste à \<i>casser les codes secrets\</i> utilisés par \[...]". Dans ce cas de figure, les balises *\<b>* et *\<i>* posent problèmes, car si la deuxième possibilité est exécutée, les balises seraient inclues dans le texte et une fois sur le site, les balises apparaitraient à l'écran.

A contrario, la première possibilité permet de ne pas interpréter le contenu *JSON* comme du texte. Cela mène à garder la propriété des balises citées précédemment et donc d'avoir du texte en gras et en italique, aux endroits souhaités.

## Système de quiz "myQuizQuestions"

```{Admonition} A savoir
Le code qui compose le quiz est très fortement inspiré d'un code déjà existant, qui se trouve dans un tutoriel, pour apprendre à faire un quiz en *JavaScript* (lien vers le site : [https://simplestepscode.com/javascript-quiz-tutorial/](https://simplestepscode.com/javascript-quiz-tutorial/)).
```

Les quiz font partie du deuxième système créé pour que l'élève puisse apprendre en s'exerçant. Ce système possède une structure assez simple.

```{figure} ../source/figures/quiz.png
figure n°18
```

Il y a tout d'abord le titre du quiz, en haut à gauche. Puis, tout le contenu de l'exercice est centré dans la page. Ce contenu est composé d'une numérotation pour la question en cours. En dessous, vient se rajouter la problématique posée, avec trois choix de réponses. Et enfin, la dernière partie du quiz est consacrée à plusieurs boutons.

Pour ces boutons, chacun d'entre eux a une attribution différente. "PRÉCÉDENT" renvoie à la question précédente, mais si l'utilisateur se trouve à la première question du quiz, le bouton est inaccessible pour l'élève. Ensuite, le bouton "SUIVANT" fonctionne exactement comme le premier bouton, mais pour passer à la question suivante. Le troisième bouton se nomme "VALIDER" et il affiche le résultat de l'utilisateur.

```{figure} ../source/figures/quizCorrect.png
figure n°19
```

```{figure} ../source/figures/quizWrong.png
figure n°20
```

Il existe un quatrième bouton qui s'appelle "RECOMMENCER".

```{figure} ../source/figures/quizRestart.png
figure n°21
```

Son usage est de ramener au début du quiz, pour le refaire si besoin. Il s'affiche dès que l'utilisateur a dépassé la première question.

Pour ce qui est du code, la constante "myQuizQuestions" contient tous les éléments importants, pour la formation du quiz.

```JavaScript
import { ref, reactive } from "vue"

const myQuizQuestions = reactive([
  {
    id: ref(0),
    question: "What is 10/2?",
    answers: {
      a: '3',
      b: '5',
      c: '115'
    },
    choice: ref(''),
    correctAnswer: '5'
  },
  {
    id: ref(1),
    question: "What is 30/3?",
    answers: {
      a: '3',
      b: '5',
      c: '10'
    },
    choice: ref(''),
    correctAnswer: '10'
  }
])
```
[^quizSource]

L'"id" permet de donner le numéro de question.

```HTML
<h2>Question numéro {{index + 1}}</h2>
```

Cet élément est aussi utile pour faire apparaitre à l'écran les questions et réponses voulues.

```HTML
<template>
  <!-- ... -->
      <div class="q-pa-md">
        <div v-for="(value, key) in question.answers" class="q-gutter-sm">
          <q-radio v-model="answers[index]" :key="key" :val="value" :label="value"/>
        </div>
        
        <div v-show="isClick === true">
          <div v-if="myQuizQuestions[index].correctAnswer === answers[index]">
            <p class="q-px-sm" style="color:green;">Bonne réponse</p>
          </div>

          <div v-else>
            <p class="q-px-sm" style="color:red;">Mauvaise réponse</p>
          </div>
        </div>
      </div>
  <!-- ... -->
</template>

<script setup lang="ts">
// ...

const answers = reactive([])

// ...
</script>
```
[^quasarSource6]

Pour donner le résultat à l'utilisateur, la constante "answers" stocke la réponse enregistrée par l'élève. Cette réponse est vérifiée pour choisir quel résultat il faut afficher à l'écran.

```HTML
<div v-show="index === counter" v-for="(question, index) in myQuizQuestions" :key="question.id">
  <h2>Question numéro {{index + 1}}</h2>

  <p class="question">
  {{question.question}}
  </p>

  <div class="q-pa-md">
    <div v-for="(value, key) in question.answers" class="q-gutter-sm">
      <q-radio v-model="answers[index]" :key="key" :val="value" :label="value"/>
    </div>
    
    <div v-show="isClick === true">
      <div v-if="myQuizQuestions[index].correctAnswer === answers[index]">
        <p class="q-px-sm" style="color:green;">Bonne réponse</p>
      </div>

      <div v-else>
        <p class="q-px-sm" style="color:red;">Mauvaise réponse</p>
      </div>
    </div>   
  </div>  
</div>
```
[^quizSource2]

Tout ce qui est compris dans cette partie du code dépend de la constante "counter".

```JavaScript
const counter = ref(0)
```

Les éléments de "myQuizQuestions" qui figurent dans le code *HTML* ci-dessus sont remplacés par d'autres éléments appartenant à "myQuizQuestions", lorsque l'utilisateur change de question. L'index correspond à l'"id" dans la boucle *v-for* et il permet cette variation d'éléments. Par exemple, pour que la deuxième question apparaisse à l'écran, il faut que l'"id"/index de la question ait la même valeur que le compteur. Dans ce cas-ci, la valeur des deux paramètres doit être égale à un.

```HTML
<div v-show="index === counter" v-for="(question, index) in myQuizQuestions" :key="question.id">
  <!-- div content -->
</div>
```
[^vueSource2]

Il ne reste plus qu'à faire varier le compteur, pour changer de question. Voici donc l'intérêt des boutons "PRÉCÉDENT", "SUIVANT" ET "RECOMMENCER". Le premier fait baisser d’un la valeur de "counter". Le deuxième rajoute un à la valeur de la constante et le troisième l'initie à zéro. Ces boutons se servent des fonctions suivantes pour procéder :

```JavaScript
function restart() {
  counter.value = 0
  isClick.value = false
}

function next() {
  counter.value++
  isClick.value = false
}

function previous() {
  counter.value--
  isClick.value = false
}
```

Ces fonctions sont liées aux boutons de la manière suivante :

```HTML
<q-btn-group>
  <q-btn :disable="counter === 0" label="Précédent" @click="previous()"/>
  <q-btn :disable="counter === 1" label="Suivant" @click="next()"/>
  <q-btn v-if="counter > 0" label="Recommencer" @click="restart()"/>
  <q-btn label="Valider" @click="changeClick()"/>
</q-btn-group>
```
[^quasarSource7]

Il reste encore à traiter la validation des réponses. Le bouton "VALIDER" a pour but de faire apparaitre le résultat. Les autres boutons possèdent tous dans leurs fonctions respectives "isClick.value = false". Cela sert à faire disparaitre le résultat du quiz, car sinon il resterait affiché tant que le bouton "VALIDER" n'est pas réutilisé. De cette manière, dès que la question change, le résultat n'est plus affiché.

```JavaScript
const isClick = ref(false)

function changeClick() {
  isClick.value = !isClick.value
}
```

## Système de recherche par mots-clés "library"

```{Tip}
Cet outil sera intégré dans le document "default.vue", quand tout le contenu du cours sera en format *JSON*. L'outil pourra puiser à l'intérieur de ce dernier, pour fonctionner avec chaque page du cours.
```

```{Admonition} A savoir
Le code est inspiré d'un exemple se trouvant sur le site de documentation *Quasar*. Il s'agit d'une liste de différents desserts, avec des indications différentes. Il est possible de rechercher un des desserts, dans une zone de texte dédiée à cela. Une fois la recherche effectuée, il ne reste que les résultats de cette recherche affichés à l'écran (lien vers l'exemple : [https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns](https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns)).
```

Le chapitre "1.6" du cours se sert déjà de l'exemple *Quasar* mentionné précédemment. Le code a été adapté pour servir de lexique à la cryptologie.

Pour comparer les deux visuels entre le lexique et la bibliothèque, voici un rendu de chacun :

```{figure} ../source/figures/lexique.png
figure n°22
```

```{figure} ../source/figures/library.png
figure n°23
```

### Lexique

Pour le premier, les constantes "terme" et "signification" contiennent les titres et les définitions du lexique.

```JavaScript
const terme = [
  'Cryptographie',
  'Cryptanalyse',
  'Cryptologie',
  'Chiffre',
  'Texte en clair',
  'Texte chiffré',
  'Chiffrer / crypter',
  'Déchiffrer / décrypter',
  'Clé de chiffement',
  'Chiffre par substitution monoalphabétique'
]

const signification = [
  'Art d’inventer et d’appliquer des méthodes de chiffrement (codes secrets) sûrs et pratiques d’utilisation. Il s’agit aussi de vérifier et de prouver la sécurité des codes secrets utilisés / proposés.',
  'Art de casser des codes secrets, à savoir déchiffrer des messages chiffrés sans connaître la clé de déchiffrement et / ou la méthode de chiffrement utilisée.',
  'Science des codes secrets qui regroupe la cryptographie ou la cryptanalyse. La cryptologie consiste donc autant à inventer des codes secrets qu’à essayer de casser les codes secrets d’autres personnes.',
  'Un chiffre est un code secret particulier, par exemple le Chiffre de César, le chiffre de Polybe ou le chiffre de Vigenère',
  'Le texte en clair est le message à chiffrer, lisible par tout le monde.',
  'Le texte chiffré est illisible',
  'Transformer un texte en clair en son équivalent chiffré.',
  'Rétablir le texte en clair à partir d’un message chiffré',
  'Pour pouvoir déchiffrer un message, il faut connaître le chiffre à l’aide duquel il a été chiffré (généralement très connu) ainsi qu’une information secrète supplémentaire appelée clé de chiffrement ou tout simplement clé.',
  'Un chiffre par substitution monoalphabétique est un code secret dans lequel chaque caractère du message en clair est remplacé par une autre lettre. Le chiffre de César est un exemple classique de chiffre monoalphabétique qui décale simplement les lettres d’un certain nombre de positions dans l’alphabet.'
]
```

Grâce à l'instruction suivante, chaque titre et définition qui vont de pair, sont introduits en liste dans la constante "rows".

```Javascript
const rows = []

terme.forEach(titleName => {
  rows.push({ titleName: titleName, articleName: signification[terme.indexOf(titleName)] })
})
```
[^lexiqueSource]

De cette manière, il suffit de faire une boucle qui affiche chaque liste à l'intérieur d'un tableau différent. Ces tableaux sont fabriqués par le composant *q-table*.

```HTML
<q-table
  grid
  title="Termes"
  :rows="rows"
  row-key="name"
  :filter="filter"
>
  <template v-slot:top-right>
    <q-input borderless dense debounce="300" v-model="filter" placeholder="Chercher">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
  </template>

  <template v-slot:item="props">
    <div class="card align-center">
      <q-card>
        <q-card-section class="text-center">
          <strong>{{ props.row.titleName }}</strong>
        </q-card-section>
        <q-separator />
        <q-card-section class="flex flex-left" :style="{ fontSize: props.row.articleName + 'px' }">
          <div>Signification : {{ props.row.articleName }} </div>
        </q-card-section>
      </q-card>
    </div>
  </template>
</q-table>
```
[^lexiqueSource2]

Chaque section/*q-card-section* contient soit un titre, soit une explication. Dans la zone de texte, lorsque l'utilisateur écrit un mot-clé, les résultats contiennent soit le mot-clé dans le titre, soit dans l'explication.

```{figure} ../source/figures/lexiqueResult.png
figure n°24
```

Dans ce cas ci-dessus, il s'agit de "chiffre". Si "chiffre" est mis en évidence dans les résultats, voici à quoi cela ressemble :

```{figure} ../source/figures/lexiqueHighlight.png
figure n°25
```

### Bibliothèque ("library")

Pour la bibliothèque, la recherche doit être faite avec des mots-clés qui ne contiennent que des caractères en minuscules.

```{figure} ../source/figures/libraryResult.png
figure n°26
```

Avec le mot-clé "chiffre", voici le résultat :

```{figure} ../source/figures/libraryResultExemple.png
figure n°27
```

Lorsque le bouton "RECHERCHER" est enclenché, il fait apparaitre le résultat.

La fonction "highLight()" vérifie que le mot-clé "SearchWord" figure dans l'un des élément de la constante "Titles". Si c'est vrai, la fonction renvoie tous les éléments qui contiennent le mot-clé, sinon, la fonction renvoie "aucun résultat".

```JavaScript
let SearchWord = reactive({
  text: ref('')
})

const Titles = [
    "five hundred years ago, the monkey king caused havoc in heaven",
    "I love you colonel Sanders",
    "le chiffrement"
]

function researchSmth(title, searchWord) {
    if (highLight(title, searchWord) !== "aucun résultat") {
        return "Résultat pour "
    }
}

function highLight(title, searchWord){

    let research = ""

    if (visible.find = true) {

        research += ""
        
        if (searchWord.length > 0) {
            for (let i = 0; i < title.length; i++) {

                if (title[i].toLowerCase().includes(searchWord)) {
                    
                research += title[i] + " // "
                }
            }
        }
        

        if (searchWord.length === 0) {
            research += "aucun résultat"
        }   
    }

    return research
}
```
[^librarySource]

Pour ce qui est de la fonction "researchSmth()", si "highLight()" renvoie un autre élément "qu'aucun résultat", alors il est écrit 'Résultat pour ', puis le mot-clé, puis les éléments correspondant.

[^librarySource]: DEVELOP PAPER, "utilisation de v-html pour mettre en évidence des mots-clés", 2021, consulté le 12 mars 2022, <[https://developpaper.com/vue-uses-v-html-to-highlight-keywords-words-in-a-string/](https://developpaper.com/vue-uses-v-html-to-highlight-keywords-words-in-a-string/)>

[^quasarSource]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource2]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource3]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource4]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource5]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource6]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^quasarSource7]: QUASAR, "documentation de composants quasar", 2022, consulté le 26 mars 2022, <[https://quasar.dev/](https://quasar.dev/)>

[^inputSource]: QUASAR, "documentation quasar pour faire une zone de texte avec placeholder", 2022, consulté le 2 mars 2022, <[https://quasar.dev/vue-components/input#standard](https://quasar.dev/vue-components/input#standard)>

[^lexiqueSource]: QUASAR, "documentation quasar pour faire le lexique", 2022, consulté le 2 mars 2022, <[https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns](https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns)>

[^lexiqueSource2]: QUASAR, "documentation quasar pour faire le lexique", 2022, consulté le 2 mars 2022, <[https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns](https://quasar.dev/layout/grid/flexbox-patterns#masonry-with-pseudo-selectors-to-break-rows-columns)>

[^quizSource]: SIMPLE STEPS CODE, "comment faire de manière simple un quiz en javascript", 2022, consulté le 26 février 2022, <[https://simplestepscode.com/javascript-quiz-tutorial/](https://simplestepscode.com/javascript-quiz-tutorial/)>

[^quizSource2]: SIMPLE STEPS CODE, "comment faire de manière simple un quiz en javascript", 2022, consulté le 26 février 2022, <[https://simplestepscode.com/javascript-quiz-tutorial/](https://simplestepscode.com/javascript-quiz-tutorial/)>

[^vueSource]: VUE.JS, "documentation de directives vuejs", 2022, consulté le 27 mars 2022, <[https://vuejs.org/](https://vuejs.org/)>

[^vueSource2]: VUE.JS, "documentation de directives vuejs", 2022, consulté le 27 mars 2022, <[https://vuejs.org/](https://vuejs.org/)>