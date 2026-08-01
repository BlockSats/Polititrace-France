# Contribuer à PolitiTrace France

Merci de contribuer à un projet où la qualité méthodologique compte autant que le code.

## Contributions possibles

- **Données** : ajouter ou corriger une source officielle.
- **Recherche** : documenter une méthode de comparaison.
- **Développement** : collecteurs, normalisation, API, tests, interface.
- **Journalisme / droit** : vérifier le contexte, les formulations et les limites.
- **Design / accessibilité** : rendre les résultats compréhensibles et utilisables.
- **Audit contradictoire** : rechercher activement les biais ou erreurs du projet.

## Avant d'ouvrir une pull request

1. Ouvrir ou commenter une issue pour les changements importants.
2. Expliquer la question traitée et la méthode choisie.
3. Ajouter les sources et leurs conditions de réutilisation.
4. Ajouter ou adapter les tests.
5. Exécuter `pytest` et `polititrace validate`.
6. Décrire les limites et les cas non couverts.

## Règles concernant les affirmations politiques

Une contribution ne doit pas présenter une interprétation comme un fait. Utiliser les catégories suivantes :

- `source_officielle` ;
- `document_parti` ;
- `source_secondaire` ;
- `calcul` ;
- `inference` ;
- `sortie_ia`.

Toute `inference` ou `sortie_ia` doit référencer les éléments sur lesquels elle repose.

## Neutralité procédurale

Une méthode proposée doit pouvoir être appliquée sans modification aux quatre familles étudiées. Toute exception doit être justifiée par une différence institutionnelle explicite, par exemple parti au pouvoir contre parti d'opposition.

## Pull requests

- PR courtes et ciblées ;
- titre explicite ;
- aucune donnée personnelle inutile ;
- aucune reproduction intégrale d'articles protégés ;
- commits compréhensibles ;
- désaccords méthodologiques consignés dans une ADR si nécessaire.

## Convention de branches

- `feat/...` nouvelle fonctionnalité ;
- `fix/...` correction ;
- `data/...` source ou schéma de données ;
- `docs/...` documentation ;
- `method/...` méthodologie.

## Environnement

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pre-commit install
pytest
```

## Reconnaissance

Les contributions sont conservées dans l'historique Git. Les contributions substantielles peuvent être ajoutées à `CITATION.cff` avec l'accord de leur auteur.
