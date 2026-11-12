---
title: "Pourcentages, proportions et taux d’évolution"
description: "Cours et exercices de Première STMG sur proportions, pourcentages, coefficients multiplicateurs, taux d’évolution et évolutions successives."
---

# N02 — Proportions, pourcentages et taux d’évolution

Un pourcentage permet de comparer des parts, mesurer une évolution et interpréter des données économiques ou sociales. Les ressources font travailler le passage entre taux et coefficient multiplicateur, le calcul d’une valeur initiale ou finale, les évolutions successives et les évolutions réciproques.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N01-rentree-donnees-logique/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N01 — Rentrée, données, logique et automatismes</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N03-calcul-algebrique-equations/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N03 — Calcul algébrique, équations et signes</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

!!! objectifs ""

    - Passer d’un taux à un coefficient multiplicateur.
    - Calculer une valeur initiale ou finale.
    - Traiter des évolutions successives ou réciproques.

## Voir aussi

- [N05 — Taux de variation et fonctions monotones](N05-taux-variation-fonctions.md)
- [N10 — Modèles d’évolution, seuils, tableur et Python](N10-evolution-seuils-python.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N02 — Proportions, pourcentages et taux d’évolution](../cours/COURS_N02_PROPORTIONS_POURCENTAGES_EVOLUTIONS.pdf)
- [TD N02 — Proportions, pourcentages et taux d’évolution](../td/TD_N02_PROPORTIONS_POURCENTAGES_EVOLUTIONS.pdf)
- [Corrigé TD N02](../corriges/CORRIGE_TD_N02_PROPORTIONS_POURCENTAGES_EVOLUTIONS.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N02 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N02-proportions-pourcentages-evolutions.md)
<!-- AUTOMATISMES-WEB:END -->

<!-- AUTO-EVAL:START -->
- 🎯 Évaluée au DS1 du mardi 24 novembre : [devoir blanc en ligne le mardi 17 novembre](../preparer-evaluation/index.md#ds1-2026-2027)
<!-- AUTO-EVAL:END -->

## Notions essentielles

!!! essentiel ""

    Dans une population de référence d'effectif `N`, une sous-population d'effectif `n` représente la proportion `p = n/N`. Passer de `40 %` à `42 %` correspond à une hausse de 2 points de pourcentage, ce qui n'est pas la même chose qu'une hausse relative de `(42-40)/40 = 5 %` : il faut distinguer les deux.

    Pour une valeur passant de `Vi` à `Vf`, le taux d'évolution est `t = (Vf-Vi)/Vi`, et le coefficient multiplicateur associé est `CM = 1 + t`, avec `Vf = Vi × CM`. Pour des évolutions successives, les coefficients multiplicateurs se multiplient : `CM_global = CM1 × CM2 × …` (les taux, eux, ne s'additionnent généralement pas). L'évolution réciproque, qui ramène de la valeur finale à la valeur initiale, a pour coefficient `1/CM`.

    Un indice base 100 attribue la valeur 100 à une période de référence `V0` ; pour une valeur `V`, l'indice est `I = 100 × V/V0`. Entre deux indices `Ii` et `If`, le taux d'évolution se calcule comme pour deux valeurs : `t = (If-Ii)/Ii`.

## Exemple

!!! exemple ""

    Deux remises successives de 15 % puis 10 % ont pour coefficients `0,85` et `0,90`. Le coefficient global est `0,85 × 0,90 = 0,765`.

    Le taux global vaut `0,765 - 1 = -0,235`, soit une remise totale de 23,5 % — et non 25 %, car les taux ne s'additionnent pas.

## Repère historique — Stevin et le calcul des intérêts successifs

!!! historique ""

    Simon Stevin, tables d’intérêts, 1582
    {: .frise data-annee="1582" }

    En 1582, Simon Stevin publie des tables d’intérêts, précédées de règles et d’exemples sur les intérêts simples et composés. Ces calculs répondent à un besoin financier : déterminer comment une somme évolue avec le temps. La distinction essentielle porte sur la base du calcul. Avec des intérêts simples, l’intérêt est calculé sur le capital initial ; avec des intérêts composés, les intérêts conservés s’ajoutent au capital et produisent à leur tour des intérêts.

    Voici une illustration moderne fictive, avec nos notations actuelles : un capital de 100 € augmente de 10 % par an pendant deux ans, les intérêts étant capitalisés, sans frais ni versement supplémentaire. Il devient `100 × 1,10 = 110` €, puis `110 × 1,10 = 121` €. La hausse totale est donc de 21 %, et non de 20 %. Comme pour les remises successives du chapitre, les coefficients se multiplient parce que la valeur de référence change. Le même outil permet de traiter une hausse ou une baisse ; le contexte précise le coefficient à employer.

    Source : [MacTutor, université de St Andrews, Simon Stevin, tables d’intérêts de 1582](https://mathshistory.st-andrews.ac.uk/Biographies/Stevin/).
