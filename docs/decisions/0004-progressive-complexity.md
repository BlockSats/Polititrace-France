# ADR 0004 — Complexité progressive

- Statut : accepté
- Date : 2026-08-01

## Contexte

PolitiTrace doit conserver une méthode rigoureuse sans devenir une infrastructure difficile à comprendre, à installer ou à contribuer. Plusieurs choix potentiellement utiles — base de données graphe, moteur d’événements générique, multiples adaptateurs, modèles d’IA et schémas très abstraits — pourraient être introduits trop tôt.

## Décision

Le projet adopte une règle de **complexité progressive** : une nouvelle dépendance, abstraction ou infrastructure n’est ajoutée que lorsqu’un besoin concret du démonstrateur vertical la justifie.

Le premier démonstrateur doit pouvoir fonctionner avec :

- des modèles Python simples et validés ;
- des fichiers JSON ou un stockage local léger ;
- un adaptateur limité à la XVe législature ;
- un petit nombre de documents, engagements et scrutins ;
- une validation humaine explicite ;
- aucune IA obligatoire.

## Choix différés

Les éléments suivants ne sont pas interdits, mais reportés jusqu’à justification mesurable :

- base de données orientée graphe ;
- moteur générique d’événements ;
- import exhaustif de toutes les législatures ;
- orchestration distribuée ;
- infrastructure de modèles d’IA ;
- microservices ;
- interface web complète.

## Critères d’introduction d’une complexité nouvelle

Une proposition doit expliquer :

1. le problème concret rencontré ;
2. pourquoi la solution actuelle ne suffit plus ;
3. l’alternative la plus simple examinée ;
4. le coût d’installation, de maintenance et de contribution ;
5. la manière de revenir en arrière.

## Conséquences

- le README reste centré sur l’utilité et l’état réel du projet ;
- les détails techniques sont placés dans les issues et documents dédiés ;
- les nouveaux contributeurs peuvent travailler sur des tâches isolées ;
- certaines migrations futures resteront possibles, mais elles seront fondées sur des données d’usage réelles.
