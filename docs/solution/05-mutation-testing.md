# Mutation testing

## Code Coverage
Lancer une analyse du `code coverage` et discuter des résultats obtenus.

> Seriez-vous confiants pour remanier ce code avec la couverture actuelle ?

## Mutation Testing
Prendre un peu de temps pour découvrir le concept de [Mutation Testing](https://xtrem-tdd.netlify.app/Flavours/mutation-testing)
- Qu'avez-vous appris ?

- Le mutation testing est un type de test qui introduit différentes mutations à l'intérieur du code. Par mutation, on entend changer des actions (telles qu'une addition ou soustraction) en une autre afin de voir si le programme détecte cette erreur ou non.
- Cela permet d'évaluer l'efficacité des tests réalisés ainsi que découvrir d'éventuelles failles dans le programme qui n'auraient pas été vues avant.
- Les tests de mutations sont légèrement plus longs que des tests classiques
- Les tests de mutations peuvent ne rien tester si l'on n'utilise pas d'assertions ; il faut faire attention 

- Mettez en place les outils nécessaires à une `analyse de mutants`
  - java => [pitest](https://pitest.org/)
  - csharp => [stryker.NET](https://stryker-mutator.io/docs/stryker-net/introduction/)
  - php => [infection](https://infection.github.io/guide/)
  - typescript => [stryker-js](https://stryker-mutator.io/docs/stryker-js/introduction/)
  - python => [mutmut](https://mutmut.readthedocs.io/en/latest/)

- Analyser les résultats obtenus
- Quelques problèmes dans les tests réalisés avant. Modifications à apporter.

## La chasse aux mutants

En mob programming, appliquer les corrections nécessaires
