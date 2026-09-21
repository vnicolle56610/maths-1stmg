---
title: "Variables aléatoires, espérance et simulation"
description: "Cours et exercices de Première STMG pour définir une variable aléatoire discrète, calculer une loi, une espérance et simuler une loi de Bernoulli."
---

# N19 — Variables aléatoires, espérance et simulation

Une variable aléatoire associe une valeur numérique aux issues d’une expérience. Les ressources font établir une loi de probabilité, calculer une espérance et utiliser la simulation, notamment autour de la loi de Bernoulli. L’objectif est d’interpréter le résultat moyen attendu, pas seulement d’appliquer une formule.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N18-bernoulli-arbres/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N18 — Épreuves indépendantes de Bernoulli et arbres</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N20-synthese-annuelle-epreuve/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N20 — Synthèse annuelle et préparation à l'épreuve anticipée</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Définir une variable aléatoire discrète en contexte.
- Calculer une loi de probabilité et une espérance.
- Reconnaître et simuler une loi de Bernoulli.

## Voir aussi

- [N18 — Épreuves indépendantes de Bernoulli et arbres](N18-bernoulli-arbres.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N19 — Variables aléatoires, espérance et simulation](../cours/COURS_N19_VARIABLES_ALEATOIRES_ESPERANCE_SIMULATION.pdf)
- [TD N19 — Variables aléatoires, espérance et simulation](../td/TD_N19_VARIABLES_ALEATOIRES_ESPERANCE_SIMULATION.pdf)
- [Automatismes N19 — Variables aléatoires, espérance et simulation](../automatismes/AUTOMATISMES_N19_VARIABLES_ALEATOIRES_ESPERANCE_SIMULATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une variable aléatoire discrète `X` associe un nombre réel à chaque issue d'une expérience aléatoire. Sa loi de probabilité associe à chaque valeur possible `xᵢ` la probabilité `P(X=xᵢ)`, avec la somme de toutes ces probabilités égale à 1 ; les valeurs `xᵢ` elles-mêmes ne sont pas des probabilités, elles peuvent être négatives (un gain algébrique, par exemple).

L'espérance de `X` est `E(X) = x1×p1 + ⋯ + xn×pn` : une moyenne pondérée des valeurs possibles. Ce n'est pas nécessairement une valeur que `X` peut prendre, et elle ne prédit pas le résultat d'une expérience unique — elle s'interprète comme la moyenne observée sur un grand nombre de répétitions comparables. La loi de Bernoulli de paramètre `p` correspond à `X=1` en cas de succès et `X=0` en cas d'échec, avec `P(X=1)=p` ; son espérance est `E(X) = p`.

Une simulation permet d'observer la fluctuation d'échantillonnage : deux échantillons de même taille, obtenus avec le même paramètre `p`, ne donnent généralement pas exactement la même fréquence de succès. Lorsque la taille de l'échantillon augmente, les fréquences observées ont tendance à se concentrer davantage autour de `p`.

## Exemple

Un jeu promotionnel fait gagner 0 € (60 % des clients), 2 € (30 %) ou 8 € (10 %). En notant `X` le montant du bon gagné :

`E(X) = 0×0,60 + 2×0,30 + 8×0,10 = 1,40`. L'enseigne doit prévoir un coût moyen de 1,40 € par client, sur un grand nombre de clients — ce n'est le montant gagné par aucun client en particulier.
