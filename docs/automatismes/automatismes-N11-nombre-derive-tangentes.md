---
title: "Automatismes Première STMG – Nombre dérivé : sécantes, tangentes, interprétation : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première STMG (nombre dérivé : sécantes, tangentes, interprétation), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N11 — Nombre dérivé : sécantes, tangentes, interprétation

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N11-nombre-derive-tangentes.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N11_NOMBRE_DERIVE_SECANTES_TANGENTES_INTERPRETATION.pdf){ .md-button }
[📖 Revoir la notion](../notions/N11-nombre-derive-tangentes.md){ .md-button }
</div>

## Série A — Pente de sécante

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer une pente entre deux points.
</div>

<ol class="auto-questions">
<li value="1">Calculer la pente entre <span class="arithmatex">\(A(1;4)\)</span> et <span class="arithmatex">\(B(3;10)\)</span>.</li>
<li value="2">Calculer la pente entre <span class="arithmatex">\(A(0;8)\)</span> et <span class="arithmatex">\(B(4;0)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(\dfrac{f(5)-f(2)}{5-2}\)</span> si <span class="arithmatex">\(f(2)=7\)</span> et <span class="arithmatex">\(f(5)=16\)</span>.</li>
<li value="4">Un coût passe de <span class="arithmatex">\(120\)</span> à <span class="arithmatex">\(180\)</span> euros quand la quantité passe de <span class="arithmatex">\(2\)</span> à <span class="arithmatex">\(5\)</span>. Variation moyenne ?</li>
<li value="5">Entre <span class="arithmatex">\(x=1\)</span> et <span class="arithmatex">\(x=4\)</span>, une fonction passe de <span class="arithmatex">\(9\)</span> à <span class="arithmatex">\(9\)</span>. Pente de la sécante ?</li>
<li value="6">Une pente positive indique une variation moyenne <span class="arithmatex">\(\ldots\)</span></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Pente : différence des ordonnées divisée par différence des abscisses.</li><li>Commencer par <span class="arithmatex">\(y_B-y_A\)</span>.</li><li>Garder l'unité si le contexte en a une.</li></ul>
    <p><strong>Vigilance</strong></p><p>La pente d'une sécante est une variation moyenne, pas encore une variation instantanée.</p>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\dfrac{10-4}{3-1}=\)</span><wbr><span class="arithmatex">\(\dfrac{6}{2}=\)</span><wbr><span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\dfrac{0-8}{4-0}=\)</span><wbr><span class="arithmatex">\(\boxed{-2}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\dfrac{16-7}{3}=\)</span><wbr><span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\dfrac{180-120}{5-2}=\)</span><wbr><span class="arithmatex">\(\boxed{20}\)</span> euros par unité.</li>
    <li value="5"><span class="arithmatex">\(\dfrac{9-9}{4-1}=\)</span><wbr><span class="arithmatex">\(\boxed{0}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{\text{positive / croissante en moyenne}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une sécante coupe la courbe en deux points : sa pente résume une variation moyenne.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Surveiller l'ordre des soustractions dans le numérateur et le dénominateur.</div>

## Série B — Tangente et nombre dérivé

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Lire ou utiliser une pente de tangente.
</div>

<ol class="auto-questions">
<li value="1">La tangente en <span class="arithmatex">\(x=2\)</span> a pour pente <span class="arithmatex">\(5\)</span>. Donner <span class="arithmatex">\(f'(2)\)</span>.</li>
<li value="2">La tangente en <span class="arithmatex">\(x=0\)</span> est horizontale. Donner <span class="arithmatex">\(f'(0)\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(f'(3)=-4\)</span>, la tangente en <span class="arithmatex">\(x=3\)</span> monte-t-elle ou descend-elle ?</li>
<li value="4">Si <span class="arithmatex">\(f'(1)=0\)</span>, que peut-on dire de la tangente en <span class="arithmatex">\(x=1\)</span> ?</li>
<li value="5">Compléter : <span class="arithmatex">\(f'(a)\)</span> est le coefficient directeur de la <span class="arithmatex">\(\ldots\)</span> à la courbe au point d'abscisse <span class="arithmatex">\(a\)</span>.</li>
<li value="6">Si une tangente passe par <span class="arithmatex">\((2;6)\)</span> et a pour pente <span class="arithmatex">\(3\)</span>, de combien monte-t-elle quand <span class="arithmatex">\(x\)</span> augmente de <span class="arithmatex">\(1\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Le nombre dérivé est une pente locale.</li><li>Tangente horizontale : pente nulle.</li><li>Signe de la pente : sens local.</li></ul>
    <p><strong>Vigilance</strong></p><p>On ne formule pas ici de définition formelle avec une limite.</p>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\boxed{f'(2)=5}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\boxed{f'(0)=0}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\boxed{\text{elle descend}}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\boxed{\text{elle est horizontale}}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\boxed{\text{tangente}}\)</span>.</li>
    <li value="6">Elle monte de <span class="arithmatex">\(\boxed{3}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Le nombre dérivé <span class="arithmatex">\(f'(a)\)</span> se lit comme la pente de la tangente au point d'abscisse <span class="arithmatex">\(a\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une pente nulle ne signifie pas que la fonction est nulle.</div>

## Série C — Interpréter en contexte

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Associer un nombre dérivé à une variation instantanée.
</div>

<ol class="auto-questions">
<li value="1">Un coût <span class="arithmatex">\(C(q)\)</span> est en euros et <span class="arithmatex">\(q\)</span> en objets. Que signifie <span class="arithmatex">\(C'(10)=4\)</span> ?</li>
<li value="2">Une distance <span class="arithmatex">\(d(t)\)</span> est en km et <span class="arithmatex">\(t\)</span> en h. Que représente <span class="arithmatex">\(d'(2)\)</span> ?</li>
<li value="3">Si <span class="arithmatex">\(C'(20)&lt;0\)</span>, le coût augmente-t-il ou diminue-t-il localement ?</li>
<li value="4">Si une recette <span class="arithmatex">\(R\)</span> vérifie <span class="arithmatex">\(R'(50)=0\)</span>, que vaut la pente de la tangente ?</li>
<li value="5">Un indicateur passe localement de <span class="arithmatex">\(35\)</span> à <span class="arithmatex">\(39\)</span> pour <span class="arithmatex">\(1\)</span> unité de temps. Pente locale approximative ?</li>
<li value="6">Une pente de tangente égale à <span class="arithmatex">\(-2\)</span> signifie : pour <span class="arithmatex">\(+1\)</span> en abscisse, l'ordonnée varie d'environ <span class="arithmatex">\(\ldots\)</span></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Lire les unités : ordonnée par unité d'abscisse.</li><li>Le signe donne le sens local.</li><li>Le nombre dérivé sert à interpréter une tendance immédiate.</li></ul>
    <p><strong>Vigilance</strong></p><p>Une variation instantanée est locale : elle ne décrit pas toute la courbe.</p>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1">À <span class="arithmatex">\(10\)</span> objets, le coût augmente localement d'environ <span class="arithmatex">\(\boxed{4}\)</span> euros par objet.</li>
    <li value="2">La <span class="arithmatex">\(\boxed{\text{vitesse instantanée}}\)</span> à <span class="arithmatex">\(t=2\)</span>, en km/h.</li>
    <li value="3">Il <span class="arithmatex">\(\boxed{\text{diminue localement}}\)</span>.</li>
    <li value="4">La pente vaut <span class="arithmatex">\(\boxed{0}\)</span>.</li>
    <li value="5">Pente approximative <span class="arithmatex">\(\boxed{4}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{-2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Interpréter <span class="arithmatex">\(f'(a)\)</span>, c'est donner un sens à une pente au voisinage de <span class="arithmatex">\(a\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas oublier l'unité : euros par objet, km/h, points par mois, etc.</div>

## Série D — QCM : lecture rapide

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la bonne réponse.
</div>

<ol class="auto-questions">
<li value="1">La pente entre <span class="arithmatex">\((1;2)\)</span> et <span class="arithmatex">\((4;11)\)</span> vaut<ol class="auto-choix" type="A"><li><span class="arithmatex">\(3\)</span></li><li><span class="arithmatex">\(9\)</span></li><li><span class="arithmatex">\(\frac13\)</span></li><li><span class="arithmatex">\(13\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(f'(5)=7\)</span>, alors la tangente en <span class="arithmatex">\(x=5\)</span> a pour pente<ol class="auto-choix" type="A"><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(7\)</span></li><li><span class="arithmatex">\(12\)</span></li><li><span class="arithmatex">\(0\)</span></li></ol></li>
<li value="3">Une tangente horizontale a pour coefficient directeur<ol class="auto-choix" type="A"><li><span class="arithmatex">\(-1\)</span></li><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(1\)</span></li><li>impossible</li></ol></li>
<li value="4">Si <span class="arithmatex">\(f'(a)&lt;0\)</span>, la courbe est localement<ol class="auto-choix" type="A"><li>montante</li><li>descendante</li><li>horizontale</li><li>constante partout</li></ol></li>
<li value="5">Un coût marginal se lit comme<ol class="auto-choix" type="A"><li>une pente locale</li><li>une ordonnée</li><li>un pourcentage</li><li>une aire</li></ol></li>
<li value="6">La pente entre deux points est associée à<ol class="auto-choix" type="A"><li>une tangente</li><li>une sécante</li><li>un sommet</li><li>une probabilité</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Pente de sécante : deux points.</li><li>Pente de tangente : un point et une direction locale.</li><li>Relier le signe à l'allure graphique.</li></ul>
    <p><strong>Vigilance</strong></p><p>Le nombre dérivé n'est pas une image : <span class="arithmatex">\(f'(a)\neq f(a)\)</span> en général.</p>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(\frac{11-2}{4-1}=3\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(7\)</span></li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(0\)</span></li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : descendante</li>
    <li value="5"><strong class="auto-resultat">Réponse A</strong> : une pente locale</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : une sécante</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Le vocabulaire graphique est essentiel : sécante, tangente, pente.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas confondre position du point et pente de la droite.</div>

---

*Ces questions reprennent le diaporama d'automatismes N11 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
