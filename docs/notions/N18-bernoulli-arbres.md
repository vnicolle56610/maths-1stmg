---
title: "Épreuves indépendantes de Bernoulli et arbres"
description: "Cours et exercices de Première STMG pour reconnaître une épreuve de Bernoulli et représenter des répétitions indépendantes avec un arbre."
---

# N18 — Épreuves indépendantes de Bernoulli et arbres

Une épreuve de Bernoulli n’a que deux issues : succès ou échec. Les ressources font reconnaître ce modèle, représenter des répétitions indépendantes et construire des arbres jusqu’à un nombre limité d’épreuves. Le calcul reste guidé par la structure de l’arbre.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N17-probabilites-conditionnelles/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N17 — Probabilités conditionnelles et indépendance</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N19-variables-aleatoires-esperance/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N19 — Variables aléatoires, espérance et simulation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

- Reconnaître une épreuve de Bernoulli.
- Représenter des répétitions indépendantes.
- Construire et exploiter un arbre jusqu’à n ≤ 4.

## Voir aussi

- [N17 — Probabilités conditionnelles et indépendance](N17-probabilites-conditionnelles.md)
- [N19 — Variables aléatoires, espérance et simulation](N19-variables-aleatoires-esperance.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N18 — Épreuves indépendantes de Bernoulli et arbres](../cours/COURS_N18_EPREUVES_BERNOULLI_REPETITIONS_INDEPENDANTES.pdf)
- [TD N18 — Épreuves indépendantes de Bernoulli et arbres](../td/TD_N18_EPREUVES_BERNOULLI_REPETITIONS_INDEPENDANTES.pdf)
- [Automatismes N18 — Épreuves indépendantes de Bernoulli et arbres](../automatismes/AUTOMATISMES_N18_EPREUVES_INDEPENDANTES_BERNOULLI_ARBRES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une épreuve de Bernoulli est une expérience aléatoire à exactement deux issues : le succès `S`, de probabilité `p`, et l'échec `S̄`, de probabilité `1-p`. Le mot « succès » est une simple convention : il ne signifie pas forcément un résultat favorable dans le contexte.

Répéter une même épreuve de Bernoulli de façon identique et indépendante signifie que la probabilité de succès reste `p` à chaque étape, et que le résultat d'une étape ne modifie pas les probabilités des étapes suivantes : les mêmes probabilités réapparaissent alors à chaque niveau de l'arbre, et la probabilité d'un chemin est le produit des probabilités de ses branches. On se limite à au plus 4 répétitions : pour calculer la probabilité d'un événement, on traduit l'événement en termes de `S` et `S̄`, on repère tous les chemins qui le réalisent, on calcule chaque chemin, puis on additionne. Pour « au moins un succès », il est souvent plus court de passer par l'événement contraire : `P(au moins un S) = 1 - P(aucun S)`.

## Exemple

Une entreprise envoie une offre à trois clients indépendants, chacun l'acceptant avec une probabilité de 0,30.

« Exactement deux succès » correspond aux trois chemins `SSS̄`, `SS̄S`, `S̄SS`, chacun de probabilité `0,30² × 0,70 = 0,063`. La probabilité cherchée est donc `3 × 0,063 = 0,189`.
