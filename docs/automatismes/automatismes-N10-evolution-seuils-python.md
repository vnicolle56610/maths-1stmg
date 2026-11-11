---
title: "Automatismes Première STMG – Modèles d’évolution, seuils, tableur et Python : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première STMG (modèles d’évolution, seuils, tableur et Python), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N10 — Modèles d’évolution, seuils, tableur et Python

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N10-evolution-seuils-python.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N10_MODELES_EVOLUTION_SEUILS_TABLEUR_PYTHON.pdf){ .md-button }
[📖 Revoir la notion](../notions/N10-evolution-seuils-python.md){ .md-button }
</div>

## Série A — Termes et sommes finies

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer rapidement des termes et des sommes courtes.
</div>

<ol class="auto-questions">
<li value="1">Calculer <span class="arithmatex">\(120+15\times4\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(200\times1{,}05\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(50+55+60\)</span>.</li>
<li value="4">Pour <span class="arithmatex">\(u(n)=30+8n\)</span>, calculer <span class="arithmatex">\(u(6)\)</span>.</li>
<li value="5">Pour <span class="arithmatex">\(v(n)=100\times1{,}1^n\)</span>, calculer <span class="arithmatex">\(v(2)\)</span>.</li>
<li value="6">Une offre coûte <span class="arithmatex">\(12\)</span> euros par mois pendant <span class="arithmatex">\(6\)</span> mois. Calculer le total.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Identifier la formule avant de calculer.</li><li>Une somme finie additionne plusieurs termes.</li><li>Garder les unités : euros, clients, objets.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre le rang <span class="arithmatex">\(n\)</span> avec le nombre de termes additionnés.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\boxed{180}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\boxed{210}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\boxed{165}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(30+8\times6=\boxed{78}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(100\times1{,}21=\)</span><wbr><span class="arithmatex">\(\boxed{121}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(12\times6=\boxed{72}\)</span> euros.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour un modèle explicite, remplacer <span class="arithmatex">\(n\)</span> par le rang demandé.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Dans une somme, compter les termes réellement additionnés.</div>

## Série B — Rang seuil

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Déterminer à partir de quel rang un seuil est dépassé.
</div>

<ol class="auto-questions">
<li value="1">Suite <span class="arithmatex">\(u(n)=50+10n\)</span>. À partir de quel rang <span class="arithmatex">\(u(n)\geqslant 100\)</span> ?</li>
<li value="2">Suite <span class="arithmatex">\(u(n)=20+5n\)</span>. À partir de quel rang <span class="arithmatex">\(u(n)&gt;50\)</span> ?</li>
<li value="3">Valeurs : <span class="arithmatex">\(80;96;115{,}2;138{,}24\)</span>. Quel est le premier terme supérieur à <span class="arithmatex">\(100\)</span> ?</li>
<li value="4">Une clientèle vaut <span class="arithmatex">\(300\)</span> puis augmente de <span class="arithmatex">\(50\)</span> par mois. Quand dépasse-t-elle <span class="arithmatex">\(500\)</span> ?</li>
<li value="5">Si <span class="arithmatex">\(u(0)=40\)</span> et <span class="arithmatex">\(u(n+1)=u(n)+7\)</span>, calculer le premier rang tel que <span class="arithmatex">\(u(n)\geqslant61\)</span>.</li>
<li value="6">Compléter : chercher un seuil, c'est chercher le premier rang pour lequel une condition devient <span class="arithmatex">\(\ldots\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Tester les rangs dans l'ordre.</li><li>Le mot « à partir de » demande le premier rang.</li><li>Différencier <span class="arithmatex">\(&gt;\)</span> et <span class="arithmatex">\(\geqslant\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le rang seuil n'est pas toujours la valeur du terme.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(50+10n\geqslant100\)</span> : premier rang <span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(20+5n&gt;50\)</span> : <span class="arithmatex">\(n&gt;6\)</span>, premier rang <span class="arithmatex">\(\boxed{7}\)</span>.</li>
    <li value="3">Premier terme supérieur à <span class="arithmatex">\(100\)</span> : <span class="arithmatex">\(\boxed{115{,}2}\)</span>, rang <span class="arithmatex">\(2\)</span>.</li>
    <li value="4"><span class="arithmatex">\(300+50n&gt;500\)</span> : premier mois <span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(40;47;54;61\)</span> : premier rang <span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{\text{vraie}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Pour une condition stricte <span class="arithmatex">\(&gt;\)</span>, l'égalité ne suffit pas.</div>

## Série C — Tableur et algorithme

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Lire une formule de tableur ou un petit algorithme.
</div>

<ol class="auto-questions">
<li value="1">En B2, on a <span class="arithmatex">\(120\)</span>. En B3 : <code>=B2+8</code>. Quelle valeur en B3 ?</li>
<li value="2">En B2, on a <span class="arithmatex">\(200\)</span>. En B3 : <code>=B2*1,04</code>. Quelle valeur en B3 ?</li>
<li value="3">Si on recopie <code>=B2+8</code> vers le bas, quel type de suite obtient-on ?</li>
<li value="4">Si on recopie <code>=B2*0,95</code> vers le bas, quel type de suite obtient-on ?</li>
<li value="5">Algorithme : <span class="arithmatex">\(n=0\)</span>, <span class="arithmatex">\(u=100\)</span>. Tant que <span class="arithmatex">\(u&lt;140\)</span> : <span class="arithmatex">\(u=u+10\)</span>, <span class="arithmatex">\(n=n+1\)</span>. Valeur finale de <span class="arithmatex">\(n\)</span> ?</li>
<li value="6">Dans un programme, pourquoi initialise-t-on <span class="arithmatex">\(n=0\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une formule recopiée décrit une récurrence.</li><li>Addition constante : arithmétique.</li><li>Multiplication constante : géométrique.</li></ul>
    <p><strong>Vigilance</strong></p><p>Dans une boucle, chaque passage augmente souvent le rang d'une unité.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\boxed{128}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\boxed{208}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\boxed{\text{arithmétique}}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\boxed{\text{géométrique}}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(100;110;120;130;140\)</span> : <span class="arithmatex">\(\boxed{n=4}\)</span>.</li>
    <li value="6">Pour partir du <span class="arithmatex">\(\boxed{\text{rang initial}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> La boucle « tant que » continue tant que la condition est vraie.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> On sort de la boucle dès que la condition devient fausse.</div>

## Série D — QCM : évolutions et seuils

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la bonne réponse sans calculatrice.
</div>

<ol class="auto-questions">
<li value="1">Un capital de <span class="arithmatex">\(1000\)</span> augmente de <span class="arithmatex">\(3\%\)</span>.<ol class="auto-choix" type="A"><li><span class="arithmatex">\(1030\)</span></li><li><span class="arithmatex">\(1003\)</span></li><li><span class="arithmatex">\(970\)</span></li><li><span class="arithmatex">\(3000\)</span></li></ol></li>
<li value="2">Modèle <span class="arithmatex">\(u(n)=250-20n\)</span>. Le seuil <span class="arithmatex">\(u(n)\leqslant150\)</span> est atteint au rang<ol class="auto-choix" type="A"><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(100\)</span></li></ol></li>
<li value="3">Une formule <code>=B2*1,07</code> correspond à<ol class="auto-choix" type="A"><li><span class="arithmatex">\(+7\)</span></li><li><span class="arithmatex">\(+7\%\)</span></li><li><span class="arithmatex">\(-7\%\)</span></li><li><span class="arithmatex">\(\times7\)</span></li></ol></li>
<li value="4">La somme <span class="arithmatex">\(10+15+20+25\)</span> vaut<ol class="auto-choix" type="A"><li><span class="arithmatex">\(60\)</span></li><li><span class="arithmatex">\(70\)</span></li><li><span class="arithmatex">\(75\)</span></li><li><span class="arithmatex">\(80\)</span></li></ol></li>
<li value="5">Dans une boucle de seuil, la variable <span class="arithmatex">\(n\)</span> sert à<ol class="auto-choix" type="A"><li>compter les rangs</li><li>stocker le seuil</li><li>calculer un pourcentage</li><li>écrire le titre</li></ol></li>
<li value="6">Si <span class="arithmatex">\(u(0)=500\)</span> et <span class="arithmatex">\(u(n+1)=0{,}8u(n)\)</span>, le stock<ol class="auto-choix" type="A"><li>augmente</li><li>diminue</li><li>reste constant</li><li>double</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Identifier le modèle : ajout, multiplication, somme ou seuil.</li><li>Tester les réponses proches.</li><li>Ne pas utiliser la calculatrice : calculs choisis pour être mentaux.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le seuil demandé est un rang, pas seulement une valeur.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(1000\times1{,}03=1030\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(250-20\times5=150\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : coefficient <span class="arithmatex">\(1{,}07\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(10+15+20+25=70\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse A</strong> : compter les rangs</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(0&lt;0{,}8&lt;1\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Les automatismes de seuil combinent calcul, comparaison et interprétation.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un coefficient multiplicateur inférieur à <span class="arithmatex">\(1\)</span> traduit une baisse.</div>

---

*Ces questions reprennent le diaporama d'automatismes N10 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
