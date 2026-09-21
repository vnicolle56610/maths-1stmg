---
title: "Probabilités conditionnelles et indépendance"
description: "Cours et exercices de Première STMG pour utiliser arbres, tableaux croisés, probabilités conditionnelles, indépendance et probabilités totales."
---

# N17 — Probabilités conditionnelles et indépendance

Les probabilités conditionnelles servent à tenir compte d’une information déjà connue. Les ressources consolident les arbres et tableaux croisés, puis introduisent l’indépendance et la formule des probabilités totales. L’enjeu est de choisir le bon événement de référence avant de calculer.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N16-ajustement-affine/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N16 — Ajustement affine, interpolation et extrapolation</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N18-bernoulli-arbres/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N18 — Épreuves indépendantes de Bernoulli et arbres</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Consolider les arbres et tableaux croisés.
- Calculer une probabilité conditionnelle.
- Introduire indépendance et probabilités totales.

## Voir aussi

- [N18 — Épreuves indépendantes de Bernoulli et arbres](N18-bernoulli-arbres.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N17 — Probabilités conditionnelles et indépendance](../cours/COURS_N17_PROBABILITES_CONDITIONNELLES_INDEPENDANCE.pdf)
- [TD N17 — Probabilités conditionnelles et indépendance](../td/TD_N17_PROBABILITES_CONDITIONNELLES_INDEPENDANCE.pdf)
- [Automatismes N17 — Probabilités conditionnelles et indépendance](../automatismes/AUTOMATISMES_N17_PROBABILITES_CONDITIONNELLES_INDEPENDANCE.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Si `P(A) > 0`, la probabilité de `B` sachant `A` est `P_A(B) = P(A∩B)/P(A)`, d'où la formule du produit `P(A∩B) = P(A) × P_A(B)`. Il faut bien distinguer `P(A∩B)`, `P_A(B)` et `P_B(A)` : ces trois nombres portent sur des dénominateurs différents et répondent à des questions différentes.

Dans un arbre pondéré, la somme des probabilités des branches issues d'un même nœud vaut 1, et la probabilité d'un chemin est le produit des probabilités rencontrées ; on additionne les probabilités des chemins incompatibles qui réalisent le même événement final. Comme `A` et `Ā` forment une partition de l'univers, la formule des probabilités totales donne, pour tout événement `B` : `P(B) = P(A)×P_A(B) + P(Ā)×P_Ā(B)`.

Deux événements `A` et `B` sont indépendants lorsque `P_A(B) = P(B)`, ce qui équivaut à `P(A∩B) = P(A)×P(B)`. Indépendance et incompatibilité sont deux notions différentes : deux événements incompatibles de probabilités non nulles ne sont jamais indépendants.

## Exemple

Un site étudie 1000 commandes : 300 sont express, 80 sont en retard, et 45 sont à la fois express et en retard.

`P(E∩R) = 45/1000 = 0,045` ; parmi les commandes express, `P_E(R) = 45/300 = 0,15` ; parmi les commandes en retard, `P_R(E) = 45/80 = 0,5625`. Ces trois calculs portent sur les mêmes 45 commandes, mais sur des univers de référence différents : toutes les commandes, puis les commandes express, puis les commandes en retard.
