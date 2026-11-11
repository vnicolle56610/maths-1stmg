---
title: "Automatismes Première STMG – Épreuves indépendantes de Bernoulli et arbres : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première STMG (épreuves indépendantes de Bernoulli et arbres), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N18 — Épreuves indépendantes de Bernoulli et arbres

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N18-bernoulli-arbres.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N18_EPREUVES_INDEPENDANTES_BERNOULLI_ARBRES.pdf){ .md-button }
[📖 Revoir la notion](../notions/N18-bernoulli-arbres.md){ .md-button }
</div>

## Série A — Reconnaître une épreuve de Bernoulli

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Identifier succès, échec et probabilité du succès.
</div>

<ol class="auto-questions">
<li value="1">Un client répond oui ou non à une offre. Est-ce une épreuve de Bernoulli ?</li>
<li value="2">Si la probabilité de succès est <span class="arithmatex">\(0{,}35\)</span>, quelle est la probabilité d'échec ?</li>
<li value="3">Si <span class="arithmatex">\(p=0{,}4\)</span>, calculer la probabilité de deux succès successifs indépendants.</li>
<li value="4">Si <span class="arithmatex">\(p=0{,}4\)</span>, calculer la probabilité de deux échecs successifs.</li>
<li value="5">Si <span class="arithmatex">\(p=0{,}4\)</span>, calculer la probabilité du chemin succès puis échec.</li>
<li value="6">Dans un arbre de <span class="arithmatex">\(3\)</span> épreuves, combien y a-t-il de niveaux de tirage ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Bernoulli : deux issues seulement.</li><li>Succès de probabilité <span class="arithmatex">\(p\)</span>, échec de probabilité <span class="arithmatex">\(1-p\)</span>.</li><li>Indépendance : on multiplie les probabilités.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le succès n'est pas forcément un résultat positif dans le contexte : c'est l'événement choisi.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1">Oui : deux issues, oui/non. <strong class="auto-resultat">Bernoulli</strong>.</li>
    <li value="2"><span class="arithmatex">\(1-0{,}35=\boxed{0{,}65}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(0{,}4\times0{,}4=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}16}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(0{,}6\times0{,}6=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}36}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(0{,}4\times0{,}6=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}24}\)</span>.</li>
    <li value="6">Il y a <span class="arithmatex">\(\boxed{3}\)</span> niveaux de tirage.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une répétition indépendante de Bernoulli répète la même expérience à deux issues.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Toujours écrire clairement ce qui est appelé succès.</div>

## Série B — Calculer des chemins d'arbre

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Multiplier les probabilités d'un chemin.
</div>

