# Feuille de route

## v0.1 — Fondation ouverte

- identité et principes ;
- licence, contribution, gouvernance et sécurité ;
- catalogue historique des quatre familles ;
- registre initial des sources ;
- validation et tests ;
- modèles d'issues et CI.

## v0.2a — Démonstrateur vertical minimal

- sélectionner un seul thème politique comparable ;
- structurer quelques engagements sourcés ;
- relier ces engagements à un petit nombre de scrutins officiels ;
- résoudre les entités et groupes uniquement au niveau nécessaire ;
- expliquer chaque rapprochement et ses limites ;
- publier une démonstration compréhensible sans infrastructure lourde.

Cette étape sert à prouver l’utilité du projet avant la généralisation. Voir l’[issue #14](https://github.com/BlockSats/Polititrace-France/issues/14) et l’[ADR sur la complexité progressive](docs/decisions/0004-progressive-complexity.md).

## v0.2 — Parlement

- premier collecteur centré sur la XVe législature ;
- députés, groupes, scrutins et positions individuelles ;
- résolution temporelle minimale des changements de groupe ;
- validation sur un échantillon avant import exhaustif ;
- statistiques descriptives documentées.

L’extension aux XVIe et XVIIe législatures intervient seulement après validation du premier adaptateur.

## v0.3 — Programmes

- archivage des documents et empreintes ;
- segmentation des engagements ;
- taxonomie thématique ;
- interface de validation humaine.

## v0.4 — Transparence des financements

- comptes d’ensemble et annexes publiés par la CNCCFP ;
- aide publique, dons, cotisations, contributions d’élus et autres ressources ;
- actifs, dettes, trésorerie et résultat annuel ;
- prêts bancaires et identité des prêteurs personnes morales lorsqu’elle est publique ;
- prêts de personnes physiques suivis uniquement sous forme légalement publiable ;
- flux entre partis et structures liées ;
- historique des remboursements, réserves, manquements et décisions officielles ;
- indicateurs de dépendance, concentration et capacité de remboursement ;
- signaux d’alerte soumis à validation humaine, sans accusation automatique ;
- provenance, réconciliation comptable et visualisations comparables.

Voir [`docs/FINANCING_TRANSPARENCY.md`](docs/FINANCING_TRANSPARENCY.md) et l’[issue #12](https://github.com/BlockSats/Polititrace-France/issues/12).

## v0.5 — Médias

- registre des médias et échantillonnage ;
- métadonnées, temps de parole et thèmes ;
- protocole d'évaluation de tonalité ;
- audits de biais et tests de sensibilité.

## v1.0 — Publication publique

- API stable ;
- tableau de bord ;
- exports documentés ;
- méthodologie versionnée ;
- gouvernance pluraliste ;
- processus public de correction.
