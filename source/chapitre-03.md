# 3. Cryptographie

```{Admonition} Important
Il existe deux grands types de chiffrement, le chiffrement de substitution monoalphabétique ou polyalphabétique. Pour le premier on y retrouve, le chiffrement César, le carré de Polybe, ainsi que d'autres qui n'ont pas été abordés.
En ce qui concerne le second, il concerne Enigma, le chiffrement de Vigenère, etc. [1+2]
```

```{Note}
Dans ce chapitre, seulement trois chiffrements seront abordés. Chaque algorithme apportera une réflexion nouvelle sur le sujet.
```

## Définition

Il s'agit de "l'art du chiffrement" ou de "la science de chiffrement". C'est une des grandes catégories de la cryptologie. Son étymologie vient "d'écriture secrète". [3]

## Chiffrement César

### Définition

Le cryptosystème César est un chiffrement de substitution monoalphabétique. Cela signifie qu'il utilise deux alphabets, un pour le texte clair qui correspond au notre et un second, qui change l'ordre des lettres. La clé de chiffrement sera un décalage de la position entre la lettre en clair et celle chiffrée. Il faut s'imaginer que chaque a une position initiale, par exemple, dans le texte clair, la lettre "a" est à la position une, alors que la lettre "k" du texte chiffré, qui se réfère à la lettre "a", est également au premier emplacement de son alphabet. [1+3+4]

```{Tip}
Si la clé est égale à 2, alors il faudra remplacer la lettre "a", par la lettre "c". Pour l'illustration, le décalage est de 4. [3]
```

Il est assez courant d'utiliser la roue de César pour choisir avec aisance le décalage voulu. Il suffit de tourner la roue extérieure qui symbolise l'alphabet clair, afin de changer la clé. A contrario, la roue intérieure fait référence à l'alphabet chiffré. [3]

### Inconvénient

Le problème du chiffrement César est qu'il est limité à 25 clés différentes, ce qui fait de cet algorithme, un chiffrement insécurisé. Il existe d'autres méthodes plus performantes pour pallier ce désavantage. [1+3+4]

```{Warning}
Pour le moment, tout le texte subit le même décalage. Mais il est possible de le faire varier en se servant de la substitution polyalphabétique. [1+2]
```

## Chiffrement de Substitution monoalphabétique

Comme cité précédemment, il existe plusieurs algorithmes ressemblant dans la démarche, à celui de César. Pour la substitution monoalphabétique, il suffit de garder deux alphabets statiques. La lettre claire vaudra toujours le même symbole ou la même lettre chiffrée. [2+3]

```{Tip}
Prenons pour exemple la lettre "a", elle se référera toujours au symbole "@", ou à la lettre "w", s'il s'agit d'un chiffrement de substitution monoalphabétique.
```

```{Warning}
Le problème reste identique à celui de César. Le procédé est trop limité, ce qui rend facile la cryptanalyse de celui-ci. [2+3]
```

## Chiffrement de Vigenère

```{Note}
Avec le chiffrement de Vigenère, le raisonnement du chiffrement César va être repris, pour y apporter plus de spécificités et renforcer la sécurité des nouveaux algorithmes. [3+4]
```

Ce cryptosystème reprend l'idée des positions des lettres qu'exploitait déjà César, mais cette fois-ci, la clé de chiffrement sera composée de n'importe quel mot de l'alphabet romain, qui sera répété en chaine, jusqu'au dernier caractère du texte clair, cette méthode est autrement appelée le chiffrement de substitution polyalphabétique. La position de la lettre dans la clé, sera additionnée à celle de la lettre claire, pour former la lettre chiffrée. [3+4]

```{Tip}
Pour le texte : "voici la porte ou se trouve la cle", il est possible d'utiliser la clé "key" :

Texte en clair : **voici la porte ou se trouve la cle**

Clé : **keyke yk eykey ke yk eykeyk ey key**

Texte chiffré : **fsgmm jk tmbxc yy qo xpyyto py mpc**
```

## Notes de bas de page

[1] : SWEIGART, Al. *Cracking Codes with Python An Introduction to Building and Breaking Ciphers*. Californie : Mountain View, Riley Hoffman, 2018, 418 p.

[2] : COMMENTCAMARCHE.NET, "Chiffrement par substitution", 2007. Consulté le 16 janvier 2022. <https://web.maths.unsw.edu.au/~lafaye/CCM/crypto/simple.htm>

[3] : HROMKOVIČ, Juraj. *Einfach Informatik 7-9 – Lehrwerksteile - Klett und Balmer Verlag*. Baar : Klett & Balmer, 82 p.

[4] : SINGH, Simon. *The Code Book How to Make It, Hack It, Crack It*. New York : Brodway, Delacorte Press, 2002, 273 p.