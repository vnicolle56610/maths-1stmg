---
title: "QCM automatismes Première STMG – Variables aléatoires, espérance et simulation (interactif, corrigé)"
description: "QCM en ligne d'automatismes de Première STMG (variables aléatoires, espérance et simulation) : chronomètre, score immédiat et correction détaillée, sans calculatrice."
---

# QCM interactif — Variables aléatoires, espérance et simulation

Entraînement **sans calculatrice**. Rien n'est enregistré ni envoyé : tout se passe dans le navigateur.

[← Énoncés et corrigés à lire](automatismes-N19-variables-aleatoires-esperance.md)

<div class="auto-qcm" data-banque="banque-automatismes"></div>

<script type="application/json" id="banque-automatismes">
{
 "notion": "N19",
 "cle": "N19",
 "titre": "Variables aléatoires, espérance et simulation",
 "niveau": "Première STMG",
 "series": [
  {
   "lettre": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "duree": "6 min",
   "consigne": "Compléter une loi de probabilité et calculer une espérance simple.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "duree": "6 min",
   "consigne": "Reconnaître une loi de Bernoulli et lire son paramètre.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "duree": "7 min",
   "consigne": "Lire une simulation et interpréter une fréquence observée.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "duree": "6 min",
   "consigne": "QCM type épreuve anticipée : une seule réponse correcte, aucune justification.",
   "qcm": true,
   "figure": ""
  }
 ],
 "questions": [
  {
   "id": "N19-A1",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Une variable <span class=\"arithmatex\">\\(X\\)<\/span> prend les valeurs <span class=\"arithmatex\">\\(0\\)<\/span> ; <span class=\"arithmatex\">\\(10\\)<\/span> ; <span class=\"arithmatex\">\\(20\\)<\/span> avec probabilités <span class=\"arithmatex\">\\(0{,}2\\)<\/span> ; <span class=\"arithmatex\">\\(0{,}5\\)<\/span> ; <span class=\"arithmatex\">\\(0{,}3\\)<\/span>. Vérifier que c'est une loi.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(0{,}2+0{,}5+0{,}3=1\\)<\/span>, donc c'est une loi : <strong class=\"auto-resultat\">oui<\/strong>.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-A2",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(X\\geqslant 10)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(X\\geqslant 10)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}5+0{,}3=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}8}\\)<\/span>.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-A3",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(X=0)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(X=0)=\\boxed{0{,}2}\\)<\/span>.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-A4",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Calculer l'espérance <span class=\"arithmatex\">\\(E(X)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(E(X)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0\\times0{,}2+10\\times0{,}5+20\\times0{,}3=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{11}\\)<\/span>.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-A5",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Un jeu coûte <span class=\"arithmatex\">\\(8\\)<\/span> euros et le gain moyen brut vaut <span class=\"arithmatex\">\\(11\\)<\/span> euros. Quel est le gain moyen net ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Gain net moyen : <span class=\"arithmatex\">\\(11-8=\\boxed{3}\\)<\/span> euros.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-A6",
   "serie": "A",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Dire en une phrase ce que signifie <span class=\"arithmatex\">\\(E(X)=11\\)<\/span> dans ce contexte.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Sur un grand nombre de jeux, le gain brut moyen est d'environ <strong class=\"auto-resultat\">11 euros par jeu<\/strong>.",
   "methode": "On calcule une moyenne pondérée. Chaque valeur est multipliée par sa probabilité."
  },
  {
   "id": "N19-B1",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Un client achète ou n'achète pas un produit. Peut-on modéliser par une Bernoulli ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Oui : deux issues possibles, donc <strong class=\"auto-resultat\">modèle de Bernoulli possible<\/strong>.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-B2",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}7\\)<\/span>, donner <span class=\"arithmatex\">\\(P(X=1)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(X=1)=p=\\boxed{0{,}7}\\)<\/span>.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-B3",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}7\\)<\/span>, donner <span class=\"arithmatex\">\\(P(X=0)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(X=0)=1-p=\\boxed{0{,}3}\\)<\/span>.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-B4",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Pour une Bernoulli de paramètre <span class=\"arithmatex\">\\(p\\)<\/span>, donner <span class=\"arithmatex\">\\(E(X)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(E(X)=\\boxed{p}\\)<\/span>.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-B5",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Dans <span class=\"arithmatex\">\\(X=1\\)<\/span> si succès, <span class=\"arithmatex\">\\(X=0\\)<\/span> sinon, que représente <span class=\"arithmatex\">\\(1-X\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(1-X\\)<\/span> vaut <span class=\"arithmatex\">\\(1\\)<\/span> en cas d'échec : il code <strong class=\"auto-resultat\">l'échec<\/strong>.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-B6",
   "serie": "B",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Sur <span class=\"arithmatex\">\\(100\\)<\/span> essais avec <span class=\"arithmatex\">\\(p=0{,}7\\)<\/span>, combien de succès attend-on en moyenne ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(100\\times0{,}7=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{70}\\)<\/span> succès en moyenne.",
   "methode": "Une Bernoulli se lit avec <span class=\"arithmatex\">\\(X=1\\)<\/span> ou <span class=\"arithmatex\">\\(X=0\\)<\/span>. Sur <span class=\"arithmatex\">\\(n\\)<\/span> essais, le nombre moyen de succès vaut <span class=\"arithmatex\">\\(np\\)<\/span>."
  },
  {
   "id": "N19-C1",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Une simulation de <span class=\"arithmatex\">\\(200\\)<\/span> clients donne <span class=\"arithmatex\">\\(118\\)<\/span> achats. Calculer la fréquence observée.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\dfrac{118}{200}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}59}\\)<\/span>.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-C2",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Comparer cette fréquence à <span class=\"arithmatex\">\\(p=0{,}6\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(0{,}59\\)<\/span> est proche de <span class=\"arithmatex\">\\(0{,}6\\)<\/span> : écart <span class=\"arithmatex\">\\(\\boxed{0{,}01}\\)<\/span>.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-C3",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "La fréquence <span class=\"arithmatex\">\\(0{,}59\\)<\/span> appartient-elle à l'intervalle <span class=\"arithmatex\">\\([0{,}55;0{,}65]\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Oui, <span class=\"arithmatex\">\\(0{,}55\\leqslant0{,}59\\leqslant0{,}65\\)<\/span> : <strong class=\"auto-resultat\">oui<\/strong>.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-C4",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Dans un programme, que signifie l'instruction : <span class=\"arithmatex\">\\(\\texttt{alea()&lt;0.6}\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "L'instruction teste si le tirage aléatoire est inférieur à <span class=\"arithmatex\">\\(0{,}6\\)<\/span> : succès avec probabilité <span class=\"arithmatex\">\\(\\boxed{0{,}6}\\)<\/span>.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-C5",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Un succès rapporte <span class=\"arithmatex\">\\(4\\)<\/span> euros et un échec coûte <span class=\"arithmatex\">\\(1\\)<\/span> euro. Avec <span class=\"arithmatex\">\\(p=0{,}6\\)<\/span>, calculer le gain moyen.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(4\\times0{,}6+(-1)\\times0{,}4=\\)<\/span><wbr><span class=\"arithmatex\">\\(2{,}4-0{,}4=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{2}\\)<\/span> euros.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-C6",
   "serie": "C",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "flash",
   "enonce": "Dire pourquoi deux simulations de même taille ne donnent pas toujours la même fréquence.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "À cause de la <strong class=\"auto-resultat\">fluctuation d'échantillonnage<\/strong>.",
   "methode": "La fréquence observée varie d'une simulation à l'autre. L'espérance décrit un comportement moyen."
  },
  {
   "id": "N19-D1",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "Une loi donne <span class=\"arithmatex\">\\(P(X=1)=0{,}25\\)<\/span>, <span class=\"arithmatex\">\\(P(X=2)=0{,}45\\)<\/span>. Alors <span class=\"arithmatex\">\\(P(X=3)=\\)<\/span>",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}20\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}30\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}70\\)<\/span>",
    "<span class=\"arithmatex\">\\(1\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(1-0{,}25-0{,}45=0{,}30\\)<\/span>.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  },
  {
   "id": "N19-D2",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(X\\)<\/span> suit une Bernoulli de paramètre <span class=\"arithmatex\">\\(0{,}4\\)<\/span>, alors <span class=\"arithmatex\">\\(E(X)=\\)<\/span>",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}6\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}4\\)<\/span>",
    "<span class=\"arithmatex\">\\(1\\)<\/span>",
    "<span class=\"arithmatex\">\\(4\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "pour une Bernoulli, <span class=\"arithmatex\">\\(E(X)=p\\)<\/span>.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  },
  {
   "id": "N19-D3",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "Pour <span class=\"arithmatex\">\\(X\\)<\/span> : <span class=\"arithmatex\">\\(0;5;10\\)<\/span> avec probabilités <span class=\"arithmatex\">\\(0{,}2;0{,}6;0{,}2\\)<\/span>, <span class=\"arithmatex\">\\(E(X)=\\)<\/span>",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(4\\)<\/span>",
    "<span class=\"arithmatex\">\\(5\\)<\/span>",
    "<span class=\"arithmatex\">\\(6\\)<\/span>",
    "<span class=\"arithmatex\">\\(10\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(0\\times0{,}2+5\\times0{,}6+10\\times0{,}2=\\)<\/span><wbr><span class=\"arithmatex\">\\(5\\)<\/span>.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  },
  {
   "id": "N19-D4",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "Dans <span class=\"arithmatex\">\\(50\\)<\/span> essais, <span class=\"arithmatex\">\\(31\\)<\/span> succès donnent la fréquence",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}31\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}50\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}62\\)<\/span>",
    "<span class=\"arithmatex\">\\(31\\)<\/span>"
   ],
   "bonne": 2,
   "corrige": "<span class=\"arithmatex\">\\(\\dfrac{31}{50}=0{,}62\\)<\/span>.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  },
  {
   "id": "N19-D5",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "La loi de Bernoulli modélise une expérience à",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(1\\)<\/span> issue",
    "<span class=\"arithmatex\">\\(2\\)<\/span> issues",
    "<span class=\"arithmatex\">\\(3\\)<\/span> issues",
    "<span class=\"arithmatex\">\\(n\\)<\/span> issues"
   ],
   "bonne": 1,
   "corrige": "succès ou échec.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  },
  {
   "id": "N19-D6",
   "serie": "D",
   "theme": "N19 - Variables aléatoires, espérance et simulation",
   "type": "qcm",
   "enonce": "Si un gain net moyen vaut <span class=\"arithmatex\">\\(-0{,}50\\)<\/span> euro, le jeu est en moyenne",
   "contexte": [],
   "choix": [
    "favorable",
    "neutre",
    "défavorable",
    "impossible"
   ],
   "bonne": 2,
   "corrige": "une espérance négative est défavorable au joueur.",
   "methode": "QCM : aucun point n'est gagné par une réponse non contrôlée. Les calculs sont courts et doivent rester mentaux."
  }
 ]
}
</script>

<noscript>Le QCM interactif nécessite JavaScript. Les énoncés et corrigés sont aussi disponibles <a href="../automatismes-N19-variables-aleatoires-esperance/">en lecture</a>.</noscript>
