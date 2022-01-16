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

Le cryptosystème César est un chiffrement de substitution monoalphabétique. Cela signifie qu'il utilise deux alphabets, un pour le texte clair qui correspond au notre et un second, qui change l'ordre des lettres. La clé de chiffrement sera un décalage de la position entre la lettre en clair et celle chiffrée.

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

Cette fois-ci, le raisonnement du chiffrement va être repris, pour y apporter plus de sécurité.