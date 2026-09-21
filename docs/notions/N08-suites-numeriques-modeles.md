---
title: "Suites numériques : modèles discrets"
description: "Cours et exercices de Première STMG pour définir une suite, calculer des termes, utiliser différents modes de génération et représenter un modèle discret."
---

# N08 — Suites numériques : modèles discrets

Une suite numérique décrit une grandeur observée par étapes, souvent année après année ou période après période. Les ressources font utiliser différents modes de génération, calculer des termes et représenter graphiquement une suite. Le chapitre prépare les modèles arithmétiques et géométriques.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N07-second-degre-factorise/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N07 — Second degré factorisé : racines, signe et problèmes</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N09-suites-arithmetiques-geometriques/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N09 — Suites arithmétiques et géométriques</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Comprendre une suite comme modèle discret.
- Utiliser différents modes de génération.
- Calculer des termes et représenter une suite.

## Voir aussi

- [N09 — Suites arithmétiques et géométriques](N09-suites-arithmetiques-geometriques.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N08 — Suites numériques : modèles discrets](../cours/COURS_N08_SUITES_NUMERIQUES_MODELES_DISCRETS.pdf)
- [TD N08 — Suites numériques : modèles discrets](../td/TD_N08_SUITES_NUMERIQUES_MODELES_DISCRETS.pdf)
- [Automatismes N08 — Suites numériques : modèles discrets](../automatismes/AUTOMATISMES_N08_SUITES_NUMERIQUES_MODELES_DISCRETS.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une suite numérique est une liste ordonnée de nombres repérés par des entiers appelés rangs ; le nombre associé au rang `n` est noté `u(n)` — c'est le terme de rang `n`. Une évolution est discrète lorsqu'elle est observée à des étapes séparées (chaque mois, chaque année…), ce qui explique que les rangs soient des entiers.

Une suite peut être définie par une formule explicite, où `u(n)` s'exprime directement en fonction de `n` (utile pour calculer un terme éloigné), ou par une relation de récurrence, où l'on connaît un terme initial et une règle donnant chaque terme à partir du précédent (le calcul se fait alors pas à pas). La représentation graphique d'une suite est un nuage de points `(n ; u(n))` : les points ne sont jamais reliés, car aucun terme n'est défini entre deux rangs entiers. Une suite est croissante lorsque `u(n+1) ⩾ u(n)`, décroissante lorsque `u(n+1) ⩽ u(n)` ; elle peut aussi n'être ni l'une ni l'autre.

## Exemple

Deux modèles décrivent le nombre de comptes actifs d'une plateforme : `u(n) = 400 + 35n` (formule explicite) et `v(0) = 400`, `v(n+1) = 0,9 × v(n) + 80` (récurrence).

Avec `u`, on calcule directement `u(10)`. Avec `v`, il faut calculer successivement `v(1) = 440`, puis `v(2) = 476`, etc. : la récurrence impose un calcul pas à pas.
