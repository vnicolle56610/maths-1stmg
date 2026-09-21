---
title: "Ajustement affine, interpolation et extrapolation"
description: "Cours et exercices de Première STMG pour déterminer un ajustement affine, l’utiliser en interpolation ou extrapolation et critiquer le modèle."
---

# N16 — Ajustement affine, interpolation et extrapolation

L’ajustement affine propose une droite pour résumer une tendance statistique. Les documents font déterminer cette droite, l’utiliser pour interpoler ou extrapoler, puis critiquer la pertinence du modèle. Les prévisions doivent rester liées au contexte et aux limites des données, surtout lorsque l’on sort de la zone observée.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N15-statistiques-deux-variables/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N15 — Statistiques à deux variables : nuages et point moyen</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N17-probabilites-conditionnelles/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N17 — Probabilités conditionnelles et indépendance</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Déterminer un ajustement affine.
- Utiliser une droite d’ajustement pour interpoler ou extrapoler.
- Critiquer la pertinence d’un modèle.

## Voir aussi

- [N15 — Statistiques à deux variables : nuages et point moyen](N15-statistiques-deux-variables.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N16 — Ajustement affine, interpolation et extrapolation](../cours/COURS_N16_AJUSTEMENT_AFFINE_INTERPOLATION_EXTRAPOLATION.pdf)
- [TD N16 — Ajustement affine, interpolation et extrapolation](../td/TD_N16_AJUSTEMENT_AFFINE_INTERPOLATION_EXTRAPOLATION.pdf)
- [Automatismes N16 — Ajustement affine, interpolation et extrapolation](../automatismes/AUTOMATISMES_N16_AJUSTEMENT_AFFINE_INTERPOLATION_EXTRAPOLATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Un ajustement affine approche un nuage de points presque rectiligne par une droite `y = ax+b`, qui résume une tendance globale. Il peut être obtenu au jugé (tracé visuel entre deux points lisibles), par la méthode de Mayer (on partage la série en deux groupes de même effectif, on calcule leurs points moyens `G1` et `G2`, et la droite `(G1G2)` est la droite d'ajustement — elle passe par le point moyen global), ou par une droite dite « des moindres carrés », fournie par une calculatrice, un tableur ou un logiciel : aucune théorie de calcul n'est exigée, cette droite est seulement lue sur l'outil.

Interpoler, c'est estimer `y` pour une valeur de `x` intérieure à l'intervalle des abscisses observées ; extrapoler, c'est l'estimer pour une valeur extérieure à cet intervalle. Une interpolation est généralement moins risquée qu'une extrapolation proche, et une extrapolation lointaine peut être très peu fiable même si le calcul est correct : le modèle affine ne doit jamais être prolongé indéfiniment, car des contraintes réelles peuvent limiter la grandeur étudiée.

## Exemple

Pour une série budget publicitaire / ventes, un outil donne la droite d'ajustement `y ≈ 2,67x + 9,13`, avec des abscisses observées entre 2 et 12.

Pour `x = 9`, on obtient `y ≈ 33,2` : comme `9 ∈ [2 ; 12]`, c'est une interpolation. Pour `x = 15`, on obtient `y ≈ 49,2` : comme `15 > 12`, c'est une extrapolation, à interpréter avec davantage de prudence.
