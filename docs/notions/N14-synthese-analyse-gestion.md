---
title: "Synthèse d’analyse et problèmes de gestion"
description: "Révisions de Première STMG pour articuler fonctions, suites, dérivation et modèles dans des problèmes de gestion."
---

# N14 — Synthèse d’analyse et problèmes de gestion

Cette synthèse rassemble les outils d’analyse utiles dans des situations de gestion : fonctions, suites, dérivation, modèles discrets ou continus. Les exercices demandent de choisir une représentation, d’exploiter un calcul et d’interpréter le résultat. La page reste large car elle prépare des exercices plus longs et moins guidés.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N13-variations-extremums/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N13 — Variations et extremums par dérivation</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N15-statistiques-deux-variables/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N15 — Statistiques à deux variables : nuages et point moyen</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

!!! objectifs ""

    - Articuler fonctions, suites et dérivation.
    - Choisir un modèle discret ou continu.
    - Préparer les exercices longs de l’épreuve anticipée.

## Voir aussi

- [N10 — Modèles d’évolution, seuils, tableur et Python](N10-evolution-seuils-python.md)
- [N13 — Variations et extremums par dérivation](N13-variations-extremums.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N14 — Synthèse d’analyse et problèmes de gestion](../cours/COURS_N14_SYNTHESE_ANALYSE_PROBLEMES_GESTION.pdf)
- [TD N14 — Synthèse d’analyse et problèmes de gestion](../td/TD_N14_SYNTHESE_ANALYSE_PROBLEMES_GESTION.pdf)
- [Automatismes N14 — Synthèse d’analyse et problèmes de gestion](../automatismes/AUTOMATISMES_N14_SYNTHESE_ANALYSE_PROBLEMES_GESTION.pdf)
<!-- AUTO-DOCS:END -->

## Points essentiels à maîtriser

!!! essentiel ""

    Un modèle est discret lorsque la grandeur est observée à des étapes séparées (mois, trimestres, années…) : on utilise alors une suite `u(n)`. Il est continu lorsque la variable peut prendre toutes les valeurs d'un intervalle : on utilise alors une fonction `f(x)`. Une même situation peut se décrire par quatre registres complémentaires — phrase, tableau, formule, représentation graphique — qui s'articulent entre eux.

    Pour organiser un problème long, une démarche en six étapes est utile : comprendre (grandeurs, unités, question), définir (variable ou suite, domaine), modéliser (formule, récurrence ou fonction), traiter (calculer, dériver, résoudre), contrôler (ordre de grandeur, bornes, cohérence), interpréter (phrase liée à la décision de gestion). Une suite répond typiquement à une question d'échéance (rang seuil), une fonction à une question d'optimisation (extremum) — une décision complète peut mobiliser les deux modèles, sans mélanger leurs variables, et doit toujours être confrontée aux contraintes réelles (capacité, budget, valeurs entières).

## Exemple de synthèse

!!! exemple ""

    Une entreprise suit son nombre d'abonnés par trimestre, `u(n) = 1200 × 1,06ⁿ`, et son bénéfice quotidien selon la quantité produite, `B(x) = -0,5x² + 30x - 150` sur `[0 ; 50]`.

    Pour les abonnés (modèle discret), on cherche un rang seuil : `u(3) ≈ 1429 < 1500` et `u(4) ≈ 1515 > 1500`, donc le seuil de 1500 abonnés est franchi au 4ᵉ trimestre. Pour le bénéfice (modèle continu), on optimise : `B'(x) = -x+30` s'annule en 30, où `B` passe de croissante à décroissante : le bénéfice maximal est `B(30) = 300` milliers d'euros pour 3000 unités. Ces deux résultats répondent à des questions différentes et ne se mélangent pas.

## Repère historique — Cournot met les relations économiques en équations

!!! historique ""

    Antoine Augustin Cournot, *Recherches sur les principes mathématiques de la théorie des richesses*, 1838
    {: .frise data-annee="1838" }

    En 1838, Antoine Augustin Cournot publie ses Recherches sur les principes mathématiques de la théorie des richesses. Il y étudie des relations entre prix, production et demande à l’aide de fonctions. Cette démarche fait de lui un pionnier de l’économie mathématique : une hypothèse économique devient une relation que l’on peut représenter et analyser. Une conclusion calculée dépend alors des hypothèses retenues ; elle ne décrit pas automatiquement toutes les entreprises ni tous les marchés.

    Dans une illustration moderne fictive, une entreprise vend `q` articles par jour à un prix unitaire supposé égal à `p(q) = 50-q` euros, pour `0 ⩽ q ⩽ 40`. La recette quotidienne est donc `R(q) = q(50-q)` euros. Le modèle continu donne `R'(q) = 50-2q`, puis une recette maximale de 625 € pour 25 articles. Ce résultat concerne la recette, pas le bénéfice : les coûts ne sont pas renseignés. Ce seul modèle ne prévoit pas non plus l’évolution des ventes d’un trimestre à l’autre. Choisir les grandeurs, les unités et la question permet ainsi d’articuler les outils de la synthèse sans confondre leurs rôles.

    Source : [MacTutor, université de St Andrews, Cournot et son ouvrage économique de 1838](https://mathshistory.st-andrews.ac.uk/Biographies/Cournot/).
