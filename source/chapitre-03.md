# 3. Cryptographie

```{Admonition} Important
Il existe deux grands types de chiffrement, le chiffrement de substitution monoalphabétique ou polyalphabétique. Pour le premier on y retrouve, le chiffrement César, le carré de Polybe, ainsi que d'autres qui n'ont pas été abordés.
En ce qui concerne le second, il concerne Enigma, le chiffrement de Vigenère, etc.
```

```{Note}
Dans ce chapitre, seulement trois chiffrements seront abordés. Chaque algorithme apportera une reflexion nouvelle sur le sujet.
```

## Définition

Il s'agit de "l'art du chiffrement" ou de "la science de chiffrement". C'est une des grandes catégories de la cryptologie. Son étymologie vient "d'écriture secrète".

## Chiffrement César

### Définition

Le cryptosystème César est un chiffrement de substitution monoalphabétique. Cela signifie qu'il utilise deux alphabets, un pour le texte clair qui correspond au notre et un second, qui change l'ordre des lettres. La clé de chiffrement sera un décalage de la position entre la lettre en clair et celle chiffrée. Il faut s'imaginer que chaque a une position initiale, par exemple, dans le texte clair, la lettre "a" est à la position une, alors que la lettre "k" du texte chiffré, qui se réfère à la lettre "a", est également au premier emplacement de son alphabet.

```{figure} figures/decalage-cesar.png
---
width: 30%
align: center
---
```

```{Tip}
Si la clé est égale à 2, alors il faudra remplacer la lettre "a", par la lettre "c". Pour l'illustration, le décalage est de 4.
```

```{figure} figures/roue-cesar.png
---
width: 30%
align: center
---
```

Il est assez courant d'utiliser la roue de César pour choisir avec aisance le décalage voulu. Il suffit de tourner la roue extérieur qui symbolise l'alphabet clair, afin de changer la clé. A contrario, la roue intérieur fait référence à l'alphabet chiffré.

```{Note}
Dans ce cas-là, la lettre se rapportant à "a" est la lettre "t".
```

### Inconvénient

Le problème du chiffrement César est qu'il est limité à 25 clé différentes, ce qui fait de cet algorithme, un chiffrement insécurisé. Il existe d'autres méthodes plus performantes pour pallier ce désavantage.

```{Warning}
Pour le moment, tout le texte subit le même décalage. Mais il est possible de le faire varier en se servant de la substitution polyalphabétique.
```

## Chiffrement de Substitution monoalphabétique

Comme cité précédemment, il existe plusieurs algorithmes ressemblant dans la démarche, à celui de César. Pour la substitution monoalphabétique, il suffit de garder deux alphabets statiques. La lettre clair vaudra toujours le même symbole ou la même lettre chiffrée.

```{Tip}
Prenons pour exemple la lettre "a", elle se référera toujours au symbole "@", ou à la lettre "w", s'il s'agit d'un chiffrement de substitution monoalphabétique.
```

```{Warning}
Le problème reste identique à celui de César. Le procédé est trop limité, ce qui rend facile la cryptanalyse de celui-ci.
```

## Chiffrement de Vigenère

```{Note}
Cette fois-ci, le raisonnement du chiffrement César va être repris, pour y apporter plus de spécificités et renforcer la sécurité des nouveaux algorithmes.
```

Ce cryptosystème reprend l'idée des positions des lettres qu'exploitait déjà César, mais cette fois-ci, la clé de chiffrement sera composée de n'importe quel mot de l'alphabet romain, qui sera répété en chaine, jusqu'au dernier caractère du texte clair. La position de la lettre dans la clé, sera additionnée à celle de la lettre claire, pour former la lettre chiffrée.

```{Tip}
Pour le texte "voici la porte ou se trouve la cle", il est possible d'utiliser la clé "key" :

Texte en clair : **voici la porte ou se trouve la cle**

Clé : **keyke yk eykey ke yk eykeyk ey key**

Texte chiffré : **fsgmm jk tmbxc yy qo xpyyto py mpc**
```