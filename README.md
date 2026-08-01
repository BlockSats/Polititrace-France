# PolitiTrace France

> **Prototype citoyen open source visant à relier les programmes, déclarations, votes, financements et traitements médiatiques des forces politiques françaises.**

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](pyproject.toml)
[![Contributions bienvenues](https://img.shields.io/badge/contributions-bienvenues-brightgreen.svg)](CONTRIBUTING.md)
[![Statut: expérimental](https://img.shields.io/badge/statut-expérimental-orange.svg)](ROADMAP.md)

## État réel du projet

**PolitiTrace France est actuellement en phase d’amorçage — version 0.1.**

Le dépôt contient les fondations méthodologiques et techniques nécessaires pour essayer de construire un observatoire ouvert, vérifiable et reproductible. Il ne faut pas encore le présenter comme un observatoire opérationnel.

### Ce qui fonctionne déjà

- licence open source MIT ;
- méthodologie initiale publique ;
- règles de gouvernance, de contribution et de correction ;
- politique de provenance et de réutilisation des données ;
- catalogue historique initial de quatre familles politiques ;
- registre des premières sources officielles ;
- interface en ligne de commande pour consulter et valider ces catalogues ;
- tests automatisés et intégration continue GitHub ;
- feuille de route et issues ouvertes aux contributions.

### Ce qui n’existe pas encore

- aucun collecteur complet des votes de l’Assemblée nationale ;
- aucune base consolidée de programmes électoraux ;
- aucun rapprochement automatisé entre promesses, déclarations et votes ;
- aucune analyse financière automatisée des partis ;
- aucun corpus médiatique constitué par le projet ;
- aucune mesure publiée du traitement médiatique ;
- aucun système autonome de fact-checking ;
- aucun tableau de bord public ;
- aucun classement ou résultat politique produit par PolitiTrace ;
- aucune intelligence artificielle d’analyse politique opérationnelle dans le dépôt.

Ces éléments sont des **objectifs de recherche et de développement**, pas des fonctionnalités disponibles.

## Ce qui existe déjà

De nombreux projets utiles couvrent déjà certaines briques :

| Projet ou source | Apport principal |
|---|---|
| [NosDéputés.fr](https://www.nosdeputes.fr/) | Activité parlementaire : interventions, amendements, questions, présence et travaux des députés |
| [Datan](https://datan.fr/) | Votes, positions des groupes, participation, cohésion et proximité parlementaire |
| [Manifesto Project](https://manifesto-project.wzb.eu/) | Corpus international de programmes électoraux codés et comparables |
| [CNCCFP](https://cnccfp.fr/partis-politiques/) | Comptes officiels et financement des partis politiques français |
| [Arcom](https://www.arcom.fr/temps-parole) | Données officielles sur le pluralisme audiovisuel et les temps de parole |
| [Media Cloud](https://www.mediacloud.org/) | Recherche et analyse de grands corpus de presse en ligne |
| [GDELT](https://www.gdeltproject.org/) | Suivi mondial et à grande échelle de l’actualité et des événements médiatisés |

PolitiTrace ne cherche pas à remplacer ces projets ni à reproduire inutilement leurs fonctions.

## Est-ce que PolitiTrace fait davantage que ce qui existe ?

### Aujourd’hui : non

Dans son état actuel, PolitiTrace fournit un cadre initial, du code de validation et une proposition de méthode commune.

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
Financements et endettement
        ↓
Visibilité et cadrage médiatiques
```

La valeur ajoutée potentielle serait de permettre :

- le suivi d’une même famille politique depuis 2017 malgré les changements de noms, groupes et coalitions ;
- la distinction entre parti juridique, groupe parlementaire, coalition, candidat et élu ;
- le rapprochement d’un engagement avec des actes parlementaires observables ;
- la comparaison du discours et des votes sans confondre pouvoir et opposition ;
- l’analyse conjointe des finances, de l’activité politique et de la médiatisation ;
- la traçabilité de chaque résultat jusqu’aux sources et au code de calcul ;
- la publication des incertitudes, contradictions et limites ;
- la reproduction, la contestation et l’amélioration des analyses par des tiers.

Cette valeur ajoutée reste à démontrer par un prototype fonctionnel.

## Module envisagé : transparence des financements politiques

PolitiTrace doit pouvoir expliquer **comment chaque parti se finance**, auprès de quels organismes et sous quelles formes :

- aide publique ;
- dons de personnes physiques ;
- cotisations des adhérents ;
- contributions des élus ;
- prêts bancaires ;
- prêts de personnes physiques ;
- transferts entre partis ou structures liées ;
- ventes, prestations, produits financiers ou exceptionnels ;
- dettes fournisseurs et autres dettes.

### Ce que les sources publiques peuvent permettre

À partir des comptes et annexes de la [CNCCFP](https://cnccfp.fr/partis-politiques/) et du [jeu de données ouvert sur data.gouv.fr](https://www.data.gouv.fr/datasets/comptes-des-partis-et-groupements-politiques), le futur module pourrait notamment présenter :

- la répartition annuelle des ressources ;
- la dépendance à l’aide publique, aux dons ou aux cotisations ;
- le niveau et la composition de l’endettement ;
- l’identité des banques et autres prêteurs personnes morales lorsqu’elle est officiellement publiée ;
- les montants, échéances, taux et remboursements lorsqu’ils figurent dans les documents publics ;
- les flux financiers entre partis ou structures affiliées ;
- les comptes non déposés, non certifiés, tardifs ou assortis de réserves ;
- les manquements, décisions administratives et décisions juridictionnelles publiées.

### Ce que PolitiTrace ne pourra pas affirmer seul

Les listes nominatives des donateurs, cotisants et prêteurs particuliers transmises à la CNCCFP ne sont pas des données ouvertes. PolitiTrace ne doit pas tenter de réidentifier ces personnes ni publier des informations personnelles non publiques.

Le projet pourra signaler une incohérence, une dépendance inhabituelle ou un prêt nécessitant une vérification. Il ne devra jamais transformer automatiquement ce signal en accusation de fraude, de corruption, de blanchiment ou de financement occulte.

La qualification employée devra distinguer :

1. information publique ;
2. anomalie technique ;
3. signal d’alerte ;
4. manquement constaté par une autorité ;
5. décision officielle ;
6. condamnation définitive.

Documentation complète : [`docs/FINANCING_TRANSPARENCY.md`](docs/FINANCING_TRANSPARENCY.md)  
Suivi du chantier : [issue #12](https://github.com/BlockSats/Polititrace-France/issues/12)

## Ce que le projet ne veut pas devenir

PolitiTrace ne doit pas être :

- une IA qui décide quel parti dit la vérité ;
- un outil de propagande en faveur ou contre une formation ;
- un classement général des « meilleurs » et « pires » partis ;
- un système qui attribue une intention aux médias à partir d’un simple écart statistique ;
- un détecteur automatique de financement illégal ;
- une boîte noire dont les sources ou calculs seraient inaccessibles ;
- un agrégateur qui copie des contenus protégés sans respecter leurs droits ;
- un substitut au travail des journalistes, chercheurs, juristes, autorités de contrôle ou juridictions.

## Questions auxquelles un futur prototype pourrait répondre

| Question | Éléments nécessaires |
|---|---|
| Un groupe vote-t-il conformément à ses engagements ? | Programmes, scrutins, amendements et chronologie |
| Une position politique a-t-elle changé ? | Documents datés, déclarations et votes successifs |
| Comment un parti finance-t-il son activité ? | Comptes CNCCFP, ressources, prêteurs publics et flux financiers |
| Un parti est-il financièrement fragile ? | Actifs, dettes, trésorerie, échéances et produits annuels |
| Quelle banque ou personne morale lui a prêté de l’argent ? | Annexes publiques et identité officielle des prêteurs personnes morales |
| Existe-t-il un signal financier inhabituel ? | Historique, ratios, documents primaires et validation humaine |
| Deux groupes opposés votent-ils parfois ensemble ? | Votes individuels et positions majoritaires |
| La visibilité médiatique correspond-elle au poids politique ? | Temps de parole, invitations, mentions et variables de contrôle |

Le système pourra mesurer des différences observables. Il ne pourra pas, à lui seul, démontrer une intention politique, éditoriale ou frauduleuse.

## Périmètre du premier prototype

**Période principale : 1er janvier 2017 à aujourd’hui.**

Quatre familles politiques sont retenues au départ :

- Front national / Rassemblement national ;
- La France insoumise et ses groupes parlementaires successifs ;
- En Marche / LREM / Renaissance et le groupe Ensemble pour la République ;
- Parti socialiste et ses groupes parlementaires successifs.

Ce périmètre est volontairement limité afin de vérifier la cohérence de la méthode avant son extension.

## Principes méthodologiques

- **Sources avant synthèse** : aucune conclusion importante sans référence vérifiable.
- **Pas de score politique global** : les indicateurs restent séparés et documentés.
- **Neutralité procédurale** : mêmes règles de collecte et de calcul pour chaque famille.
- **Contexte institutionnel** : pouvoir et opposition ne disposent pas des mêmes moyens d’action.
- **Reproductibilité** : les chiffres doivent être calculés par du code déterministe.
- **IA explicitement signalée** : une sortie de modèle n’est jamais une source primaire.
- **Présomption et statut juridique** : un signal n’est ni un manquement ni une condamnation.
- **Droit de correction** : les erreurs et modifications doivent rester visibles.
- **Respect des licences et de la vie privée** : le code libre ne rend pas automatiquement libres les données tierces ou personnelles.
- **Cœur sans verrou propriétaire** : le fonctionnement essentiel doit rester reproductible avec des composants ouverts.

## Un exemple à critiquer et améliorer

Le dépôt est publié avant que le produit soit terminé afin de rendre les choix visibles et de permettre à d’autres personnes de proposer mieux.

Le projet recherche notamment :

- développeurs Python et data ;
- spécialistes de données parlementaires ;
- journalistes et chercheurs en sciences politiques ;
- comptables, auditeurs et spécialistes des financements politiques ;
- statisticiens et spécialistes du traitement automatique du langage ;
- juristes sur les données, médias et financements politiques ;
- designers et spécialistes de l’accessibilité ;
- citoyens prêts à vérifier des sources et des chronologies ;
- contradicteurs capables d’identifier les biais de la méthode.

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

Ces commandes consultent et valident les catalogues initiaux. Elles ne lancent encore aucune analyse politique ou financière.

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
- **v0.4 — envisagée** : transparence des ressources, prêteurs, dettes et décisions financières ;
- **v0.5 — envisagée** : corpus médiatique légalement collectable et métriques descriptives ;
- **v1.0 — objectif** : observatoire public avec API, tableaux de bord et méthodologie stabilisée.

Voir [`ROADMAP.md`](ROADMAP.md), l’[issue de suivi v0.2](https://github.com/BlockSats/Polititrace-France/issues/9) et l’[issue finances #12](https://github.com/BlockSats/Polititrace-France/issues/12).

## Contribution et licence

Consulter [`CONTRIBUTING.md`](CONTRIBUTING.md), [`METHODOLOGY.md`](METHODOLOGY.md), [`OPEN_SOURCE_POLICY.md`](OPEN_SOURCE_POLICY.md) et [`DATA_POLICY.md`](DATA_POLICY.md).

Le code et la documentation originale sont publiés sous licence **MIT**. Les données importées ou référencées conservent leurs licences et conditions d’utilisation d’origine.

## Avertissement

PolitiTrace France est un projet indépendant et expérimental, non affilié à un parti politique, un média ou une institution publique. Il ne produit actuellement aucune recommandation électorale, aucun classement politique et aucune conclusion automatisée sur les formations étudiées.
