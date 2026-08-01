# Architecture cible

```text
Sources officielles / partis / médias
                ↓
        Collecteurs versionnés
                ↓
      Zone brute + métadonnées
                ↓
 Normalisation et résolution d'entités
                ↓
 PostgreSQL / fichiers Parquet / index texte
                ↓
 Indicateurs déterministes + analyses IA tracées
                ↓
          API FastAPI
                ↓
 Tableau de bord et exports reproductibles
```

## Phase actuelle

Le dépôt démarre par un catalogue versionné des familles politiques et des sources. Cette couche évite d'attribuer rétrospectivement un acte à une entité qui portait alors un autre nom ou appartenait à une autre coalition.

## Choix techniques progressifs

- Python 3.12+ ;
- formats JSON simples pour le catalogue initial ;
- tests `pytest` ;
- validation automatisée en CI ;
- PostgreSQL et stockage colonne ajoutés lorsque le volume le justifie ;
- API et interface seulement après stabilisation des modèles de données.
