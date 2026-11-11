---
title: "Automatismes Première STMG – Suites arithmétiques et géométriques : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première STMG (suites arithmétiques et géométriques), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N09 — Suites arithmétiques et géométriques

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N09-suites-arithmetiques-geometriques.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N09_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf){ .md-button }
[📖 Revoir la notion](../notions/N09-suites-arithmetiques-geometriques.md){ .md-button }
</div>

## Série A — Suites : réactiver les termes

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer des termes et reconnaître un mode de génération.
</div>

<ol class="auto-questions">
<li value="1">Une suite vérifie <span class="arithmatex">\(u(0)=5\)</span> et <span class="arithmatex">\(u(n+1)=u(n)+3\)</span>. Calculer <span class="arithmatex">\(u(1)\)</span>.</li>
<li value="2">Avec la même suite, calculer <span class="arithmatex">\(u(2)\)</span>.</li>
<li value="3">Une suite vérifie <span class="arithmatex">\(v(0)=4\)</span> et <span class="arithmatex">\(v(n+1)=2v(n)\)</span>. Calculer <span class="arithmatex">\(v(1)\)</span>.</li>
<li value="4">Avec la même suite, calculer <span class="arithmatex">\(v(2)\)</span>.</li>
<li value="5">Dans le tableau <span class="arithmatex">\(n:0;1;2;3\)</span> et <span class="arithmatex">\(w(n):7;10;13;16\)</span>, quelle est la différence constante ?</li>
<li value="6">Dans le tableau <span class="arithmatex">\(n:0;1;2;3\)</span> et <span class="arithmatex">\(z(n):3;6;12;24\)</span>, quel est le coefficient multiplicateur constant ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Lire le rang de départ : ici <span class="arithmatex">\(0\)</span>.</li><li>Appliquer la relation une étape à la fois.</li><li>Différence constante : modèle arithmétique.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre <span class="arithmatex">\(u(2)\)</span> avec le deuxième terme si le rang de départ est <span class="arithmatex">\(0\)</span>.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u(1)=5+3=\boxed{8}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u(2)=8+3=\boxed{11}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(v(1)=2\times4=\boxed{8}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(v(2)=2\times8=\boxed{16}\)</span>.</li>
    <li value="5">La différence constante est <span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="6">Le coefficient multiplicateur constant est <span class="arithmatex">\(\boxed{2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une relation de récurrence donne le terme suivant à partir du terme précédent.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le premier rang doit toujours être repéré avant de calculer.</div>

## Série B — Suite arithmétique

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Identifier et utiliser une évolution absolue constante.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u(0)=12\)</span> et la raison est <span class="arithmatex">\(5\)</span>. Calculer <span class="arithmatex">\(u(1)\)</span>.</li>
<li value="2">Avec les mêmes données, calculer <span class="arithmatex">\(u(4)\)</span> sans tout lister.</li>
<li value="3">Une suite arithmétique vérifie <span class="arithmatex">\(u(0)=80\)</span> et <span class="arithmatex">\(r=-6\)</span>. Calculer <span class="arithmatex">\(u(3)\)</span>.</li>
<li value="4">Les termes <span class="arithmatex">\(20;25;30;35\)</span> définissent-ils une suite arithmétique ?</li>
<li value="5">Compléter : si <span class="arithmatex">\(u(0)=a\)</span> et la raison est <span class="arithmatex">\(r\)</span>, alors <span class="arithmatex">\(u(n)=\ldots\)</span>.</li>
<li value="6">Un stock augmente de <span class="arithmatex">\(40\)</span> unités par semaine à partir de <span class="arithmatex">\(250\)</span>. Donner l'expression de <span class="arithmatex">\(u(n)\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Ajouter la raison à chaque rang.</li><li>Formule explicite depuis le rang <span class="arithmatex">\(0\)</span> : <span class="arithmatex">\(u(n)=u(0)+nr\)</span>.</li><li>Une baisse constante donne une raison négative.</li></ul>
    <p><strong>Vigilance</strong></p><p>Une suite arithmétique modélise une évolution en quantité, pas en pourcentage.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u(1)=12+5=\boxed{17}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u(4)=\)</span><wbr><span class="arithmatex">\(12+4\times5=\)</span><wbr><span class="arithmatex">\(\boxed{32}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(u(3)=\)</span><wbr><span class="arithmatex">\(80+3\times(-6)=\)</span><wbr><span class="arithmatex">\(\boxed{62}\)</span>.</li>
    <li value="4">Oui, différence constante <span class="arithmatex">\(5\)</span> : <span class="arithmatex">\(\boxed{\text{arithmétique}}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\boxed{u(n)=a+nr}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{u(n)=250+40n}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour une suite arithmétique de raison <span class="arithmatex">\(r\)</span>, on ajoute toujours la même quantité.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le signe de <span class="arithmatex">\(r\)</span> indique le sens de variation.</div>

## Série C — Suite géométrique

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Identifier et utiliser une évolution relative constante.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(v(0)=10\)</span> et la raison est <span class="arithmatex">\(1{,}2\)</span>. Calculer <span class="arithmatex">\(v(1)\)</span>.</li>
<li value="2">Avec les mêmes données, calculer <span class="arithmatex">\(v(2)\)</span>.</li>
<li value="3"><span class="arithmatex">\(w(0)=200\)</span> et la raison est <span class="arithmatex">\(0{,}9\)</span>. Calculer <span class="arithmatex">\(w(1)\)</span>.</li>
<li value="4">Une augmentation de <span class="arithmatex">\(8\%\)</span> correspond à quelle raison ?</li>
<li value="5">Une baisse de <span class="arithmatex">\(15\%\)</span> correspond à quelle raison ?</li>
<li value="6">Compléter : si <span class="arithmatex">\(v(0)=b\)</span> et la raison est <span class="arithmatex">\(q\)</span>, alors <span class="arithmatex">\(v(n)=\ldots\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Multiplier par la raison à chaque rang.</li><li>Une hausse de <span class="arithmatex">\(t\%\)</span> donne <span class="arithmatex">\(1+\frac{t}{100}\)</span>.</li><li>Une baisse de <span class="arithmatex">\(t\%\)</span> donne <span class="arithmatex">\(1-\frac{t}{100}\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p>La raison d'une suite géométrique n'est pas le taux en pourcentage.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(v(1)=\)</span><wbr><span class="arithmatex">\(10\times1{,}2=\)</span><wbr><span class="arithmatex">\(\boxed{12}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(v(2)=\)</span><wbr><span class="arithmatex">\(12\times1{,}2=\)</span><wbr><span class="arithmatex">\(\boxed{14{,}4}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(w(1)=\)</span><wbr><span class="arithmatex">\(200\times0{,}9=\)</span><wbr><span class="arithmatex">\(\boxed{180}\)</span>.</li>
    <li value="4">Raison <span class="arithmatex">\(\boxed{1{,}08}\)</span>.</li>
    <li value="5">Raison <span class="arithmatex">\(\boxed{0{,}85}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{v(n)=b\times q^n}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour une suite géométrique à termes positifs, on multiplie toujours par le même nombre.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Si <span class="arithmatex">\(0&lt;q&lt;1\)</span>, les termes positifs diminuent.</div>

## Série D — QCM : choisir le modèle

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Pour chaque question, choisir A, B, C ou D. Une seule réponse est correcte.
</div>

<ol class="auto-questions">
<li value="1">Suite <span class="arithmatex">\(12;18;24;30\)</span>.<ol class="auto-choix" type="A"><li>arithmétique</li><li>géométrique</li><li>les deux</li><li>aucune</li></ol></li>
<li value="2">Suite <span class="arithmatex">\(5;10;20;40\)</span>.<ol class="auto-choix" type="A"><li>arithmétique</li><li>géométrique</li><li>constante</li><li>aucune</li></ol></li>
<li value="3">Si <span class="arithmatex">\(u(n)=30+4n\)</span>, alors <span class="arithmatex">\(u(5)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(34\)</span></li><li><span class="arithmatex">\(50\)</span></li><li><span class="arithmatex">\(150\)</span></li><li><span class="arithmatex">\(20\)</span></li></ol></li>
<li value="4">Si <span class="arithmatex">\(v(n)=80\times0{,}5^n\)</span>, alors <span class="arithmatex">\(v(2)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(40\)</span></li><li><span class="arithmatex">\(20\)</span></li><li><span class="arithmatex">\(160\)</span></li><li><span class="arithmatex">\(82\)</span></li></ol></li>
<li value="5">Une baisse annuelle de <span class="arithmatex">\(12\%\)</span> donne <span class="arithmatex">\(q=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(1{,}12\)</span></li><li><span class="arithmatex">\(0{,}12\)</span></li><li><span class="arithmatex">\(0{,}88\)</span></li><li><span class="arithmatex">\(-12\)</span></li></ol></li>
<li value="6">Une suite arithmétique croissante a une raison<ol class="auto-choix" type="A"><li>nulle</li><li>positive</li><li>négative</li><li>inférieure à <span class="arithmatex">\(1\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer : ajout constant ou multiplication constante.</li><li>Dans un QCM, tester deux étapes suffit souvent.</li><li>Vérifier l'ordre de grandeur.</li></ul>
    <p><strong>Vigilance</strong></p><p>Une augmentation régulière en euros n'est pas une augmentation régulière en pourcentage.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse A</strong> : on ajoute <span class="arithmatex">\(6\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : on multiplie par <span class="arithmatex">\(2\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(30+4\times5=50\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(80\times0{,}25=20\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(1-0{,}12=0{,}88\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(r&gt;0\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Le type de suite dépend de la façon dont on passe d'un terme au suivant.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le mot « raison » désigne <span class="arithmatex">\(r\)</span> pour l'arithmétique et <span class="arithmatex">\(q\)</span> pour la géométrique.</div>

---

*Ces questions reprennent le diaporama d'automatismes N09 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
