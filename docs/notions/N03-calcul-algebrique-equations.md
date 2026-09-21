---
title: "Calcul algébrique, équations et signes"
description: "Cours et exercices de Première STMG pour consolider le calcul littéral, résoudre des équations produit nul et étudier le signe d’expressions simples."
---

# N03 — Calcul algébrique, équations et signes

Le calcul algébrique permet de transformer des expressions et de résoudre des problèmes. Les ressources consolident le calcul littéral simple, les équations produit nul et le signe d’une expression du premier degré. Ces outils servent ensuite dans les fonctions et le second degré.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N02-proportions-pourcentages-evolutions/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N02 — Proportions, pourcentages et évolutions</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N04-fonctions-registres-lectures/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N04 — Fonctions : registres et lectures graphiques</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Consolider le calcul littéral simple.
- Résoudre des équations produit nul.
- Déterminer le signe d’une expression du premier degré.

## Voir aussi

- [N06 — Fonctions du second degré : paraboles et formes simples](N06-second-degre-paraboles.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N03 — Calcul algébrique, équations et signes](../cours/COURS_N03_CALCUL_ALGEBRIQUE_EQUATIONS_SIGNES.pdf)
- [TD N03 — Calcul algébrique, équations et signes](../td/TD_N03_CALCUL_ALGEBRIQUE_EQUATIONS_SIGNES.pdf)
- [Automatismes N03 — Calcul algébrique, équations et signes](../automatismes/AUTOMATISMES_N03_CALCUL_ALGEBRIQUE_EQUATIONS_SIGNES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Développer transforme un produit en somme (`a(b+c) = ab+ac`) ; factoriser transforme une somme en produit (`ab+ac = a(b+c)`). Un produit de réels est nul si et seulement si l'un au moins de ses facteurs est nul : `A × B = 0 ⟺ A = 0 ou B = 0` — cette propriété ne s'applique qu'à un second membre égal à 0.

L'expression `ax+b` (avec `a ≠ 0`) s'annule en `x0 = -b/a` ; elle a le signe de `a` à droite de `x0`, et le signe opposé à gauche. Pour étudier le signe d'un produit `(ax+b)(cx+d)`, on calcule les zéros de chaque facteur, on les range dans l'ordre croissant, puis on multiplie les signes colonne par colonne dans un tableau de signes. Un zéro appartient à l'ensemble des solutions pour `⩾` ou `⩽`, mais pas pour `>` ou `<`.

## Exemple

Le bénéfice d'une opération commerciale est modélisé par `B(x) = (x-20)(60-x)`, où `x` est le nombre de lots vendus, avec `0 ⩽ x ⩽ 80`.

Les zéros 20 et 60 sont les seuils d'équilibre. Le tableau de signes donne `B(x) > 0` pour `20 < x < 60` : l'entreprise réalise un bénéfice sur cet intervalle, et subit une perte en dehors.
