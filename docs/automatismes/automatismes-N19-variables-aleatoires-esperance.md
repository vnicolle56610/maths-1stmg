---
title: "Automatismes Première STMG – Variables aléatoires, espérance et simulation : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première STMG (variables aléatoires, espérance et simulation), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N19 — Variables aléatoires, espérance et simulation

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N19-variables-aleatoires-esperance.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N19_VARIABLES_ALEATOIRES_ESPERANCE_SIMULATION.pdf){ .md-button }
[📖 Revoir la notion](../notions/N19-variables-aleatoires-esperance.md){ .md-button }
</div>

## Série A — N19 - Variables aléatoires, espérance et simulation

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Compléter une loi de probabilité et calculer une espérance simple.
</div>

<ol class="auto-questions">
<li value="1">Une variable <span class="arithmatex">\(X\)</span> prend les valeurs <span class="arithmatex">\(0\)</span> ; <span class="arithmatex">\(10\)</span> ; <span class="arithmatex">\(20\)</span> avec probabilités <span class="arithmatex">\(0{,}2\)</span> ; <span class="arithmatex">\(0{,}5\)</span> ; <span class="arithmatex">\(0{,}3\)</span>. Vérifier que c'est une loi.</li>
<li value="2">Calculer <span class="arithmatex">\(P(X\geqslant 10)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(P(X=0)\)</span>.</li>
<li value="4">Calculer l'espérance <span class="arithmatex">\(E(X)\)</span>.</li>
<li value="5">Un jeu coûte <span class="arithmatex">\(8\)</span> euros et le gain moyen brut vaut <span class="arithmatex">\(11\)</span> euros. Quel est le gain moyen net ?</li>
<li value="6">Dire en une phrase ce que signifie <span class="arithmatex">\(E(X)=11\)</span> dans ce contexte.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une loi a des probabilités positives.</li><li>La somme des probabilités vaut <span class="arithmatex">\(1\)</span>.</li><li>Espérance : moyenne attendue sur beaucoup d'essais.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre la valeur prise par <span class="arithmatex">\(X\)</span> et sa probabilité.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(0{,}2+0{,}5+0{,}3=1\)</span>, donc c'est une loi : <strong class="auto-resultat">oui</strong>.</li>
    <li value="2"><span class="arithmatex">\(P(X\geqslant 10)=\)</span><wbr><span class="arithmatex">\(0{,}5+0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}8}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(X=0)=\boxed{0{,}2}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(E(X)=\)</span><wbr><span class="arithmatex">\(0\times0{,}2+10\times0{,}5+20\times0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{11}\)</span>.</li>
    <li value="5">Gain net moyen : <span class="arithmatex">\(11-8=\boxed{3}\)</span> euros.</li>
    <li value="6">Sur un grand nombre de jeux, le gain brut moyen est d'environ <strong class="auto-resultat">11 euros par jeu</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'espérance n'est pas forcément une valeur réellement obtenue à chaque essai.</div>

## Série B — N19 - Variables aléatoires, espérance et simulation

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Reconnaître une loi de Bernoulli et lire son paramètre.
</div>

