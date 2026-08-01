# Transparence des financements politiques

## Objet du module

Ce module doit expliquer **comment les partis politiques se financent**, auprès de quels organismes et selon quelles formes juridiques, puis détecter des incohérences ou signaux nécessitant une vérification humaine.

Il ne constitue ni une enquête judiciaire ni un système capable de prouver automatiquement l’existence d’un financement occulte.

## Questions traitées

- Quelle part des ressources provient de l’aide publique ?
- Quelle part provient des dons, cotisations d’adhérents et contributions d’élus ?
- Quel est le niveau d’endettement du parti ?
- Les emprunts viennent-ils de banques, d’autres personnes morales autorisées ou de personnes physiques ?
- Quelle banque ou personne morale prêteuse est publiquement identifiée ?
- Les prêts sont-ils remboursés selon les informations publiées ?
- Existe-t-il des flux importants entre partis ou structures affiliées ?
- Les comptes ont-ils été certifiés, déposés à temps et déclarés conformes ?
- Une autorité ou une juridiction a-t-elle relevé un manquement ?

## Sources de financement à distinguer

1. aide publique directe ;
2. dons de personnes physiques ;
3. cotisations des adhérents ;
4. contributions des élus ;
5. prêts bancaires ;
6. prêts consentis par des personnes physiques ;
7. transferts provenant d’autres partis ou structures liées ;
8. ventes, prestations et produits financiers ;
9. produits exceptionnels ;
10. dettes fournisseurs et autres dettes.

Ces catégories doivent rester séparées. Un emprunt n’est pas une recette définitive et une dette fournisseur n’est pas un financement volontaire.

## Cadre juridique minimal

Les ressources d’un parti sont recueillies par un mandataire financier ou une association de financement agréée. Les partis transmettent chaque année leurs comptes, la liste de leurs donateurs et cotisants ainsi que les contrats de prêts de personnes physiques à la CNCCFP.

Les dons aux partis sont réservés aux personnes physiques françaises ou résidant en France et sont plafonnés. Les personnes morales privées ne peuvent pas effectuer de dons. Les prêts peuvent notamment provenir d’établissements de crédit ou de sociétés de financement établis dans l’Union européenne ou l’Espace économique européen. Les prêts de personnes physiques sont autorisés sous des conditions strictes et doivent être déclarés à la CNCCFP.

Références officielles :

