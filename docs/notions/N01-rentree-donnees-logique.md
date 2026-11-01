---
title: "Rentrée, données, logique et automatismes"
description: "Cours et exercices de Première STMG pour diagnostiquer les acquis de Seconde et réactiver calculs, données, lectures graphiques et logique."
---

# N01 — Rentrée, données, logique et automatismes

Le début d’année sert à installer les routines de travail et à repérer les acquis utiles. Les ressources réactivent les calculs simples, les proportions, les lectures graphiques, les données et quelques réflexes de logique. Cette page reste diagnostique : elle prépare les chapitres suivants sans annoncer un cours complet sur chacun d’eux.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--next" href="../N02-proportions-pourcentages-evolutions/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N02 — Proportions, pourcentages et évolutions</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

!!! objectifs ""

    - Installer les routines de travail.
    - Diagnostiquer les acquis de Seconde utiles en STMG.
    - Réactiver proportions, lectures graphiques, calculs simples et logique.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N01 — Rentrée, données, logique et automatismes](../cours/COURS_N01_RENTREE_DONNEES_LOGIQUE_AUTOMATISMES.pdf)
- [TD N01 — Rentrée, données, logique et automatismes](../td/TD_N01_RENTREE_DONNEES_LOGIQUE_AUTOMATISMES.pdf)
- [Automatismes N01 — Rentrée, données, logique et automatismes](../automatismes/AUTOMATISMES_N01_RENTREE_DONNEES_LOGIQUE.pdf)
- [Corrigé TD N01](../corriges/CORRIGE_TD_N01_RENTREE_DONNEES_LOGIQUE_AUTOMATISMES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

!!! essentiel ""

    Un ensemble rassemble des objets : si `x` appartient à `A`, on écrit `x ∈ A` ; dire que `A` est inclus dans `B` (`A ⊂ B`) signifie que tout élément de `A` appartient à `B`. L'intersection `A ∩ B` correspond au « et », la réunion `A ∪ B` au « ou » inclusif. Pour montrer qu'une affirmation générale est fausse, un seul contre-exemple suffit.

    Un tableau croisé répartit une population selon deux critères : chaque case intérieure donne un effectif, et les totaux de lignes et de colonnes servent à contrôler le tableau. Une case ne désigne plus un individu particulier, mais un nombre d'individus.

    Une identité est une égalité vraie pour toutes les valeurs autorisées des lettres ; une équation n'est vraie que pour certaines valeurs de l'inconnue, qu'il s'agit de déterminer.

## Exemple

!!! exemple ""

    Dans une entreprise de 10 personnes réparties en trois services, un tableau croisé service/formation donne, pour le service Gestion, 2 personnes formées et 1 non formée, soit un total de 3.

    La case « 2 » à la ligne Gestion et à la colonne Formés signifie que deux personnes du service Gestion ont suivi la formation — ce n'est plus une information sur une personne précise, mais un effectif.

## Repère historique — Des cartes de Hollerith aux effectifs croisés

!!! historique ""

    Herman Hollerith, recensement américain, 1890
    {: .frise data-annee="1890" }

    Comment compter une population nombreuse selon plusieurs critères sans recompter toutes les fiches à la main ? Pour le recensement américain de 1890, le système de Herman Hollerith utilise des cartes perforées : les renseignements recueillis sur les personnes sont codés par des trous. Une machine électrique permet ensuite de compter et de croiser des caractéristiques. Ce dispositif distingue deux niveaux que l’on retrouve dans le chapitre : les informations individuelles et les effectifs obtenus en regroupant les individus.

    Dans un exemple actuel fictif, une entreprise classe ses salariés par service et selon qu’ils ont suivi ou non une formation. La case « Gestion et formés » compte les personnes qui satisfont simultanément les deux critères : c’est le sens du « et » et de l’intersection. Elle ne représente pas une fiche individuelle. Vérifier les totaux de lignes et de colonnes permet de contrôler que la répartition couvre bien l’ensemble du personnel sans double comptage. L’automatisation du calcul ne dispense donc pas de comprendre ce que chaque case compte.

    Source : [U.S. Census Bureau, le recensement de 1890 et son système de dépouillement](https://www.census.gov/programs-surveys/decennial-census/decade/1890/about-1890.html).
