# Premières issues à ouvrir

Cette liste est destinée à amorcer le tableau de travail public dès la création du dépôt GitHub.

## Bonnes premières contributions

1. **Vérifier les dénominations historiques RN/FN**  
   Ajouter les sources primaires et confirmer les dates de changement de nom.

2. **Vérifier les groupes parlementaires de la XVe législature**  
   Confirmer les noms officiels et les périodes de changement.

3. **Documenter les licences des cinq sources initiales**  
   Compléter le champ `redistribution` dans `sources.json`.

4. **Ajouter un schéma JSON pour `families.json`**  
   Produire un schéma lisible et des messages d'erreur précis.

5. **Ajouter un schéma JSON pour `sources.json`**  
   Valider catégories, URL, niveau de preuve et conditions de réutilisation.

6. **Écrire un guide Windows complet**  
   Installation, environnement virtuel, tests et commandes.

## Contributions intermédiaires

7. **Prototyper le téléchargement des scrutins de la XVe législature**  
   Conserver l'archive brute, son empreinte et les métadonnées de provenance.

8. **Définir le modèle normalisé d'un scrutin**  
   Séparer scrutin, position de groupe et vote individuel.

9. **Créer un audit de symétrie**  
   Vérifier automatiquement qu'un indicateur traite les quatre familles selon la même règle.

10. **Comparer deux stratégies de stockage**  
    JSON/Parquet local contre PostgreSQL pour les premières données parlementaires.

## Recherche et méthodologie

11. **Revue des outils citoyens existants**  
    Étudier NosDéputés, Datan, Manifesto Project, Media Cloud et GDELT : fonctions réutilisables, licences et limites.

12. **Protocole de mesure du traitement médiatique**  
    Proposer des indicateurs descriptifs, des variables de contrôle et des tests de sensibilité.