<ol class="auto-questions">
<li value="1">Un client achète ou n'achète pas un produit. Peut-on modéliser par une Bernoulli ?</li>
<li value="2">Si <span class="arithmatex">\(p=0{,}7\)</span>, donner <span class="arithmatex">\(P(X=1)\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(p=0{,}7\)</span>, donner <span class="arithmatex">\(P(X=0)\)</span>.</li>
<li value="4">Pour une Bernoulli de paramètre <span class="arithmatex">\(p\)</span>, donner <span class="arithmatex">\(E(X)\)</span>.</li>
<li value="5">Dans <span class="arithmatex">\(X=1\)</span> si succès, <span class="arithmatex">\(X=0\)</span> sinon, que représente <span class="arithmatex">\(1-X\)</span> ?</li>
<li value="6">Sur <span class="arithmatex">\(100\)</span> essais avec <span class="arithmatex">\(p=0{,}7\)</span>, combien de succès attend-on en moyenne ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Bernoulli : deux issues, succès ou échec.</li><li>On code souvent succès par <span class="arithmatex">\(1\)</span>, échec par <span class="arithmatex">\(0\)</span>.</li><li>L'espérance d'une Bernoulli est son paramètre.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le mot succès désigne l'événement étudié, pas forcément une réussite commerciale.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1">Oui : deux issues possibles, donc <strong class="auto-resultat">modèle de Bernoulli possible</strong>.</li>
    <li value="2"><span class="arithmatex">\(P(X=1)=p=\boxed{0{,}7}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(X=0)=1-p=\boxed{0{,}3}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(E(X)=\boxed{p}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(1-X\)</span> vaut <span class="arithmatex">\(1\)</span> en cas d'échec : il code <strong class="auto-resultat">l'échec</strong>.</li>
    <li value="6"><span class="arithmatex">\(100\times0{,}7=\)</span><wbr><span class="arithmatex">\(\boxed{70}\)</span> succès en moyenne.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une Bernoulli se lit avec <span class="arithmatex">\(X=1\)</span> ou <span class="arithmatex">\(X=0\)</span>. Sur <span class="arithmatex">\(n\)</span> essais, le nombre moyen de succès vaut <span class="arithmatex">\(np\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas écrire <span class="arithmatex">\(P(X=0)=p\)</span> : c'est <span class="arithmatex">\(1-p\)</span>.</div>

## Série C — N19 - Variables aléatoires, espérance et simulation

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Lire une simulation et interpréter une fréquence observée.
</div>

<ol class="auto-questions">
<li value="1">Une simulation de <span class="arithmatex">\(200\)</span> clients donne <span class="arithmatex">\(118\)</span> achats. Calculer la fréquence observée.</li>
<li value="2">Comparer cette fréquence à <span class="arithmatex">\(p=0{,}6\)</span>.</li>
<li value="3">La fréquence <span class="arithmatex">\(0{,}59\)</span> appartient-elle à l'intervalle <span class="arithmatex">\([0{,}55;0{,}65]\)</span> ?</li>
<li value="4">Dans un programme, que signifie l'instruction : <span class="arithmatex">\(\texttt{alea()&lt;0.6}\)</span> ?</li>
<li value="5">Un succès rapporte <span class="arithmatex">\(4\)</span> euros et un échec coûte <span class="arithmatex">\(1\)</span> euro. Avec <span class="arithmatex">\(p=0{,}6\)</span>, calculer le gain moyen.</li>
<li value="6">Dire pourquoi deux simulations de même taille ne donnent pas toujours la même fréquence.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Fréquence observée : effectif / total.</li><li>Une simulation donne une valeur observée, pas une certitude.</li><li>Pour une moyenne de gains, pondérer par les probabilités.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas conclure qu'un modèle est faux dès qu'une fréquence n'est pas exactement égale à <span class="arithmatex">\(p\)</span>.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\dfrac{118}{200}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}59}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(0{,}59\)</span> est proche de <span class="arithmatex">\(0{,}6\)</span> : écart <span class="arithmatex">\(\boxed{0{,}01}\)</span>.</li>
    <li value="3">Oui, <span class="arithmatex">\(0{,}55\leqslant0{,}59\leqslant0{,}65\)</span> : <strong class="auto-resultat">oui</strong>.</li>
    <li value="4">L'instruction teste si le tirage aléatoire est inférieur à <span class="arithmatex">\(0{,}6\)</span> : succès avec probabilité <span class="arithmatex">\(\boxed{0{,}6}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(4\times0{,}6+(-1)\times0{,}4=\)</span><wbr><span class="arithmatex">\(2{,}4-0{,}4=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span> euros.</li>
    <li value="6">À cause de la <strong class="auto-resultat">fluctuation d'échantillonnage</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une simulation ne remplace pas le calcul de probabilité, elle l'illustre.</div>

## Série D — N19 - Variables aléatoires, espérance et simulation

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** QCM type épreuve anticipée : une seule réponse correcte, aucune justification.
</div>

<ol class="auto-questions">
<li value="1">Une loi donne <span class="arithmatex">\(P(X=1)=0{,}25\)</span>, <span class="arithmatex">\(P(X=2)=0{,}45\)</span>. Alors <span class="arithmatex">\(P(X=3)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}20\)</span></li><li><span class="arithmatex">\(0{,}30\)</span></li><li><span class="arithmatex">\(0{,}70\)</span></li><li><span class="arithmatex">\(1\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(X\)</span> suit une Bernoulli de paramètre <span class="arithmatex">\(0{,}4\)</span>, alors <span class="arithmatex">\(E(X)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}6\)</span></li><li><span class="arithmatex">\(0{,}4\)</span></li><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(4\)</span></li></ol></li>
<li value="3">Pour <span class="arithmatex">\(X\)</span> : <span class="arithmatex">\(0;5;10\)</span> avec probabilités <span class="arithmatex">\(0{,}2;0{,}6;0{,}2\)</span>, <span class="arithmatex">\(E(X)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(10\)</span></li></ol></li>
<li value="4">Dans <span class="arithmatex">\(50\)</span> essais, <span class="arithmatex">\(31\)</span> succès donnent la fréquence<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}31\)</span></li><li><span class="arithmatex">\(0{,}50\)</span></li><li><span class="arithmatex">\(0{,}62\)</span></li><li><span class="arithmatex">\(31\)</span></li></ol></li>
<li value="5">La loi de Bernoulli modélise une expérience à<ol class="auto-choix" type="A"><li><span class="arithmatex">\(1\)</span> issue</li><li><span class="arithmatex">\(2\)</span> issues</li><li><span class="arithmatex">\(3\)</span> issues</li><li><span class="arithmatex">\(n\)</span> issues</li></ol></li>
<li value="6">Si un gain net moyen vaut <span class="arithmatex">\(-0{,}50\)</span> euro, le jeu est en moyenne<ol class="auto-choix" type="A"><li>favorable</li><li>neutre</li><li>défavorable</li><li>impossible</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer d'abord la nature de la question.</li><li>Pour une loi, la somme des probabilités vaut <span class="arithmatex">\(1\)</span>.</li><li>Pour une espérance, faire une moyenne pondérée.</li></ul>
    <p><strong>Vigilance</strong></p><p>Dans un QCM, éliminer les réponses incompatibles avec un ordre de grandeur.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(1-0{,}25-0{,}45=0{,}30\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : pour une Bernoulli, <span class="arithmatex">\(E(X)=p\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(0\times0{,}2+5\times0{,}6+10\times0{,}2=\)</span><wbr><span class="arithmatex">\(5\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(\dfrac{31}{50}=0{,}62\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : succès ou échec.</li>
    <li value="6"><strong class="auto-resultat">Réponse C</strong> : une espérance négative est défavorable au joueur.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Vérifier que la réponse choisie a la bonne nature : probabilité, valeur, fréquence ou phrase.</div>

---

*Ces questions reprennent le diaporama d'automatismes N19 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
