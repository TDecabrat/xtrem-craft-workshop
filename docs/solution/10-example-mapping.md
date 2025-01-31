# Example Mapping

## Format de restitution
*(rappel, pour chaque US)*

```markdown
## Titre de l'US (post-it jaunes)

- Convert a money
- Define Pivot Currency
- Add an exchange rate

> Question (post-it rouge)

Peut-on transformer l'argent en différentes devises après évaluation ?

### Règle Métier (post-it bleu)

Exemple: (post-it vert)

- 0 USD -> 0 KRW -> 0 €
- 10 USD -> ... KRW -> 9.~ €
- Le portefeuille contient 5 USD et 10 € -> 17 USD

- [ ] 5 USD + 10 EUR = 17 USD
```

Vous pouvez également joindre une photo du résultat obtenu en utilisant les post-its.

## Story 1: Define Pivot Currency

```gherkin
As a Foreign Exchange Expert
I want to be able to define a Pivot Currency
So that I can express exchange rates based on it
```

## Story 2: Add an exchange rate
```gherkin
As a Foreign Exchange Expert
I want to add/update exchange rates by specifying: a multiplier rate and a currency
So they can be used to evaluate client portfolios
```

## Story 3: Convert a Money

```gherkin
As a Bank Consumer
I want to convert a given amount in currency into another currency
So it can be used to evaluate client portfolios
```




