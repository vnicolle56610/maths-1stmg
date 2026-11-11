---
title: "Fonction dérivée et polynômes de degré au plus 3"
description: "Cours et exercices de Première STMG pour calculer des dérivées simples, utiliser la linéarité et préparer l’étude des variations de polynômes."
---

# N12 — Fonction dérivée et polynômes de degré au plus 3

La fonction dérivée donne une méthode de calcul pour étudier les variations. Les ressources portent sur les dérivées simples, la linéarité et les polynômes de degré au plus 3. Cette étape prépare les tableaux de variations : il faut d’abord calculer correctement avant d’interpréter le signe de la dérivée.

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N11-nombre-derive-tangentes/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N11 — Nombre dérivé : sécantes, tangentes, interprétation</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N13-variations-extremums/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N13 — Variations et extremums par dérivation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

## Objectifs

!!! objectifs ""

    - Calculer des dérivées simples.
    - Utiliser les règles de linéarité.
    - Préparer l’étude de variations par le signe de la dérivée.

## Voir aussi

- [N11 — Nombre dérivé : sécantes, tangentes, interprétation](N11-nombre-derive-tangentes.md)
- [N13 — Variations et extremums par dérivation](N13-variations-extremums.md)

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N12 — Fonction dérivée et polynômes de degré au plus 3](../cours/COURS_N12_FONCTION_DERIVEE_POLYNOMES_DEGRE_3.pdf)
- [TD N12 — Fonction dérivée et polynômes de degré au plus 3](../td/TD_N12_FONCTION_DERIVEE_POLYNOMES_DEGRE_3.pdf)
- [Automatismes N12 — Fonction dérivée et polynômes de degré au plus 3](../automatismes/AUTOMATISMES_N12_FONCTION_DERIVEE_POLYNOMES_DEGRE_3.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N12 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N12-fonction-derivee-polynomes.md)
<!-- AUTOMATISMES-WEB:END -->

## Notions essentielles

!!! essentiel ""

    La fonction qui, à chaque réel `x` d'un intervalle, associe le nombre dérivé `f'(x)`, s'appelle la fonction dérivée de `f`. Sur `ℝ`, les dérivées de référence sont : `(c)' = 0` pour une constante, `(x)' = 1`, `(x²)' = 2x`, `(x³)' = 3x²`. La dérivée d'une somme est la somme des dérivées, et `(kf)' = k×f'` : pour dériver un polynôme de degré au plus 3, on dérive chaque terme puis on réduit — les règles du produit et du quotient ne sont pas nécessaires ici.

    La tangente à la courbe de `f` au point d'abscisse `a` a pour équation `y = f(a) + f'(a)(x-a)` : il faut calculer `f(a)`, déterminer `f'(x)`, calculer `f'(a)`, puis remplacer et développer.

## Exemple

!!! exemple ""

    Pour `P(x) = 4x³ - 3x² + 7x - 5`, on dérive terme à terme : `P'(x) = 4×3x² - 3×2x + 7 = 12x² - 6x + 7`.

    Pour la tangente, avec `f(x) = x³ - 2x + 1` en `a = 1` : `f(1) = 0` et `f'(x) = 3x² - 2` donne `f'(1) = 1`. L'équation réduite de la tangente est donc `y = x - 1`.

## Repère historique — Leibniz organise le calcul des dérivées

!!! historique ""

    Gottfried Wilhelm Leibniz, *Acta Eruditorum*, 1684
    {: .frise data-annee="1684" }

    En 1684, Gottfried Wilhelm Leibniz publie dans les Acta Eruditorum une méthode de calcul différentiel comportant des règles de calcul. L’enjeu est de disposer d’opérations réutilisables, plutôt que de reconstruire pour chaque courbe une méthode de tangente particulière. Ses notations contribuent à la diffusion de ce calcul. Il ne faut toutefois pas lui attribuer notre définition moderne de la dérivée comme limite ni toutes les conventions actuelles du cours.

    Voici une illustration moderne fictive, avec les règles de ce chapitre : un coût est modélisé par `C(x) = 2x³ + 5x + 100`, pour `x` entre 0 et 10, en unités adaptées à la situation. On dérive terme à terme et l’on obtient `C'(x) = 6x² + 5`. Si le coût fixe passe de 100 à 150, la dérivée reste la même : une constante déplace la courbe verticalement, sans modifier la pente en chaque abscisse. Ce rapprochement entre formule et graphique donne du sens à la règle « la dérivée d’une constante est nulle ». Seules les règles sur les puissances, les sommes et les multiples sont nécessaires ici.

    Source : [MacTutor, université de St Andrews, Leibniz et sa publication de 1684](https://mathshistory.st-andrews.ac.uk/Biographies/Leibniz/).
