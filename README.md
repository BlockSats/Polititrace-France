# PolitiTrace France

> **Prototype citoyen open source visant à relier les programmes, déclarations, votes, finances et traitements médiatiques des forces politiques françaises.**

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](pyproject.toml)
[![Contributions bienvenues](https://img.shields.io/badge/contributions-bienvenues-brightgreen.svg)](CONTRIBUTING.md)
[![Statut: expérimental](https://img.shields.io/badge/statut-expérimental-orange.svg)](ROADMAP.md)

## État réel du projet

**PolitiTrace France est actuellement un projet en phase d’amorçage — version 0.1.**

Il ne faut pas le présenter comme un observatoire déjà opérationnel. Le dépôt contient aujourd’hui les fondations nécessaires pour essayer d’en construire un de manière ouverte, vérifiable et reproductible.

### Ce qui fonctionne déjà

- une licence open source MIT ;
- une méthodologie initiale publique ;
- des règles de gouvernance, de contribution et de correction ;
- une politique de provenance et de réutilisation des données ;
- un catalogue historique initial de quatre familles politiques ;
- un registre des premières sources officielles ;
- une petite interface en ligne de commande pour consulter et valider ces catalogues ;
- des tests automatisés et une intégration continue GitHub ;
- une feuille de route et des issues ouvertes aux contributions.

### Ce qui n’existe pas encore

- aucun collecteur complet des votes de l’Assemblée nationale ;
- aucune base consolidée de programmes électoraux ;
- aucun rapprochement automatisé entre promesses, déclarations et votes ;
- aucune analyse financière automatisée des partis ;
- aucun corpus médiatique constitué par le projet ;
- aucune mesure publiée du traitement médiatique ;
- aucun système de fact-checking autonome ;
- aucun tableau de bord public ;
- aucun classement ou résultat politique produit par PolitiTrace ;
- aucune intelligence artificielle d’analyse politique opérationnelle dans le dépôt.

Les éléments ci-dessus sont des **objectifs de recherche et de développement**, pas des fonctionnalités disponibles.

## Pourquoi lancer ce projet ?

De nombreux outils utiles existent déjà, mais ils répondent généralement à une partie du problème :

| Projet ou source | Ce qu’il apporte principalement |
|---|---|
| [NosDéputés.fr](https://www.nosdeputes.fr/) | Activité parlementaire : interventions, amendements, questions, présence et travaux des députés |
| [Datan](https://datan.fr/) | Votes, positions des groupes, participation, loyauté et proximité parlementaire |
| [Manifesto Project](https://manifesto-project.wzb.eu/) | Corpus international de programmes électoraux codés et comparables |
| [CNCCFP](https://cnccfp.fr/partis-politiques/) | Comptes officiels et financement des partis politiques français |
| [Arcom](https://www.arcom.fr/temps-parole) | Données officielles sur le pluralisme audiovisuel et les temps de parole |
| [Media Cloud](https://www.mediacloud.org/) | Recherche et analyse de grands corpus de presse en ligne |
| [GDELT](https://www.gdeltproject.org/) | Suivi mondial et à grande échelle de l’actualité et des événements médiatisés |

PolitiTrace ne cherche pas à remplacer ces projets ni à reproduire inutilement leurs fonctions.

## Est-ce que PolitiTrace fait davantage que ce qui existe ?

### Aujourd’hui : non

Dans son état actuel, PolitiTrace ne fait pas davantage que ces outils. Il fournit seulement un cadre initial, du code de validation et une proposition de méthode commune.

### Ce qu’il pourrait apporter si le projet aboutit

L’apport envisagé serait de **relier dans une même chronologie plusieurs types de données aujourd’hui dispersés** :

```text
Programme électoral
        ↓
Déclarations publiques
        ↓
Votes, amendements et décisions
        ↓
Évolution des positions
        ↓
Finances du parti
        ↓
Visibilité et cadrage médiatiques
```

La valeur ajoutée potentielle serait donc moins de créer une nouvelle source de données que de construire une couche de rapprochement permettant :

- de suivre une même famille politique depuis 2017 malgré les changements de noms, groupes et coalitions ;
- de distinguer parti juridique, groupe parlementaire, coalition, candidat et élu ;
- de relier un engagement à des actes parlementaires réellement observables ;
- de comparer le discours avec les votes sans confondre pouvoir et opposition ;
- de mettre les finances, l’activité politique et la médiatisation dans un même contexte ;
- de rendre chaque résultat traçable jusqu’à ses sources et à son code de calcul ;
- de publier aussi les incertitudes, contradictions et limites ;
- de permettre à d’autres de reproduire, contester ou améliorer les analyses.

Cette valeur ajoutée reste à démontrer par un prototype fonctionnel.

## Ce que le projet ne veut pas devenir

PolitiTrace ne doit pas être :

- une IA qui décide quel parti dit la vérité ;
- un outil de propagande en faveur ou contre une formation ;
- un classement général des « meilleurs » et « pires » partis ;
- un système qui attribue une intention aux médias à partir d’un simple écart statistique ;
- une boîte noire dont les sources ou calculs seraient inaccessibles ;
- un agrégateur qui copie des articles protégés sans respecter leurs droits ;
- un substitut au travail des journalistes, chercheurs, juristes ou organismes de contrôle.

## Questions auxquelles un futur prototype pourrait répondre

| Question | Éléments nécessaires |
|---|---|
| Un groupe vote-t-il conformément à ses engagements ? | Programmes, scrutins, amendements et chronologie |
| Une position politique a-t-elle changé ? | Documents datés, déclarations et votes successifs |
| Un parti est-il financièrement fragile ? | Comptes CNCCFP, actifs, dettes, trésorerie et résultat |
| Deux groupes opposés votent-ils parfois ensemble ? | Votes individuels et positions majoritaires |
| La visibilité médiatique correspond-elle au poids politique ? | Temps de parole, invitations, mentions et variables de contrôle |
| Un parti est-il davantage traité sous l’angle du fond ou de la polémique ? | Corpus défini, classification documentée et contrôle humain |

Le système pourrait mesurer des différences observables. Il ne pourrait pas, à lui seul, démontrer une intention politique ou éditoriale.

## Périmètre du premier prototype

**Période principale : 1er janvier 2017 à aujourd’hui.**

Quatre familles politiques sont retenues au départ :

- Front national / Rassemblement national ;
- La France insoumise et ses groupes parlementaires successifs ;
- En Marche / LREM / Renaissance et le groupe Ensemble pour la République ;
- Parti socialiste et ses groupes parlementaires successifs.

Ce périmètre est volontairement limité. L’objectif est d’abord de vérifier qu’une méthode peut être appliquée de manière cohérente avant de l’étendre à d’autres formations.

## Principes méthodologiques

- **Sources avant synthèse** : aucune conclusion importante sans référence vérifiable.
- **Pas de score politique global** : les indicateurs restent séparés et documentés.
- **Neutralité procédurale** : mêmes règles de collecte et de calcul pour chaque famille.
- **Contexte institutionnel** : un parti au pouvoir et un parti d’opposition ne sont pas évalués comme s’ils disposaient des mêmes moyens d’action.
- **Reproductibilité** : les chiffres doivent être calculés par du code déterministe.
- **IA explicitement signalée** : une sortie de modèle n’est jamais une source primaire.
- **Droit de correction** : les erreurs et modifications doivent rester visibles.
- **Respect des licences** : le code libre ne rend pas automatiquement libres les données tierces.
- **Cœur sans verrou propriétaire** : le fonctionnement essentiel doit rester reproductible avec des composants ouverts.

## Un exemple à critiquer et améliorer

Le dépôt est publié maintenant, avant que le produit soit terminé, pour rendre les choix initiaux visibles et permettre à d’autres personnes de proposer mieux.

Les critiques argumentées sont aussi utiles que le code. Le projet recherche notamment :

- des développeurs Python et data ;
- des spécialistes de données parlementaires ;
- des journalistes et chercheurs en sciences politiques ;
- des statisticiens et spécialistes du traitement automatique du langage ;
- des juristes sur les données, médias et financements politiques ;
- des designers et spécialistes de l’accessibilité ;
- des citoyens prêts à vérifier des sources et des chronologies ;
- des contradicteurs capables d’identifier les biais de la méthode.

➡️ [Proposer une meilleure méthode ou une autre architecture](https://github.com/BlockSats/Polititrace-France/issues/10)

➡️ [Voir les premières tâches accessibles](https://github.com/BlockSats/Polititrace-France/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## Démarrage rapide

```bash
git clone https://github.com/BlockSats/Polititrace-France.git
cd Polititrace-France
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

## Commandes actuelles

```bash
polititrace list-families
polititrace list-sources
polititrace validate
```

Ces commandes consultent et valident les catalogues initiaux. Elles ne lancent encore aucune analyse politique.

## Structure du dépôt

```text
src/polititrace/       bibliothèque et CLI
tests/                 tests automatisés
docs/                  méthode, architecture et décisions
.github/                modèles d’issues, PR et CI
scripts/                utilitaires de développement
```

## Feuille de route

- **v0.1 — disponible** : fondations, catalogues, documentation et validation ;
- **v0.2 — prochaine étape** : collecte et normalisation des scrutins de l’Assemblée nationale ;
- **v0.3 — envisagée** : programmes et engagements structurés ;
- **v0.4 — envisagée** : comptes CNCCFP et indicateurs financiers ;
- **v0.5 — envisagée** : corpus médiatique légalement collectable et métriques descriptives ;
- **v1.0 — objectif** : observatoire public avec API, tableaux de bord et méthodologie stabilisée.

Voir [`ROADMAP.md`](ROADMAP.md) et l’[issue de suivi v0.2](https://github.com/BlockSats/Polititrace-France/issues/9).

## Contribution et licence

Consulter [`CONTRIBUTING.md`](CONTRIBUTING.md), [`METHODOLOGY.md`](METHODOLOGY.md), [`OPEN_SOURCE_POLICY.md`](OPEN_SOURCE_POLICY.md) et [`DATA_POLICY.md`](DATA_POLICY.md).

Le code et la documentation originale sont publiés sous licence **MIT**. Les données importées ou référencées conservent leurs licences et conditions d’utilisation d’origine.

## Avertissement

PolitiTrace France est un projet indépendant et expérimental, non affilié à un parti politique, un média ou une institution publique. Il ne produit actuellement aucune recommandation électorale, aucun classement politique et aucune conclusion automatisée sur les formations étudiées.
