# 2. Histoire de la cryptologie

```{Note}
Les premiers codes secrets datent de l'Antiquité et ils sont originaires de Mésopotamie, d'Egypte, de Palestine, d'Inde, de Chine et de Grèce.
```

```{figure} figures/schema-cryptologie.png
---
width: 60%
align: center
---
```

## Carré de Polybe

```{figure} figures/carre-de-polybe.png
---
width: 30%
align: center
---
```

En Grèce antique, les indigènes utilisaient plusieurs alphabets, qui variaient entre 21 et 28 caractères. Pour le carré de Polybe, ils codaient des textes avec des combinaisons de suites de chiffres. Il suffit de faire un tableau, dans lequel, chaque lettre est alignée de gauche à droite, pour former un carré de 5 lettres, sur 5 lettres. Pour le numérotation, il faut d'abord prendre le chiffre appartenant à la colonne de gauche, puis prendre le chiffre de la ligne du haut. (cf. image)

```{Tip}
Par exemple, la lettre "a" correspond à "11". Le mot "salut", correspond donc à : "43 11 31 45 44"
```

```{Warning}
Le seul problème, pour l'alphabet romain est qu'il possède 26 lettres. Pour y remédier. Le "i" et le "j", vallent la même suite de chiffres(24). Cette procédure ne dérange en aucun cas, car il est facile de distinguer un mot, pour lequel il faut choisir si la lettre manquante est un "i" ou un "j". De cette manière, le carré de Polybe fonctionne avec l'alphabet romain.
```

## Chiffre des Franc-maçons

```{figure} figures/chiffre-franc-macon.png
---
width: 30%
align: center
---
```

Les Franc-maçons ont utilisé leur propre algorithme, depuis le Moyen-Age, jusqu'à aujourd'hui et il est resté secret pendant de nombreux sièclse.

Par rapport au carré de Polybe, les Franc-maçons n'ont pas pris des chiffres pour leur alphabet chiffré, mais ils se sont servis de symboles, à la place. Sur l'image ci-dessus, chaque lettre se trouve dans une sorte de tableau. Le symbole appartenant à la lettre, correspond à la zone autour de la lettre.

```{Tip}
Par exemple, le texte chiffré sous les quatres tableau, signifie "wikipedia".
```

Il semble difficile de comprendre comment leur langage secret a pu survivre aussi longtemps. Leur principe était simple, ils n'avaient le droit d'écrire leur alphabet, uniquement avec de la farine ou du sel, pour que personne puisse mettre la main sur la clé de chiffrement.

## Cryptosystème de Sckytale

```{figure} figures/scytale-baton.png
---
width: 50%
align: center
---
```

Cette nouvelle démarche vient de Sparte. Les Spartiates prennaient un bâton en bois et une lanière en papyrus, en parchemin ou en cuir, sur laquelle ils enroulaient la lanière autour du bâton et ils écrivaient le mot ou la phrase qu'ils voulaient. Cela permettait de changer l'emplacement des lettres, une fois la lanière décrochée.

```{Note}
Pour se faire, le message tenait sur 5 colonnes et 10 lignes
```

La clé de chiffrement était le nombre de colonnes et de lignes. Au fil des années, ces deux paramètres ont variés et donc, il existe plus de possibilités, de nos jours.

## Chiffrement par masque

Cette fois-ci, la méthode est plus moderne. Le chiffrement se fait en convertissant le texte clair en binaire et ensuite, d'utiliser une clé en binaire, avec laquelle il faudra additioner les bits du texte, pour ressortir un cryptotexte, toujours en binaire, qui pourra de nouveau être converti en lettres.

## Cryptanalyse d'Enigma

