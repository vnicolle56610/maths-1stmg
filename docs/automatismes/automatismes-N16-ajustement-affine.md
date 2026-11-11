---
title: "Automatismes Première STMG – Ajustement affine, interpolation et extrapolation : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première STMG (ajustement affine, interpolation et extrapolation), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N16 — Ajustement affine, interpolation et extrapolation

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N16-ajustement-affine.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N16_AJUSTEMENT_AFFINE_INTERPOLATION_EXTRAPOLATION.pdf){ .md-button }
[📖 Revoir la notion](../notions/N16-ajustement-affine.md){ .md-button }
</div>

## Série A — Utiliser une droite d'ajustement

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer rapidement avec une droite donnée.
</div>

<ol class="auto-questions">
<li value="1">Pour la droite <span class="arithmatex">\(y=2x+5\)</span>, calculer <span class="arithmatex">\(y\)</span> si <span class="arithmatex">\(x=4\)</span>.</li>
<li value="2">Avec <span class="arithmatex">\(y=2x+5\)</span>, calculer <span class="arithmatex">\(y\)</span> si <span class="arithmatex">\(x=10\)</span>.</li>
<li value="3">Avec <span class="arithmatex">\(y=2x+5\)</span>, résoudre <span class="arithmatex">\(y=25\)</span>.</li>
<li value="4">Dans <span class="arithmatex">\(y=2x+5\)</span>, quel est le coefficient directeur ?</li>
<li value="5">Dans <span class="arithmatex">\(y=2x+5\)</span>, quelle est l'ordonnée à l'origine ?</li>
<li value="6">Si <span class="arithmatex">\(x\)</span> augmente de <span class="arithmatex">\(1\)</span>, de combien <span class="arithmatex">\(y\)</span> augmente-t-il ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Remplacer <span class="arithmatex">\(x\)</span> par la valeur demandée.</li><li>Dans <span class="arithmatex">\(y=ax+b\)</span>, <span class="arithmatex">\(a\)</span> est le coefficient directeur.</li><li>Résoudre <span class="arithmatex">\(2x+5=25\)</span> par équivalences.</li></ul>
    <p><strong>Vigilance</strong></p><p>Une valeur prévue par ajustement est une estimation, pas une certitude.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(y=2\times4+5=\boxed{13}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(y=2\times10+5=\boxed{25}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(2x+5=25\Longleftrightarrow\)</span><wbr><span class="arithmatex">\( 2x=20\Longleftrightarrow\)</span><wbr><span class="arithmatex">\( x=\boxed{10}\)</span>.</li>
    <li value="4">Le coefficient directeur est <span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="5">L'ordonnée à l'origine est <span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="6">Quand <span class="arithmatex">\(x\)</span> augmente de <span class="arithmatex">\(1\)</span>, <span class="arithmatex">\(y\)</span> augmente de <span class="arithmatex">\(\boxed{2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une droite d'ajustement permet de prévoir une valeur par calcul sur le modèle.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le calcul est exact dans le modèle, mais la prévision reste approximative pour les données réelles.</div>

## Série B — Interpolation ou extrapolation

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Décider si une prévision reste dans la zone observée.
</div>

<ol class="auto-questions">
<li value="1">Les données observées vont de <span class="arithmatex">\(x=2019\)</span> à <span class="arithmatex">\(x=2024\)</span>. Prévoir <span class="arithmatex">\(x=2022\)</span> : interpolation ou extrapolation ?</li>
<li value="2">Mêmes données. Prévoir <span class="arithmatex">\(x=2027\)</span> : interpolation ou extrapolation ?</li>
<li value="3">Les <span class="arithmatex">\(x\)</span> observés vont de <span class="arithmatex">\(0\)</span> à <span class="arithmatex">\(50\)</span>. Prévoir pour <span class="arithmatex">\(x=20\)</span>.</li>
<li value="4">Les <span class="arithmatex">\(x\)</span> observés vont de <span class="arithmatex">\(0\)</span> à <span class="arithmatex">\(50\)</span>. Prévoir pour <span class="arithmatex">\(x=80\)</span>.</li>
<li value="5">Quelle prévision est généralement la plus risquée : interpolation ou extrapolation ?</li>
<li value="6">Pourquoi une extrapolation très lointaine doit-elle être critiquée ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Comparer la valeur demandée à l'intervalle observé.</li><li>Interpolation : dedans ; extrapolation : dehors.</li><li>Plus on s'éloigne, plus l'incertitude augmente.</li></ul>
    <p><strong>Vigilance</strong></p><p>Un calcul possible n'est pas toujours une prévision pertinente.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(2022\)</span> est dans l'intervalle observé : <strong class="auto-resultat">interpolation</strong>.</li>
    <li value="2"><span class="arithmatex">\(2027\)</span> est hors de l'intervalle : <strong class="auto-resultat">extrapolation</strong>.</li>
    <li value="3"><span class="arithmatex">\(20\in[0;50]\)</span> : <strong class="auto-resultat">interpolation</strong>.</li>
    <li value="4"><span class="arithmatex">\(80\notin[0;50]\)</span> : <strong class="auto-resultat">extrapolation</strong>.</li>
    <li value="5">La plus risquée est <strong class="auto-resultat">l'extrapolation</strong>.</li>
    <li value="6">Le modèle peut ne plus être valable loin des données : <strong class="auto-resultat">prudence</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Toujours situer la valeur demandée par rapport aux valeurs observées.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'extrapolation n'est pas interdite, mais elle doit être interprétée avec réserve.</div>

## Série C — Ajustement par deux points

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Déterminer rapidement une équation de droite.
</div>

<ol class="auto-questions">
<li value="1">Une droite passe par <span class="arithmatex">\(A(0;12)\)</span> et <span class="arithmatex">\(B(4;20)\)</span>. Calculer son coefficient directeur.</li>
<li value="2">Avec ces deux points, donner l'équation réduite de la droite.</li>
<li value="3">Utiliser cette droite pour prévoir <span class="arithmatex">\(y\)</span> lorsque <span class="arithmatex">\(x=6\)</span>.</li>
<li value="4">La prévision pour <span class="arithmatex">\(x=6\)</span> est-elle une extrapolation si les données vont de <span class="arithmatex">\(0\)</span> à <span class="arithmatex">\(4\)</span> ?</li>
<li value="5">Une droite d'ajustement passe-t-elle toujours par tous les points du nuage ?</li>
<li value="6">Une droite d'ajustement doit-elle passer près du point moyen ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Coefficient directeur : <span class="arithmatex">\(\frac{y_B-y_A}{x_B-x_A}\)</span>.</li><li>Si <span class="arithmatex">\(A(0;12)\)</span>, alors <span class="arithmatex">\(b=12\)</span>.</li><li>Relier le calcul à la zone observée.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre ajustement affine et interpolation exacte de tous les points.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(a=\)</span><wbr><span class="arithmatex">\(\frac{20-12}{4-0}=\)</span><wbr><span class="arithmatex">\(\frac{8}{4}=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="2">Comme <span class="arithmatex">\(b=12\)</span>, l'équation est <span class="arithmatex">\(\boxed{y=2x+12}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(y=2\times6+12=\boxed{24}\)</span>.</li>
    <li value="4">Oui, <span class="arithmatex">\(6&gt;4\)</span> : <strong class="auto-resultat">extrapolation</strong>.</li>
    <li value="5">Non, elle passe seulement <strong class="auto-resultat">au plus près</strong> du nuage.</li>
    <li value="6">Oui, elle doit être cohérente avec <strong class="auto-resultat">le point moyen</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une droite d'ajustement <span class="arithmatex">\(y=ax+b\)</span> se lit comme un modèle de tendance.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'ajustement au juge est visuel ; il doit rester cohérent avec le nuage.</div>

## Série D — QCM type épreuve

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1">Dans <span class="arithmatex">\(y=3x-4\)</span>, le coefficient directeur est<ol class="auto-choix" type="A"><li><span class="arithmatex">\(3\)</span></li><li><span class="arithmatex">\(-4\)</span></li><li><span class="arithmatex">\(x\)</span></li><li><span class="arithmatex">\(y\)</span></li></ol></li>
<li value="2">Avec <span class="arithmatex">\(y=3x-4\)</span>, pour <span class="arithmatex">\(x=5\)</span>, <span class="arithmatex">\(y=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(11\)</span></li><li><span class="arithmatex">\(15\)</span></li><li><span class="arithmatex">\(19\)</span></li><li><span class="arithmatex">\(-1\)</span></li></ol></li>
<li value="3">Prévoir hors de la plage observée s'appelle<ol class="auto-choix" type="A"><li>interpolation</li><li>extrapolation</li><li>dérivation</li><li>factorisation</li></ol></li>
<li value="4">Un ajustement affine est représenté par<ol class="auto-choix" type="A"><li>une droite</li><li>un cercle</li><li>un arbre</li><li>un tableau de signes</li></ol></li>
<li value="5">Une extrapolation très lointaine est<ol class="auto-choix" type="A"><li>toujours exacte</li><li>à interpréter avec prudence</li><li>impossible à écrire</li><li>une probabilité</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer la forme <span class="arithmatex">\(y=ax+b\)</span>.</li><li>Calcul mental puis choix.</li><li>Identifier le vocabulaire.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le modèle ne garantit pas la réalité future.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse A</strong> : Réponse : coefficient directeur <span class="arithmatex">\(3\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse A</strong> : Réponse : <span class="arithmatex">\(3\times5-4=11\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : Réponse : extrapolation.</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : Réponse : une droite.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : Réponse : prudence.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En QCM, associer rapidement chaque mot à son registre : droite, prévision, modèle.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un bon ajustement se juge aussi graphiquement et dans le contexte.</div>

---

*Ces questions reprennent le diaporama d'automatismes N16 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
