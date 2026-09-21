---
title: "Variations et extremums par dérivation"
description: "Cours et exercices de Première STMG pour utiliser le signe de la dérivée, construire un tableau de variations et résoudre une optimisation simple."
---

# N13 — Variations et extremums par dérivation

Le signe de la dérivée permet d’organiser l’étude des variations d’une fonction. Les ressources font construire des tableaux de variations, repérer des extremums et traiter des problèmes simples d’optimisation. L’attention porte sur le lien entre calcul de dérivée, signe et interprétation graphique ou économique.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N12-fonction-derivee-polynomes/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N12 — Fonction dérivée et polynômes de degré au plus 3</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N14-synthese-analyse-gestion/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N14 — Synthèse d'analyse et problèmes de gestion</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Relier le signe de la dérivée aux variations.
- Construire un tableau de variations.
- Résoudre un problème d’optimisation simple.

## Voir aussi

- [N12 — Fonction dérivée et polynômes de degré au plus 3](N12-fonction-derivee-polynomes.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N13 — Variations et extremums par dérivation](../cours/COURS_N13_VARIATIONS_EXTREMUMS_DERIVATION.pdf)
- [TD N13 — Variations et extremums par dérivation](../td/TD_N13_VARIATIONS_EXTREMUMS_DERIVATION.pdf)
- [Automatismes N13 — Variations et extremums par dérivation](../automatismes/AUTOMATISMES_N13_VARIATIONS_EXTREMUMS_DERIVATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Sur un intervalle `I`, si `f'(x) ⩾ 0`, alors `f` est croissante sur `I` ; si `f'(x) ⩽ 0`, alors `f` est décroissante. Pour étudier les variations : calculer `f'(x)`, résoudre `f'(x) = 0`, étudier le signe de `f'`, puis en déduire les variations et les valeurs utiles de `f`. Si `f'` change de signe de négatif à positif en `a`, `f` admet un minimum local en `a` ; de positif à négatif, un maximum local.

Sur un intervalle fermé, un extremum local n'est pas nécessairement l'extremum sur tout l'intervalle : il faut comparer les valeurs de `f` aux points critiques et aux deux bornes avant de conclure. Une optimisation en contexte se conclut toujours par une interprétation avec les unités.

## Exemple

Le bénéfice d'une entreprise, en milliers d'euros, est `P(x) = -x² + 48x - 320` pour `x ∈ [0 ; 40]`, où `x` est un nombre de centaines d'articles.

`P'(x) = -2x + 48` est positif sur `[0 ; 24[`, nul en 24, négatif sur `]24 ; 40]` : `P` croît puis décroît, avec un maximum en `x = 24`. Comme `P(24) = 256`, le bénéfice maximal est de 256 000 euros pour une production de 2400 articles.
