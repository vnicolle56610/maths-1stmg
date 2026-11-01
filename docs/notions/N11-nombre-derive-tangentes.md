---
title: "Nombre dérivé : sécantes, tangentes et interprétation"
description: "Cours et exercices de Première STMG pour introduire le nombre dérivé, interpréter des pentes de sécante et de tangente, et lire une variation instantanée."
---

# N11 — Nombre dérivé : sécantes, tangentes, interprétation

Le nombre dérivé apparaît comme une pente limite : on part des sécantes pour arriver à la tangente. Les ressources privilégient l’interprétation graphique et le lien avec une variation instantanée. Ce chapitre prépare la fonction dérivée et les tableaux de variations.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N10-evolution-seuils-python/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N10 — Modèles d'évolution, seuils, tableur et Python</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N12-fonction-derivee-polynomes/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N12 — Fonction dérivée et polynômes de degré au plus 3</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

!!! objectifs ""

    - Introduire le nombre dérivé par un point de vue graphique.
    - Interpréter une pente de sécante puis de tangente.
    - Relier le nombre dérivé à une variation instantanée.

## Voir aussi

- [N05 — Taux de variation et fonctions monotones](N05-taux-variation-fonctions.md)
- [N12 — Fonction dérivée et polynômes de degré au plus 3](N12-fonction-derivee-polynomes.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N11 — Nombre dérivé : sécantes, tangentes, interprétation](../cours/COURS_N11_NOMBRE_DERIVE_SECANTES_TANGENTES.pdf)
- [TD N11 — Nombre dérivé : sécantes, tangentes, interprétation](../td/TD_N11_NOMBRE_DERIVE_SECANTES_TANGENTES.pdf)
- [Automatismes N11 — Nombre dérivé : sécantes, tangentes, interprétation](../automatismes/AUTOMATISMES_N11_NOMBRE_DERIVE_SECANTES_TANGENTES_INTERPRETATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

!!! essentiel ""

    Le taux de variation de `f` entre `a` et `b`, `(f(b)-f(a))/(b-a)`, est le coefficient directeur de la sécante passant par les points d'abscisses `a` et `b`. Lorsqu'on rapproche progressivement le second point du premier, les sécantes se rapprochent d'une droite unique : la tangente à la courbe. Lorsque les coefficients directeurs des sécantes se rapprochent ainsi d'un nombre unique, ce nombre est le nombre dérivé de `f` en `a`, noté `f'(a)` — c'est le coefficient directeur de la tangente.

    Le signe de `f'(a)` se lit sur la tangente : montante (`f'(a) > 0`), horizontale (`f'(a) = 0`), descendante (`f'(a) < 0`). Le nombre dérivé s'interprète comme une variation instantanée (ou marginale) : pour une petite augmentation de `x` autour de `a`, la variation de `f(x)` est approximativement donnée par cette pente.

## Exemple

!!! exemple ""

    Le coût total de `x` articles est `C(x) = 0,05x² + 20x + 500`. Le taux `τ_h = (C(100+h)-C(100))/h` vaut successivement 31, puis 30,5, puis 30,25, puis 30,05 lorsque `h` vaut 20, 10, 5, 1.

    Ces valeurs se rapprochent de 30 : on obtient `C'(100) = 30`. Autour de 100 articles, produire un article de plus augmente le coût d'environ 30 euros.

## Repère historique — Newton et la mesure d’un changement local

!!! historique ""

    Isaac Newton, années 1660
    {: .frise data-annee="1665" data-etiquette="années 1660" }

    Dans les années 1660, Isaac Newton étudie des grandeurs qui varient avec le temps et leurs vitesses de variation, qu’il appelle des fluxions. Le mouvement fournit ainsi une manière de penser le changement : une position et une vitesse ne décrivent pas la même chose. Ces travaux contribuent à la naissance du calcul différentiel ; la définition moderne du nombre dérivé par une limite sera précisée ultérieurement.

    Dans le modèle de coût moderne fictif de l’exemple, `C'(100) = 30` décrit une variation locale, et non le coût total de fabrication de 100 articles. Avec nos notations actuelles, la pente entre les productions 100 et 101 vaut `C(101)-C(100) = 30,05` euros par article. Elle est proche de 30, mais différente : le coût du prochain article est ici une différence entre deux valeurs, tandis que la dérivée donne la pente de la tangente au modèle continu. L’interprétation économique est actuelle, sans être attribuée à Newton. Rapprocher les deux points de la courbe permet de comprendre pourquoi cette pente locale peut fournir une approximation utile, dont il faut conserver les unités et les limites.

    Source : [MacTutor, université de St Andrews, histoire du calcul et fluxions de Newton](https://mathshistory.st-andrews.ac.uk/HistTopics/The_rise_of_calculus/).
