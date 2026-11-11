---
title: "Automatismes Première STMG – Probabilités conditionnelles et indépendance : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première STMG (probabilités conditionnelles et indépendance), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N17 — Probabilités conditionnelles et indépendance

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N17-probabilites-conditionnelles.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N17_PROBABILITES_CONDITIONNELLES_INDEPENDANCE.pdf){ .md-button }
[📖 Revoir la notion](../notions/N17-probabilites-conditionnelles.md){ .md-button }
</div>

## Série A — Distinguer intersection et conditionnement

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Identifier la probabilité demandée avant de calculer.
</div>

<ol class="auto-questions">
<li value="1">Traduire <span class="arithmatex">\(P(A\cap B)\)</span> en phrase courte.</li>
<li value="2">Traduire <span class="arithmatex">\(P_A(B)\)</span> en phrase courte.</li>
<li value="3">Si <span class="arithmatex">\(P(A)=0{,}6\)</span> et <span class="arithmatex">\(P_A(B)=0{,}3\)</span>, calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="4">Si <span class="arithmatex">\(P(B)=0{,}4\)</span> et <span class="arithmatex">\(P_B(A)=0{,}5\)</span>, calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(P(A\cap B)=0{,}18\)</span> et <span class="arithmatex">\(P(A)=0{,}6\)</span>, calculer <span class="arithmatex">\(P_A(B)\)</span>.</li>
<li value="6">Si <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont indépendants, quelle égalité utilise-t-on ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li><span class="arithmatex">\(P_A(B)\)</span> signifie : parmi les cas de <span class="arithmatex">\(A\)</span>.</li><li>Intersection : les deux événements se produisent.</li><li>Indépendance : le conditionnement ne change pas la probabilité.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre <span class="arithmatex">\(P(A\cap B)\)</span> et <span class="arithmatex">\(P_A(B)\)</span>.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(A\cap B)\)</span> : <strong class="auto-resultat"><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span></strong>.</li>
    <li value="2"><span class="arithmatex">\(P_A(B)\)</span> : <strong class="auto-resultat">probabilité de <span class="arithmatex">\(B\)</span> sachant <span class="arithmatex">\(A\)</span></strong>.</li>
    <li value="3"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}6\times0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}18}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}4\times0{,}5=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}20}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P_A(B)=\)</span><wbr><span class="arithmatex">\(\frac{0{,}18}{0{,}6}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}3}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> indépendants : <span class="arithmatex">\(\boxed{P(A\cap B)=P(A)P(B)}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La notation <span class="arithmatex">\(P_A(B)\)</span> se lit toujours de gauche à droite : sachant <span class="arithmatex">\(A\)</span>, probabilité de <span class="arithmatex">\(B\)</span>.</div>

## Série B — Lire un arbre pondéré

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer avec les branches d'un arbre simple.
</div>

<ol class="auto-questions">
<li value="1">On a <span class="arithmatex">\(P(A)=0{,}7\)</span>. Calculer <span class="arithmatex">\(P(\overline A)\)</span>.</li>
<li value="2">On a <span class="arithmatex">\(P(A)=0{,}7\)</span> et <span class="arithmatex">\(P_A(B)=0{,}2\)</span>. Calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="3">On a <span class="arithmatex">\(P(\overline A)=0{,}3\)</span> et <span class="arithmatex">\(P_{\overline A}(B)=0{,}5\)</span>. Calculer <span class="arithmatex">\(P(\overline A\cap B)\)</span>.</li>
<li value="4">Calculer <span class="arithmatex">\(P(B)\)</span> avec les deux résultats précédents.</li>
<li value="5">Dans un arbre, additionne-t-on ou multiplie-t-on le long d'un chemin ?</li>
<li value="6">Dans un arbre, additionne-t-on ou multiplie-t-on des chemins incompatibles ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une branche complémentaire complète à <span class="arithmatex">\(1\)</span>.</li><li>Un chemin se multiplie.</li><li>Plusieurs chemins qui mènent au même événement s'additionnent.</li></ul>
    <p><strong>Vigilance</strong></p><p>La formule des probabilités totales additionne des intersections.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(\overline A)=\)</span><wbr><span class="arithmatex">\(1-0{,}7=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}3}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}7\times0{,}2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}14}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(\overline A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}3\times0{,}5=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}15}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P(B)=\)</span><wbr><span class="arithmatex">\(0{,}14+0{,}15=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}29}\)</span>.</li>
    <li value="5">Le long d'un chemin, on <strong class="auto-resultat">multiplie</strong>.</li>
    <li value="6">Des chemins incompatibles, on <strong class="auto-resultat">additionne</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Vérifier que les probabilités issues d'un même nœud totalisent <span class="arithmatex">\(1\)</span>.</div>