- [Loi du 11 mars 1988 relative à la transparence financière de la vie politique](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000321646/)
- [Décret du 9 juillet 1990 relatif au financement politique](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000715369/)
- [Obligations annuelles des partis — CNCCFP](https://cnccfp.fr/partis-politiques/vous-etes-un-parti-politique/)

## Données publiques disponibles

La CNCCFP publie notamment :

- les comptes d’ensemble des partis ;
- le bilan, le compte de résultat et les annexes ;
- la composition de l’endettement par catégorie ;
- l’identité des prêteurs personnes morales lorsqu’elle figure dans la publication ;
- les flux financiers entre partis ;
- les décisions relatives au respect des obligations comptables ;
- les comptes non déposés, déposés tardivement ou non certifiés ;
- des jeux de données comptables ouverts sur data.gouv.fr.

Sources :

- [Comptes et publications des partis — CNCCFP](https://cnccfp.fr/partis-politiques/)
- [Jeu de données des comptes des partis — data.gouv.fr](https://www.data.gouv.fr/datasets/comptes-des-partis-et-groupements-politiques)
- [Publication des comptes des partis, exercice 2024](https://liste.cnccfp.fr/publications/comptes_partis_2024.html)

## Ce qui n’est pas publiquement accessible

La CNCCFP reçoit les listes nominatives des donateurs et cotisants ainsi que les contrats de prêts de personnes physiques. Ces informations ne doivent pas être assimilées à des données ouvertes.

PolitiTrace ne doit donc pas :

- publier ou tenter de reconstituer la liste des donateurs particuliers ;
- réidentifier une personne à partir de données agrégées ;
- attribuer une dette agrégée à un individu sans source publique nominative ;
- prétendre connaître l’origine économique réelle de fonds privés lorsque l’autorité de contrôle elle-même ne l’a pas établie.

La CNCCFP a publiquement signalé que le droit actuel ne lui permet pas toujours de vérifier l’origine des fonds prêtés ou donnés par une personne physique. Cette limite doit être affichée dans toute analyse.

Référence : [Propositions de la CNCCFP sur l’origine des fonds](https://liste.cnccfp.fr/docs/ra-2024/propositions.html)

## Modèle de données envisagé

### `finance_record`

- parti juridique ;
- exercice ;
- catégorie comptable ;
- montant ;
- source documentaire ;
- version du compte ;
- statut de certification ;
- date de publication ;
- empreinte du document.

### `lender`

- type : banque, société de financement, parti, autre personne morale, personne physique non publiée ;
- nom public, uniquement lorsqu’il est légalement publié ;
- pays du siège ;
- identifiant public de la personne morale ;
- source et date de vérification.

### `loan`

- prêteur ;
- emprunteur ;
- montant initial ;
- capital restant dû ;
- taux publié ;
- date de conclusion ;
- échéance ;
- remboursements ;
- garantie ;
- statut : normal, retard déclaré, déprécié, contentieux, inconnu.

### `financial_finding`

- type de constat ;
- indicateur déclencheur ;
- documents utilisés ;
- niveau de preuve ;
- validation humaine ;
- réponse éventuelle du parti ;
- statut juridique.

## Indicateurs descriptifs

- répartition des ressources en pourcentage ;
- dépendance à l’aide publique ;
- poids des dons et cotisations ;
- dette totale et dette rapportée aux produits annuels ;
- part des dettes bancaires, physiques, fournisseurs et inter-partis ;
- concentration des prêteurs personnes morales ;
- coût moyen apparent de la dette lorsque les taux sont disponibles ;
- échéances annuelles et capacité apparente de remboursement ;
- évolution des créances sur les candidats ;
- flux nets entre partis liés.

Les comparaisons doivent tenir compte de la taille, du statut parlementaire et du calendrier électoral.

## Signaux d’alerte

Un signal d’alerte est une invitation à vérifier, jamais une accusation.

Exemples :

- forte variation non expliquée d’une ressource ;
- dette importante auprès d’un prêteur unique ;
- prêt ancien non remboursé ou déprécié ;
- conditions de prêt inhabituellement favorables lorsqu’elles sont publiées ;
- dépendance extrême à une seule source ;
- flux importants entre structures liées ;
- discordance entre le bilan, les annexes et les décisions publiées ;
- comptes non certifiés, non déposés ou déposés hors délai ;
- réserve des commissaires aux comptes ;
- manquement signalé par la CNCCFP ;
- décision juridictionnelle ou condamnation définitive.

## Échelle de qualification

PolitiTrace doit employer une terminologie contrôlée :

1. `information_publique` — donnée reproduite sans interprétation ;
2. `anomalie_technique` — incohérence de format ou de calcul ;
3. `signal_alerte` — situation atypique nécessitant un examen ;
4. `manquement_constate` — manquement établi par une autorité compétente ;
5. `decision_officielle` — décision administrative ou juridictionnelle publiée ;
6. `condamnation_definitive` — décision définitive explicitement identifiée.

Les termes « financement occulte », « fraude », « corruption » ou « blanchiment » ne peuvent être employés comme constat du projet sans source officielle suffisamment probante.

## Procédure avant publication d’un signal nominatif

1. vérifier le document primaire ;
2. contrôler l’identité juridique du parti et du prêteur ;
3. rechercher une version corrigée ou plus récente ;
4. distinguer compte du parti et compte de campagne ;
5. vérifier les décisions de la CNCCFP et des juridictions ;
6. documenter les hypothèses alternatives ;
7. soumettre le constat à une revue humaine ;
8. permettre l’ajout d’une réponse ou d’une correction ;
9. afficher clairement qu’un signal n’est pas une preuve d’illégalité.

## Limite fondamentale

Les comptes publics permettent de détecter ce qui est déclaré, incohérent ou juridiquement relevé. Ils ne permettent pas, à eux seuls, de découvrir tous les flux dissimulés hors comptabilité.

PolitiTrace doit rendre cette frontière visible plutôt que donner une impression artificielle d’exhaustivité.

## Suivi

Le développement de ce module est suivi dans [l’issue #12](https://github.com/BlockSats/Polititrace-France/issues/12).
