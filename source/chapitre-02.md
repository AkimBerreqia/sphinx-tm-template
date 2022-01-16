# 2. Cryptologie

## Définition

Il s'agit de la science globale de chiffrement et de déchiffrement d'informations, avec la cryptographie et la cryptanalyse, comme embranchements.

## Histoire

```{Note}
Les premiers codes secrets datent de l'Antiquité et ils sont originaires de Mésopotamie, d'Egypte, de Palestine, d'Inde, de Chine et de Grèce.
```

### Carré de Polybe

En Grèce antique, les indigènes utilisaient plusieurs alphabets, qui variaient entre 21 et 28 caractères. Pour le carré de Polybe, ils codaient des textes avec des combinaisons de suites de chiffres. Il suffit de faire un tableau, dans lequel, chaque lettre est alignée de gauche à droite, pour former un carré de 5 lettres, sur 5 lettres. Pour la numérotation, il faut d'abord prendre le chiffre appartenant à la colonne de gauche, puis prendre le chiffre de la ligne du haut. (cf. image)

```{Tip}
Par exemple, la lettre "a" correspond à "11". Le mot "salut", correspond donc à : "43 11 31 45 44"
```

```{Warning}
Le seul problème, pour l'alphabet romain est qu'il possède 26 lettres. Pour y remédier. Le "i" et le "j", valent la même suite de chiffres(24). Cette procédure ne dérange en aucun cas, car il est facile de distinguer un mot, pour lequel il faut choisir si la lettre manquante est un "i" ou un "j". De cette manière, le carré de Polybe fonctionne avec l'alphabet romain.
```

### Chiffre des Francs-maçons

```{Tip}
Le texte chiffré sous les quatre tableaux, signifie "wikipedia".
```

Les Francs-maçons ont utilisé leur propre algorithme, depuis le Moyen-Age, jusqu'à aujourd'hui et il est resté secret pendant de nombreux siècles.

Par rapport au carré de Polybe, les Francs-maçons n'ont pas pris des chiffres pour leur alphabet chiffré, mais ils se sont servis de symboles, à la place. Sur l'image ci-dessus, chaque lettre se trouve dans une sorte de tableau. Le symbole appartenant à la lettre, correspond à la zone autour de la lettre.

Il semble difficile de comprendre comment leur langage secret a pu survivre aussi longtemps. Leur principe était simple, ils n'avaient le droit d'écrire leur alphabet, uniquement avec de la farine ou du sel, pour que personne ne puisse mettre la main sur la clé de chiffrement.

### Cryptosystème de Scytale

Cette nouvelle démarche vient de Sparte. Les Spartiates prenaient un bâton en bois et une lanière en papyrus, en parchemin ou en cuir, sur laquelle ils enroulaient la lanière autour du bâton et ils écrivaient le mot ou la phrase qu'ils voulaient. Cela permettait de changer l'emplacement des lettres, une fois la lanière décrochée.

```{Note}
Pour se faire, le message tenait sur 5 colonnes et 10 lignes
```

La clé de chiffrement était le nombre de colonnes et de lignes. Au fil des années, ces deux paramètres ont variés et donc, il existe plus de possibilités, de nos jours.

### Chiffrement par masque

Cette fois-ci, la méthode est plus moderne. Le chiffrement se fait en convertissant le texte clair en binaire et ensuite, d'utiliser une clé en binaire, avec laquelle il faudra additionner les bits du texte, pour ressortir un cryptotexte, toujours en binaire, qui pourra de nouveau être converti en lettres.

### Cryptanalyse d'Enigma

Lors de la deuxième Guerre Mondiale, les allemands chiffraient leurs messages avec un algorithme inconnu du point de vu des Alliés. Mais ces derniers ont repérés des répétitions dans les messages et après de nombreuses recherches, ils ont réussi à trouver la clé de chiffrement. A partir de ce moment, la cryptanalyse d'Enigma a permis aux Alliés de gagner la guerre, car ils gardaient une longueur d'avance, face à l'Axe.