---
title: "Statistiques à deux variables : nuages et point moyen"
description: "Cours et exercices de Première STMG pour représenter une série à deux variables, calculer le point moyen et discuter une tendance."
---

# N15 — Statistiques à deux variables : nuages et point moyen

Une série statistique à deux variables met en relation deux grandeurs observées. Les ressources font représenter un nuage de points, calculer le point moyen et discuter l’existence d’une tendance. Cette lecture prépare l’ajustement affine, sans supposer qu’un modèle linéaire est toujours pertinent.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N14-synthese-analyse-gestion/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N14 — Synthèse d'analyse et problèmes de gestion</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N16-ajustement-affine/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N16 — Ajustement affine, interpolation et extrapolation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Représenter une série statistique à deux variables.
- Calculer le point moyen.
- Lire un nuage de points et discuter une tendance.

## Voir aussi

- [N16 — Ajustement affine, interpolation et extrapolation](N16-ajustement-affine.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N15 — Statistiques à deux variables : nuages et point moyen](../cours/COURS_N15_STATISTIQUES_DEUX_VARIABLES_NUAGES_POINT_MOYEN.pdf)
- [TD N15 — Statistiques à deux variables : nuages et point moyen](../td/TD_N15_STATISTIQUES_DEUX_VARIABLES_NUAGES_POINT_MOYEN.pdf)
- [Automatismes N15 — Statistiques à deux variables : nuages et point moyen](../automatismes/AUTOMATISMES_N15_STATISTIQUES_DEUX_VARIABLES_NUAGE_POINT_MOYEN.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Lorsqu'on observe sur les mêmes individus deux caractères quantitatifs `x` et `y`, l'ensemble des couples `(xᵢ ; yᵢ)` forme une série statistique à deux variables. Dans un repère, l'ensemble des points `Mᵢ(xᵢ ; yᵢ)` est le nuage de points : on ne relie jamais ces points entre eux. Le point moyen `G(x̄ ; ȳ)`, où `x̄` et `ȳ` sont les moyennes des deux séries, résume la position centrale du nuage — sans décrire ni sa dispersion ni sa forme, et sans être nécessairement l'un des points observés.

Un nuage peut suggérer une tendance croissante, décroissante, ou l'absence de tendance nette, ainsi que des points atypiques (qu'il ne faut pas supprimer automatiquement : ils peuvent être réels et informatifs). Une tendance observée ne prouve jamais une causalité entre les deux variables.

## Exemple

Une entreprise relève, pour six campagnes, la dépense publicitaire `x` (en milliers d'euros) et le chiffre d'affaires `y` (en milliers d'euros) : `(4;52), (6;58), (7;61), (9;70), (10;73), (12;80)`.

Le point moyen est `x̄ = (4+6+7+9+10+12)/6 = 8` et `ȳ = (52+58+61+70+73+80)/6 ≈ 65,7`, soit `G(8 ; 65,7)`. Le nuage monte globalement de la gauche vers la droite : on observe une tendance croissante entre dépense et chiffre d'affaires.
