# Clean code VS Dirty code

## Qu'est-ce que du code sale ?

- Marécage où on se perd : on commence à un endroit, on se troue ensuite autre part sans raison
- Code spaghetti : tout est lié 
- Sans structure : pas de classe, voir même de fonction. Non pensé avec un UML
- Code dupliqué
- Patchwork 1000 fois reprisé
- (Au cas par cas) Code outdated : les pratiques changent, le développeur s'améliore

Pour nous : 

- Duplication de code
- Mélange de langues anglais/français/espagnol/...
- Failles de sécurité évidentes : SQL Injection, ...
- Code mort
- #TODO laissés, commentaires inutiles

## Qu'est-ce que du code propre ?

- Documenter de manière exhaustive et correcte, mise à jour
- Lisible : se lit comme une phrase. Les abstractions sont nettes, les chemins d'exécution evidents.
- Elégant : Simple/Direct
- Facile à modifier : Tests/Documentation/Peu de dépendances/Nommage correct
- Ecrit avec soin : Aucun problème évident ne saute aux yeux
- Sans surprise : Le code fait la fonction qui lui est attribué, il n'y a pas de surprises quant aux attributs / code / etc..

Pour nous :

- Du code avec des commentaires, typage et documentation
- Des variables nommées avec ce qu'elles font
- Projet structuré
- Découpage de méthodes trop longues
- Du code testé
- Du code optimisé, rapide, fonctionnel