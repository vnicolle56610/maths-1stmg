---
title: "Modèles d’évolution, seuils, tableur et Python"
description: "Cours et exercices de Première STMG pour utiliser suites et fonctions dans des modèles d’évolution, chercher un seuil et structurer une démarche avec tableur ou Python."
---

# N10 — Modèles d’évolution, seuils, tableur et Python

Les modèles d’évolution servent à prévoir quand une quantité franchit un seuil. Les ressources mobilisent suites, fonctions, tableur et Python pour organiser les calculs. L’objectif est de choisir un modèle, produire des valeurs fiables et interpréter le rang ou la date obtenue.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N09-suites-arithmetiques-geometriques/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N09 — Suites arithmétiques et géométriques</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N11-nombre-derive-tangentes/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N11 — Nombre dérivé : sécantes, tangentes, interprétation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Utiliser suites et fonctions pour étudier des évolutions.
- Chercher un rang seuil.
- Structurer une démarche avec tableur ou Python.

## Voir aussi

- [N02 — Proportions, pourcentages et taux d’évolution](N02-proportions-pourcentages-evolutions.md)
- [N09 — Suites arithmétiques et géométriques](N09-suites-arithmetiques-geometriques.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N10 — Modèles d’évolution, seuils, tableur et Python](../cours/COURS_N10_MODELES_EVOLUTION_SEUILS_TABLEUR_PYTHON.pdf)
- [TD N10 — Modèles d’évolution, seuils, tableur et Python](../td/TD_N10_MODELES_EVOLUTION_SEUILS_TABLEUR_PYTHON.pdf)
- [Automatismes N10 — Modèles d’évolution, seuils, tableur et Python](../automatismes/AUTOMATISMES_N10_MODELES_EVOLUTION_SEUILS_TABLEUR_PYTHON.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Le choix de l'outil dépend de la question posée : un terme isolé se calcule avec une formule explicite, une liste de termes s'obtient avec un tableur ou une boucle `for`, la recherche d'un rang seuil utilise une boucle `while`, et une somme se calcule avec un accumulateur.

Chercher un rang seuil, c'est déterminer le plus petit entier `n` pour lequel une condition devient vraie (par exemple `u(n) > 3000`). Pour justifier qu'un rang est bien le premier à vérifier la condition, on contrôle les deux inégalités : le rang précédent ne la vérifie pas encore, le rang trouvé la vérifie. Dans une boucle `while`, la condition de répétition est l'opposée de la condition recherchée : pour chercher `u(n) > S`, on répète tant que `u ⩽ S`.

La somme des termes de rangs 0 à `N`, notée `S = u(0) + u(1) + ⋯ + u(N)`, comporte `N+1` termes. Elle se calcule avec un tableur (fonction `SOMME`) ou avec un accumulateur Python qui mémorise le total au fur et à mesure — jamais avec une formule fermée toute faite.

## Exemple

Une entreprise a 2400 abonnés et prévoit une hausse de 4 % par an : `u(n) = 2400 × 1,04ⁿ`.

On calcule `u(5) ≈ 2920 ⩽ 3000` et `u(6) ≈ 3037 > 3000` : le rang 6 est donc bien le premier rang où le nombre d'abonnés dépasse 3000.
