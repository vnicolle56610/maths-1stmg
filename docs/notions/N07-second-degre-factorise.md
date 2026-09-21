---
title: "Second degré factorisé : racines, signe et problèmes"
description: "Cours et exercices de Première STMG pour utiliser une forme factorisée, trouver les racines et étudier le signe d’une expression du second degré."
---

# N07 — Second degré factorisé : racines, signe et problèmes

La forme factorisée rend visibles les racines d’une expression du second degré. Les ressources font vérifier une racine conjecturée, factoriser dans des cas simples et utiliser cette écriture pour étudier le signe. Ce travail prolonge la lecture des paraboles et sert dans des problèmes contextualisés.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N06-second-degre-paraboles/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N06 — Fonctions du second degré : paraboles et formes simples</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N08-suites-numeriques-modeles/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N08 — Suites numériques : modèles discrets</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Vérifier une racine conjecturée.
- Factoriser dans des cas simples lorsqu’une racine est connue.
- Utiliser une forme factorisée pour trouver racines et signe.

## Voir aussi

- [N06 — Fonctions du second degré : paraboles et formes simples](N06-second-degre-paraboles.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N07 — Second degré factorisé : racines, signe et problèmes](../cours/COURS_N07_SECOND_DEGRE_FACTORISE.pdf)
- [TD N07 — Second degré factorisé : racines, signe et problèmes](../td/TD_N07_SECOND_DEGRE_FACTORISE.pdf)
- [Automatismes N07 — Second degré factorisé : racines, signe et problèmes](../automatismes/AUTOMATISMES_N07_SECOND_DEGRE_FACTORISE_RACINES_SIGNE_PROBLEMES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Un nombre réel `α` est une racine d'un polynôme `P` lorsque `P(α) = 0` ; pour vérifier qu'un nombre conjecturé est une racine, on remplace `x` par ce nombre. Dans une forme factorisée `P(x) = a(x-x1)(x-x2)`, les racines sont directement `x1` et `x2`, car un produit est nul si et seulement si l'un de ses facteurs est nul. Lorsqu'une racine est déjà connue, on peut factoriser dans les cas simples en cherchant `P(x) = (x-α)(ax+d)`, puis en identifiant `d` par développement.

Pour `x1 < x2`, la forme `a(x-x1)(x-x2)` est du signe de `a` à l'extérieur des racines, et du signe opposé entre elles ; les racines elles-mêmes annulent l'expression. Dans un problème, « équilibre » se traduit souvent par `P(x) = 0`, « gain » par `P(x) > 0`, « perte » par `P(x) < 0` — on résout puis on croise avec l'intervalle admissible du contexte avant de conclure. Lorsqu'aucune factorisation simple n'apparaît, un balayage numérique donne un encadrement approché, jamais une valeur exacte.

## Exemple

Le bénéfice d'une entreprise, en milliers d'euros, est modélisé sur `[0 ; 10]` par `B(x) = -0,5(x-2)(x-8)`, où `x` est le nombre de centaines d'articles vendus.

Les racines sont 2 et 8 : ce sont les seuils d'équilibre. Comme le coefficient est négatif, `B(x) > 0` pour `x ∈ ]2 ; 8[` : l'entreprise réalise un bénéfice lorsqu'elle vend strictement entre 200 et 800 articles.
