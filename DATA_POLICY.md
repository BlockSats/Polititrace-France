# Politique des données

## Principe

Le dépôt est open source. Cela n'autorise pas à republier des contenus tiers sans respecter leur licence, le droit d'auteur, les conditions d'utilisation et la protection des données personnelles.

## Catégories

- `data/raw/` : données obtenues de la source, généralement non versionnées dans Git ;
- `data/interim/` : données de travail reproductibles ;
- `data/processed/` : données normalisées publiables lorsque la licence le permet ;
- `data/metadata/` : provenance, empreintes, dates, licences et schémas.

## Presse et audiovisuel

Par défaut, conserver uniquement les métadonnées nécessaires : URL, média, auteur, date, titre, bref extrait autorisé, empreinte et résultats analytiques. Ne pas committer la copie intégrale d'un article protégé.

## Provenance minimale

Chaque lot doit enregistrer :

- URL ou identifiant source ;
- organisme producteur ;
- date de collecte ;
- licence ou conditions connues ;
- version ou période ;
- empreinte du fichier ;
- script de transformation ;
- schéma de sortie.

## Données personnelles

Ne collecter que les données nécessaires à l'analyse de l'activité publique. Exclure les adresses privées, coordonnées personnelles et données sensibles sans justification juridique et méthodologique.

## Retrait

Toute demande fondée de correction ou de retrait doit être examinée et documentée. Les secrets et données personnelles ne doivent jamais être publiés dans une issue.