<ol class="auto-questions">
<li value="1">On répète <span class="arithmatex">\(3\)</span> fois une épreuve avec <span class="arithmatex">\(p=0{,}3\)</span>. Calculer <span class="arithmatex">\(P(SSS)\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(P(SSE)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(P(SES)\)</span>.</li>
<li value="4">Comparer <span class="arithmatex">\(P(SSE)\)</span> et <span class="arithmatex">\(P(SES)\)</span>.</li>
<li value="5">Combien de chemins donnent exactement deux succès en <span class="arithmatex">\(3\)</span> épreuves ?</li>
<li value="6">En déduire la probabilité d'obtenir exactement deux succès.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Un chemin se multiplie.</li><li>L'ordre change le chemin, mais pas forcément la probabilité.</li><li>Exactement deux succès : compter les positions de l'échec.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas oublier de compter tous les chemins favorables.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(SSS)=\)</span><wbr><span class="arithmatex">\(0{,}3^3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}027}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(SSE)=\)</span><wbr><span class="arithmatex">\(0{,}3\times0{,}3\times0{,}7=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}063}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(SES)=\)</span><wbr><span class="arithmatex">\(0{,}3\times0{,}7\times0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}063}\)</span>.</li>
    <li value="4">Elles sont <strong class="auto-resultat">égales</strong>.</li>
    <li value="5">Il y a <span class="arithmatex">\(\boxed{3}\)</span> chemins : <span class="arithmatex">\(SSE, SES, ESS\)</span>.</li>
    <li value="6">Donc <span class="arithmatex">\(P=\)</span><wbr><span class="arithmatex">\(3\times0{,}063=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}189}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour « exactement », compter les chemins favorables puis additionner leurs probabilités.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Les chemins <span class="arithmatex">\(SSE\)</span> et <span class="arithmatex">\(SES\)</span> sont différents, même si leurs probabilités sont égales.</div>

## Série C — Au moins un succès

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Utiliser le complémentaire quand c'est plus rapide.
</div>

<ol class="auto-questions">
<li value="1">Pour <span class="arithmatex">\(2\)</span> épreuves indépendantes avec <span class="arithmatex">\(p=0{,}4\)</span>, quelle est la probabilité d'aucun succès ?</li>
<li value="2">En déduire la probabilité d'au moins un succès.</li>
<li value="3">Pour <span class="arithmatex">\(3\)</span> épreuves avec <span class="arithmatex">\(p=0{,}5\)</span>, calculer la probabilité d'aucun succès.</li>
<li value="4">En déduire la probabilité d'au moins un succès.</li>
<li value="5">Pour <span class="arithmatex">\(4\)</span> épreuves avec <span class="arithmatex">\(p=0{,}25\)</span>, écrire la probabilité d'aucun succès sous forme de puissance.</li>
<li value="6">Que signifie « au moins un » ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Au moins un succès est le contraire de aucun succès.</li><li>Aucun succès : uniquement des échecs.</li><li>Le complémentaire se calcule avec <span class="arithmatex">\(1-\cdots\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p>« Au moins un » ne signifie pas « exactement un ».</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1">Aucun succès : <span class="arithmatex">\(0{,}6^2=\boxed{0{,}36}\)</span>.</li>
    <li value="2">Au moins un succès : <span class="arithmatex">\(1-0{,}36=\boxed{0{,}64}\)</span>.</li>
    <li value="3">Aucun succès : <span class="arithmatex">\(0{,}5^3=\boxed{0{,}125}\)</span>.</li>
    <li value="4">Au moins un succès : <span class="arithmatex">\(1-0{,}125=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}875}\)</span>.</li>
    <li value="5">Aucun succès : <span class="arithmatex">\(\boxed{0{,}75^4}\)</span>.</li>
    <li value="6">« Au moins un » signifie <strong class="auto-resultat">un ou plusieurs</strong>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour « au moins un », calculer souvent <span class="arithmatex">\(1-P(\text{aucun})\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le complémentaire de « au moins un succès » est « aucun succès ».</div>

## Série D — QCM type épreuve

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1">Une épreuve de Bernoulli a<ol class="auto-choix" type="A"><li>une seule issue</li><li>deux issues</li><li>trois issues</li><li>une infinité d'issues</li></ol></li>
<li value="2">Si <span class="arithmatex">\(p=0{,}2\)</span>, la probabilité d'échec est<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}2\)</span></li><li><span class="arithmatex">\(0{,}8\)</span></li><li><span class="arithmatex">\(1{,}2\)</span></li><li><span class="arithmatex">\(0{,}02\)</span></li></ol></li>
<li value="3">Pour deux succès indépendants de probabilité <span class="arithmatex">\(0{,}5\)</span>, la probabilité est<ol class="auto-choix" type="A"><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(0{,}25\)</span></li><li><span class="arithmatex">\(0{,}5\)</span></li><li><span class="arithmatex">\(2\)</span></li></ol></li>
<li value="4">Le contraire de « au moins un succès » est<ol class="auto-choix" type="A"><li>exactement un succès</li><li>aucun succès</li><li>deux succès</li><li>succès certain</li></ol></li>
<li value="5">Dans un arbre d'épreuves indépendantes, un chemin se calcule en<ol class="auto-choix" type="A"><li>additionnant</li><li>multipliant</li><li>dérivant</li><li>moyennant</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Associer <span class="arithmatex">\(p\)</span> au succès et <span class="arithmatex">\(1-p\)</span> à l'échec.</li><li>Le long d'un chemin : produit.</li><li>Lire chaque proposition jusqu'au bout.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le complémentaire est souvent le chemin le plus court.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : Réponse : deux issues.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(1-0{,}2=0{,}8\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(0{,}5\times0{,}5=0{,}25\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : Réponse : aucun succès.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : Réponse : en multipliant.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Avant de calculer, vérifier si les répétitions sont bien indépendantes et identiques.</div>

---

*Ces questions reprennent le diaporama d'automatismes N18 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