## Série C — Tableau croisé et indépendance

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Passer d'un tableau à des probabilités.
</div>

<ol class="auto-questions">
<li value="1">Dans un groupe de <span class="arithmatex">\(100\)</span> élèves : <span class="arithmatex">\(A\cap B=24\)</span>, <span class="arithmatex">\(A\cap\overline B=36\)</span>, <span class="arithmatex">\(\overline A\cap B=16\)</span>, <span class="arithmatex">\(\overline A\cap\overline B=\)</span><wbr><span class="arithmatex">\(24\)</span>. Calculer <span class="arithmatex">\(P(A)\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(P(B)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="4">Calculer <span class="arithmatex">\(P_A(B)\)</span>.</li>
<li value="5">Calculer <span class="arithmatex">\(P_B(A)\)</span>.</li>
<li value="6">Les événements <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont-ils indépendants ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Transformer les effectifs en fréquences sur <span class="arithmatex">\(100\)</span>.</li><li><span class="arithmatex">\(A\)</span> totalise les deux cases de la ligne <span class="arithmatex">\(A\)</span>.</li><li>Comparer <span class="arithmatex">\(P(A\cap B)\)</span> à <span class="arithmatex">\(P(A)P(B)\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le dénominateur d'une probabilité conditionnelle n'est pas toujours <span class="arithmatex">\(100\)</span>.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(A)=\)</span><wbr><span class="arithmatex">\(\frac{24+36}{100}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}60}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(B)=\)</span><wbr><span class="arithmatex">\(\frac{24+16}{100}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}40}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(\frac{24}{100}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}24}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P_A(B)=\)</span><wbr><span class="arithmatex">\(\frac{24}{60}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}40}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P_B(A)=\)</span><wbr><span class="arithmatex">\(\frac{24}{40}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}60}\)</span>.</li>
    <li value="6">Oui, car <span class="arithmatex">\(0{,}60\times0{,}40=\)</span><wbr><span class="arithmatex">\(0{,}24\)</span>. <strong class="auto-resultat">Indépendants</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Dans un tableau, la condition fixe le total de référence.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Dire « parmi les <span class="arithmatex">\(A\)</span> » aide à choisir le bon dénominateur.</div>

## Série D — QCM type épreuve

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1">Si <span class="arithmatex">\(P(A)=0{,}4\)</span>, alors <span class="arithmatex">\(P(\overline A)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}4\)</span></li><li><span class="arithmatex">\(0{,}6\)</span></li><li><span class="arithmatex">\(1{,}4\)</span></li><li><span class="arithmatex">\(0{,}04\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(P(A)=0{,}5\)</span> et <span class="arithmatex">\(P_A(B)=0{,}2\)</span>, alors <span class="arithmatex">\(P(A\cap B)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}7\)</span></li><li><span class="arithmatex">\(0{,}3\)</span></li><li><span class="arithmatex">\(0{,}1\)</span></li><li><span class="arithmatex">\(2{,}5\)</span></li></ol></li>
<li value="3"><span class="arithmatex">\(P_A(B)\)</span> signifie<ol class="auto-choix" type="A"><li><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span></li><li><span class="arithmatex">\(B\)</span> sachant <span class="arithmatex">\(A\)</span></li><li><span class="arithmatex">\(A\)</span> sachant <span class="arithmatex">\(B\)</span></li><li>ni <span class="arithmatex">\(A\)</span> ni <span class="arithmatex">\(B\)</span></li></ol></li>
<li value="4">Sur un chemin d'arbre, on<ol class="auto-choix" type="A"><li>additionne</li><li>multiplie</li><li>dérive</li><li>moyenne</li></ol></li>
<li value="5">Si <span class="arithmatex">\(P(A\cap B)=P(A)P(B)\)</span>, alors <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont<ol class="auto-choix" type="A"><li>incompatibles</li><li>indépendants</li><li>contraires</li><li>égaux</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Complément : soustraire à <span class="arithmatex">\(1\)</span>.</li><li>Conditionnel vers intersection : multiplier.</li><li>Une seule réponse est correcte.</li></ul>
    <p><strong>Vigilance</strong></p><p>Indépendants ne veut pas dire incompatibles.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(1-0{,}4=0{,}6\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse C</strong> : Réponse : <span class="arithmatex">\(0{,}5\times0{,}2=0{,}1\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(B\)</span> sachant <span class="arithmatex">\(A\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : Réponse : on multiplie.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : Réponse : indépendants.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En probabilités, commencer par traduire la notation en mots.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une erreur de notation change souvent complètement le calcul.</div>

---

*Ces questions reprennent le diaporama d'automatismes N17 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
