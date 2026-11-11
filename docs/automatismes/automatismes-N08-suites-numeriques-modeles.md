---
title: "Automatismes Première STMG – Suites numériques : modèles discrets : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première STMG (suites numériques : modèles discrets), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N08 — Suites numériques : modèles discrets

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N08-suites-numeriques-modeles.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N08_SUITES_NUMERIQUES_MODELES_DISCRETS.pdf){ .md-button }
[📖 Revoir la notion](../notions/N08-suites-numeriques-modeles.md){ .md-button }
</div>

## Série A — Suites : listes de termes

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Lire et prolonger une suite donnée par ses premiers termes.
</div>

<ol class="auto-questions">
<li value="1">On a <span class="arithmatex">\(u(0)=120\)</span>, puis on ajoute <span class="arithmatex">\(15\)</span>. Calculer <span class="arithmatex">\(u(1)\)</span>.</li>
<li value="2">Avec la même suite, calculer <span class="arithmatex">\(u(2)\)</span> et <span class="arithmatex">\(u(3)\)</span>.</li>
<li value="3">La suite <span class="arithmatex">\(120;135;150;165\)</span> est-elle croissante ou décroissante ?</li>
<li value="4">Dans cette liste, quel est l'écart entre deux termes consécutifs ?</li>
<li value="5">Une suite commence par <span class="arithmatex">\(200;180;162\)</span> et on multiplie par <span class="arithmatex">\(0{,}9\)</span>. Donner le terme suivant.</li>
<li value="6">La suite <span class="arithmatex">\(200;180;162;\ldots\)</span> semble-t-elle croissante ou décroissante ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Le rang <span class="arithmatex">\(0\)</span> est souvent le départ.</li><li>Une suite se lit terme après terme.</li><li>Noter <span class="arithmatex">\(u(0)\)</span>, <span class="arithmatex">\(u(1)\)</span>, <span class="arithmatex">\(u(2)\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p>Ne pas confondre <span class="arithmatex">\(u(2)\)</span> et le deuxième terme si la suite commence au rang 0.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u(1)=120+15=\boxed{135}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u(2)=150\)</span> et <span class="arithmatex">\(u(3)=\boxed{165}\)</span>.</li>
    <li value="3">Elle est <span class="arithmatex">\(\boxed{\text{croissante}}\)</span>.</li>
    <li value="4">L'écart vaut <span class="arithmatex">\(\boxed{15}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(162\times0{,}9=\)</span><wbr><span class="arithmatex">\(\boxed{145{,}8}\)</span>.</li>
    <li value="6">Elle est <span class="arithmatex">\(\boxed{\text{décroissante}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une suite est une liste ordonnée de nombres indexés par un rang.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Si le rang initial est 0, le terme <span class="arithmatex">\(u(2)\)</span> est le troisième terme écrit.</div>

## Série B — Modes de génération

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer des termes à partir d'une relation ou d'une formule.
</div>

<ol class="auto-questions">
<li value="1">Si <span class="arithmatex">\(u(0)=50\)</span> et <span class="arithmatex">\(u(n+1)=u(n)+8\)</span>, calculer <span class="arithmatex">\(u(1)\)</span>.</li>
<li value="2">Avec la même suite, calculer <span class="arithmatex">\(u(2)\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(v(0)=100\)</span> et <span class="arithmatex">\(v(n+1)=v(n)-12\)</span>, calculer <span class="arithmatex">\(v(3)\)</span>.</li>
<li value="4">Si <span class="arithmatex">\(w(n)=5n+40\)</span>, calculer <span class="arithmatex">\(w(4)\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(q(n)=2n^2+1\)</span>, calculer <span class="arithmatex">\(q(3)\)</span>.</li>
<li value="6">Dire en français ce que signifie <span class="arithmatex">\(u(n+1)=u(n)+8\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Récurrence : pas à pas.</li><li>Formule : remplacer <span class="arithmatex">\(n\)</span>.</li><li>Garder la notation <span class="arithmatex">\(u(n)\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><p><span class="arithmatex">\(u(n+1)\)</span> désigne le terme suivant.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u(1)=50+8=\boxed{58}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u(2)=58+8=\boxed{66}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(v(1)=88\)</span>, <span class="arithmatex">\(v(2)=76\)</span>, <span class="arithmatex">\(v(3)=\boxed{64}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(w(4)=\)</span><wbr><span class="arithmatex">\(5\times4+40=\)</span><wbr><span class="arithmatex">\(\boxed{60}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(q(3)=\)</span><wbr><span class="arithmatex">\(2\times9+1=\)</span><wbr><span class="arithmatex">\(\boxed{19}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{\text{On ajoute 8 au terme précédent.}}\)</span></li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Choisir la bonne lecture : récurrence = pas à pas ; formule = calcul direct.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le rang <span class="arithmatex">\(n\)</span> est un entier : il ne décrit pas un temps continu.</div>

## Série C — Modèles discrets en contexte

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Identifier une suite et interpréter un terme dans une situation STMG.
</div>

<ol class="auto-questions">
<li value="1">Un stock vaut <span class="arithmatex">\(500\)</span> unités au départ et augmente de <span class="arithmatex">\(30\)</span> par semaine. Calculer le stock après <span class="arithmatex">\(2\)</span> semaines.</li>
<li value="2">Un abonnement coûte <span class="arithmatex">\(10+4n\)</span> euros au rang <span class="arithmatex">\(n\)</span>. Calculer le coût pour <span class="arithmatex">\(n=6\)</span>.</li>
<li value="3">Un nombre de clients est relevé chaque mois. Est-ce un modèle discret ?</li>
<li value="4">Une température connue à tout instant est-elle naturellement modélisée par une suite ?</li>
<li value="5">On lit les points <span class="arithmatex">\((0;40)\)</span>, <span class="arithmatex">\((1;52)\)</span>, <span class="arithmatex">\((2;61)\)</span>. Donner <span class="arithmatex">\(u(2)\)</span>.</li>
<li value="6">Faut-il relier les points <span class="arithmatex">\((n;u(n))\)</span> par une courbe continue ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Discret : rangs entiers.</li><li>Point : <span class="arithmatex">\((n;u(n))\)</span>.</li><li>Interpréter le rang.</li></ul>
    <p><strong>Vigilance</strong></p><p>Une suite n'est pas une fonction tracée en continu.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(500+2\times30=\)</span><wbr><span class="arithmatex">\(\boxed{560}\)</span> unités.</li>
    <li value="2"><span class="arithmatex">\(10+4\times6=\boxed{34}\)</span> euros.</li>
    <li value="3">Oui : <span class="arithmatex">\(\boxed{\text{modèle discret}}\)</span>, car les mois sont des rangs séparés.</li>
    <li value="4">Non : c'est plutôt un modèle <span class="arithmatex">\(\boxed{\text{continu}}\)</span>.</li>
    <li value="5">Le point <span class="arithmatex">\((2;61)\)</span> donne <span class="arithmatex">\(\boxed{u(2)=61}\)</span>.</li>
    <li value="6">Non : on représente par un <span class="arithmatex">\(\boxed{\text{nuage de points}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une suite modélise une évolution rang par rang : jours, semaines, mois, années.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas relier automatiquement les points d'une suite.</div>

## Série D — QCM - suites et modèles discrets

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1">Si <span class="arithmatex">\(u(0)=7\)</span> et <span class="arithmatex">\(u(n+1)=u(n)+3\)</span>, alors <span class="arithmatex">\(u(2)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(10\)</span></li><li><span class="arithmatex">\(13\)</span></li><li><span class="arithmatex">\(14\)</span></li><li><span class="arithmatex">\(21\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(v(n)=4n+1\)</span>, alors <span class="arithmatex">\(v(5)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(9\)</span></li><li><span class="arithmatex">\(20\)</span></li><li><span class="arithmatex">\(21\)</span></li><li><span class="arithmatex">\(45\)</span></li></ol></li>
<li value="3">Le point <span class="arithmatex">\((3;80)\)</span> signifie :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(u(80)=3\)</span></li><li><span class="arithmatex">\(u(3)=80\)</span></li><li><span class="arithmatex">\(u(0)=83\)</span></li><li><span class="arithmatex">\(3u=80\)</span></li></ol></li>
<li value="4">Une suite est adaptée pour modéliser :<ol class="auto-choix" type="A"><li>une hauteur à tout instant</li><li>un stock chaque fin de mois</li><li>une courbe continue</li><li>une équation</li></ol></li>
<li value="5">Si les termes <span class="arithmatex">\(10;8;6;4\)</span> sont lus dans l'ordre, la suite est :<ol class="auto-choix" type="A"><li>croissante</li><li>décroissante</li><li>constante</li><li>positive donc croissante</li></ol></li>
<li value="6">Avec <span class="arithmatex">\(u(0)=100\)</span> et <span class="arithmatex">\(u(n+1)=0{,}8u(n)\)</span>, <span class="arithmatex">\(u(1)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(20\)</span></li><li><span class="arithmatex">\(80\)</span></li><li><span class="arithmatex">\(100{,}8\)</span></li><li><span class="arithmatex">\(125\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Faire attention au rang de départ.</li><li>Pour une formule, remplacer <span class="arithmatex">\(n\)</span>.</li><li>Une seule réponse est correcte.</li></ul>
    <p><strong>Vigilance</strong></p><p>Positif ne signifie pas croissant.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(u(1)=10\)</span>, puis <span class="arithmatex">\(u(2)=13\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse C</strong> : Réponse : <span class="arithmatex">\(4\times5+1=21\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(u(3)=80\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : Réponse : un stock relevé chaque fin de mois.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : Réponse : les valeurs diminuent.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : Réponse : <span class="arithmatex">\(100\times0{,}8=80\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En QCM, identifier d'abord si la suite est donnée par liste, récurrence ou formule explicite.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Vérifier le rang initial avant de cocher.</div>

---

*Ces questions reprennent le diaporama d'automatismes N08 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
