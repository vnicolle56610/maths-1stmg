---
title: "Taux de variation et fonctions monotones"
description: "Cours et exercices de Première STMG pour interpréter un taux de variation, le relier à une pente de sécante et caractériser la monotonie."
---

# N05 — Taux de variation et fonctions monotones

Le taux de variation mesure une évolution moyenne entre deux valeurs. Les documents le relient à la pente d’une sécante et à la monotonie d’une fonction sur un intervalle. Le travail fait le lien entre calcul, lecture graphique et interprétation d’une situation.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N04-fonctions-registres-lectures/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N04 — Fonctions : registres et lectures graphiques</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N06-second-degre-paraboles/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N06 — Fonctions du second degré : paraboles et formes simples</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Définir et interpréter un taux de variation.
- Relier taux de variation et pente d’une sécante.
- Caractériser une fonction monotone sur un intervalle.

## Voir aussi

- [N04 — Fonctions : registres et lectures graphiques](N04-fonctions-registres-lectures.md)
- [N11 — Nombre dérivé : sécantes, tangentes, interprétation](N11-nombre-derive-tangentes.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N05 — Taux de variation et fonctions monotones](../cours/COURS_N05_TAUX_VARIATION_FONCTIONS_MONOTONES.pdf)
- [TD N05 — Taux de variation et fonctions monotones](../td/TD_N05_TAUX_VARIATION_FONCTIONS_MONOTONES.pdf)
- [Automatismes N05 — Taux de variation et fonctions monotones](../automatismes/AUTOMATISMES_N05_TAUX_VARIATION_FONCTIONS_MONOTONES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Pour une fonction `f` et deux nombres distincts `a` et `b`, le taux de variation entre `a` et `b` est `τ(a;b) = (f(b)-f(a))/(b-a)` : il mesure la variation moyenne de `f(x)` par unité de variation de `x`, avec son unité propre (ce n'est pas un pourcentage). Graphiquement, ce taux est la pente de la sécante passant par `A(a ; f(a))` et `B(b ; f(b))`.

Le signe du taux indique le sens : `τ(a;b) > 0` si la sécante monte, `< 0` si elle descend, `= 0` si elle est horizontale. Une fonction est croissante sur un intervalle `I` lorsque, pour tous `a < b` dans `I`, `f(a) ⩽ f(b)` ; elle est décroissante lorsque `f(a) ⩾ f(b)`. Une fonction est croissante sur `I` si et seulement si tous ses taux de variation sur `I` sont positifs ou nuls (décroissante : négatifs ou nuls) — un seul taux calculé sur un intervalle ne renseigne que sur cet intervalle.

Pour une fonction affine `f(x) = mx+p`, le taux de variation entre deux nombres distincts vaut toujours `m` : le rythme de variation est constant, contrairement à une fonction non affine.

## Exemple

Le coût logistique `C(x)` d'une entreprise passe de 700 € à 1000 € entre 100 et 200 commandes, puis à 1600 € pour 350 commandes, puis à 2350 € pour 500 commandes.

Les taux de variation successifs sont `(1000-700)/(200-100) = 3`, `(1600-1000)/(350-200) = 4`, puis `(2350-1600)/(500-350) = 5` euros par commande. Tous positifs : le coût est croissant, mais pas à rythme constant.
