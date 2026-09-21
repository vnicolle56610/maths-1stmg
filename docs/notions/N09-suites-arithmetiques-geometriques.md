---
title: "Suites arithmétiques et géométriques en STMG"
description: "Cours et exercices de Première STMG pour reconnaître des modèles discrets linéaires ou exponentiels, travailler récurrence et formule explicite."
---

# N09 — Suites arithmétiques et géométriques

Les suites arithmétiques et géométriques modélisent deux types d’évolutions discrètes. Les ressources font reconnaître un ajout constant ou une multiplication constante, travailler récurrence et formule explicite, puis comparer croissance linéaire et croissance exponentielle dans des situations accessibles. Les tableaux de valeurs aident à garder le sens des calculs.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N08-suites-numeriques-modeles/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N08 — Suites numériques : modèles discrets</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N10-evolution-seuils-python/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N10 — Modèles d'évolution, seuils, tableur et Python</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Reconnaître un modèle discret linéaire ou exponentiel.
- Travailler récurrence et formule explicite.
- Comparer croissances arithmétique et géométrique.

## Voir aussi

- [N08 — Suites numériques : modèles discrets](N08-suites-numeriques-modeles.md)
- [N10 — Modèles d’évolution, seuils, tableur et Python](N10-evolution-seuils-python.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N09 — Suites arithmétiques et géométriques](../cours/COURS_N09_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
- [TD N09 — Suites arithmétiques et géométriques](../td/TD_N09_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
- [Automatismes N09 — Suites arithmétiques et géométriques](../automatismes/AUTOMATISMES_N09_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une suite `u` est arithmétique lorsqu'on passe d'un terme au suivant en ajoutant toujours le même nombre `r`, la raison : `u(n+1) = u(n) + r` ; elle modélise une évolution absolue constante, et son terme général est `u(n) = u(0) + nr`. On la reconnaît en vérifiant que les différences `u(n+1)-u(n)` sont toutes égales.

Une suite `v` à termes strictement positifs est géométrique lorsqu'on passe d'un terme au suivant en multipliant toujours par le même nombre `q > 0`, la raison : `v(n+1) = q × v(n)` ; elle modélise une évolution relative constante, et son terme général est `v(n) = v(0) × qⁿ`. On la reconnaît en vérifiant que les quotients `v(n+1)/v(n)` sont tous égaux. Un taux d'évolution `t` se traduit en raison géométrique par `q = 1+t`.

Une suite arithmétique de raison `r` est strictement croissante si `r > 0`, décroissante si `r < 0`. Une suite géométrique positive de raison `q` est strictement croissante si `q > 1`, décroissante si `0 < q < 1`. Une suite n'est pas nécessairement de l'un de ces deux types : il faut vérifier que la règle est valable pour tous les rangs étudiés.

## Exemple

Deux magasins partent de 500 clients. Le magasin A gagne 40 clients par mois : `u(n) = 500 + 40n`, arithmétique de raison 40. Le magasin B gagne 8 % de clients par mois : `v(n) = 500 × 1,08ⁿ`, géométrique de raison 1,08.

Au rang 12 : `u(12) = 980`, tandis que `v(12) ≈ 1259`. Le modèle géométrique donne ici l'effectif le plus élevé, mais cette comparaison ne vaut que pour les rangs étudiés.
