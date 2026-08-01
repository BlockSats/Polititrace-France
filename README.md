# PolitiTrace France

> Observatoire citoyen open source des programmes, déclarations, votes, finances et traitements médiatiques de la vie politique française.

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](pyproject.toml)
[![Contributions bienvenues](https://img.shields.io/badge/contributions-bienvenues-brightgreen.svg)](CONTRIBUTING.md)

## Pourquoi ce projet ?

PolitiTrace France vise à rendre les affirmations politiques **traçables, comparables et auditables**. Le projet ne cherche pas à décider quel parti « a raison » et ne produit pas de note idéologique unique.

Chaque résultat important doit distinguer :

1. la donnée brute ;
2. le calcul reproductible ;
3. l'interprétation humaine ou assistée par IA ;
4. le niveau de confiance et les limites.

## Périmètre initial

Période principale : **1er janvier 2017 à aujourd'hui**.

Familles politiques suivies dans le MVP :

- Front national / Rassemblement national ;
- La France insoumise et ses groupes parlementaires successifs ;
- En Marche / LREM / Renaissance et le groupe Ensemble pour la République ;
- Parti socialiste et ses groupes parlementaires successifs.

Axes initiaux : programmes, scrutins parlementaires, amendements, finances, déclarations publiques et exposition médiatique.

## Principes non négociables

- **Sources avant synthèse** : aucune conclusion importante sans référence vérifiable.
- **Pas de score politique global** : les indicateurs restent séparés et documentés.
- **Neutralité méthodologique** : mêmes règles de collecte et de mesure pour chaque famille.
- **Reproductibilité** : les chiffres sont calculés par du code déterministe.
- **IA sous contrôle** : l'IA extrait et rapproche ; elle ne remplace pas la preuve.
- **Droit de réponse et correction** : toute erreur documentée doit pouvoir être corrigée publiquement.
- **Respect des licences** : le code est libre ; les données tierces restent soumises à leurs conditions propres.
- **Cœur sans verrou propriétaire** : le fonctionnement essentiel doit rester reproductible avec des composants ouverts.

## Démarrage rapide

```bash
git clone https://github.com/BlockSats/polititrace-france.git
cd polititrace-france
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
polititrace validate
pytest
```

Sous Windows PowerShell :

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
polititrace validate
pytest
```

## Premières commandes

```bash
polititrace list-families
polititrace list-sources
polititrace validate
```

## Comment contribuer

Il n'est pas nécessaire d'être développeur. Les contributions utiles comprennent :

- vérifier une source ou une date ;
- documenter un changement de nom ou d'alliance ;
- proposer un indicateur mesurable ;
- écrire un test ;
- améliorer l'accessibilité ou la documentation ;
- auditer un biais méthodologique.

Commencer par [`CONTRIBUTING.md`](CONTRIBUTING.md), puis consulter les tickets portant le label `good first issue`.

## Structure

```text
src/polititrace/       bibliothèque et CLI
tests/                 tests automatisés
docs/                  méthode, architecture et décisions
.github/                modèles d'issues, PR et CI
scripts/                utilitaires de développement
```

## Feuille de route

- **v0.1** — catalogue historique des familles et registre des sources ;
- **v0.2** — collecte et normalisation des scrutins de l'Assemblée nationale ;
- **v0.3** — programmes et engagements structurés ;
- **v0.4** — comptes CNCCFP et indicateurs financiers ;
- **v0.5** — corpus médiatique légalement collectable et métriques descriptives ;
- **v1.0** — observatoire public avec API, tableaux de bord et méthodologie stabilisée.

Voir [`ROADMAP.md`](ROADMAP.md) pour le détail et [`docs/FIRST_ISSUES.md`](docs/FIRST_ISSUES.md) pour les premières contributions.

## Licence

Le code et la documentation originale sont publiés sous licence **MIT**. Les jeux de données importés ou référencés conservent leur licence et leurs conditions d'utilisation d'origine. Voir [`OPEN_SOURCE_POLICY.md`](OPEN_SOURCE_POLICY.md) et [`DATA_POLICY.md`](DATA_POLICY.md).

## Avertissement

PolitiTrace France est un projet indépendant, non affilié à un parti politique, un média ou une institution publique. Ses analyses ne constituent ni une consigne de vote ni une vérité automatisée.
