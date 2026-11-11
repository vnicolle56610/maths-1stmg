---
title: "QCM automatismes Première STMG – Modèles d’évolution, seuils, tableur et Python (interactif, corrigé)"
description: "QCM en ligne d'automatismes de Première STMG (modèles d’évolution, seuils, tableur et Python) : chronomètre, score immédiat et correction détaillée, sans calculatrice."
---

# QCM interactif — Modèles d’évolution, seuils, tableur et Python

Entraînement **sans calculatrice**. Rien n'est enregistré ni envoyé : tout se passe dans le navigateur.

[← Énoncés et corrigés à lire](automatismes-N10-evolution-seuils-python.md)

<div class="auto-qcm" data-banque="banque-automatismes"></div>

<script type="application/json" id="banque-automatismes">
{
 "notion": "N10",
 "cle": "N10",
 "titre": "Modèles d’évolution, seuils, tableur et Python",
 "niveau": "Première STMG",
 "series": [
  {
   "lettre": "A",
   "theme": "Termes et sommes finies",
   "duree": "6 min",
   "consigne": "Calculer rapidement des termes et des sommes courtes.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "B",
   "theme": "Rang seuil",
   "duree": "6 min",
   "consigne": "Déterminer à partir de quel rang un seuil est dépassé.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "C",
   "theme": "Tableur et algorithme",
   "duree": "7 min",
   "consigne": "Lire une formule de tableur ou un petit algorithme.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "D",
   "theme": "QCM : évolutions et seuils",
   "duree": "7 min",
   "consigne": "Choisir la bonne réponse sans calculatrice.",
   "qcm": true,
   "figure": ""
  }
 ],
 "questions": [
  {
   "id": "N10-A1",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(120+15\\times4\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{180}\\)<\/span>.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-A2",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(200\\times1{,}05\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{210}\\)<\/span>.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-A3",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(50+55+60\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{165}\\)<\/span>.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-A4",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(u(n)=30+8n\\)<\/span>, calculer <span class=\"arithmatex\">\\(u(6)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(30+8\\times6=\\boxed{78}\\)<\/span>.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-A5",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(v(n)=100\\times1{,}1^n\\)<\/span>, calculer <span class=\"arithmatex\">\\(v(2)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(100\\times1{,}21=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{121}\\)<\/span>.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-A6",
   "serie": "A",
   "theme": "Termes et sommes finies",
   "type": "flash",
   "enonce": "Une offre coûte <span class=\"arithmatex\">\\(12\\)<\/span> euros par mois pendant <span class=\"arithmatex\">\\(6\\)<\/span> mois. Calculer le total.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(12\\times6=\\boxed{72}\\)<\/span> euros.",
   "methode": "Pour un modèle explicite, remplacer <span class=\"arithmatex\">\\(n\\)<\/span> par le rang demandé."
  },
  {
   "id": "N10-B1",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Suite <span class=\"arithmatex\">\\(u(n)=50+10n\\)<\/span>. À partir de quel rang <span class=\"arithmatex\">\\(u(n)\\geqslant 100\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(50+10n\\geqslant100\\)<\/span> : premier rang <span class=\"arithmatex\">\\(\\boxed{5}\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-B2",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Suite <span class=\"arithmatex\">\\(u(n)=20+5n\\)<\/span>. À partir de quel rang <span class=\"arithmatex\">\\(u(n)&gt;50\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(20+5n&gt;50\\)<\/span> : <span class=\"arithmatex\">\\(n&gt;6\\)<\/span>, premier rang <span class=\"arithmatex\">\\(\\boxed{7}\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-B3",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Valeurs : <span class=\"arithmatex\">\\(80;96;115{,}2;138{,}24\\)<\/span>. Quel est le premier terme supérieur à <span class=\"arithmatex\">\\(100\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Premier terme supérieur à <span class=\"arithmatex\">\\(100\\)<\/span> : <span class=\"arithmatex\">\\(\\boxed{115{,}2}\\)<\/span>, rang <span class=\"arithmatex\">\\(2\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-B4",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Une clientèle vaut <span class=\"arithmatex\">\\(300\\)<\/span> puis augmente de <span class=\"arithmatex\">\\(50\\)<\/span> par mois. Quand dépasse-t-elle <span class=\"arithmatex\">\\(500\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(300+50n&gt;500\\)<\/span> : premier mois <span class=\"arithmatex\">\\(\\boxed{5}\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-B5",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(u(0)=40\\)<\/span> et <span class=\"arithmatex\">\\(u(n+1)=u(n)+7\\)<\/span>, calculer le premier rang tel que <span class=\"arithmatex\">\\(u(n)\\geqslant61\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(40;47;54;61\\)<\/span> : premier rang <span class=\"arithmatex\">\\(\\boxed{3}\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-B6",
   "serie": "B",
   "theme": "Rang seuil",
   "type": "flash",
   "enonce": "Compléter : chercher un seuil, c'est chercher le premier rang pour lequel une condition devient <span class=\"arithmatex\">\\(\\ldots\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{\\text{vraie}}\\)<\/span>.",
   "methode": "Un rang seuil se vérifie toujours en testant le rang trouvé et le précédent."
  },
  {
   "id": "N10-C1",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "En B2, on a <span class=\"arithmatex\">\\(120\\)<\/span>. En B3 : <code>=B2+8<\/code>. Quelle valeur en B3 ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{128}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-C2",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "En B2, on a <span class=\"arithmatex\">\\(200\\)<\/span>. En B3 : <code>=B2*1,04<\/code>. Quelle valeur en B3 ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{208}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-C3",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "Si on recopie <code>=B2+8<\/code> vers le bas, quel type de suite obtient-on ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{\\text{arithmétique}}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-C4",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "Si on recopie <code>=B2*0,95<\/code> vers le bas, quel type de suite obtient-on ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\boxed{\\text{géométrique}}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-C5",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "Algorithme : <span class=\"arithmatex\">\\(n=0\\)<\/span>, <span class=\"arithmatex\">\\(u=100\\)<\/span>. Tant que <span class=\"arithmatex\">\\(u&lt;140\\)<\/span> : <span class=\"arithmatex\">\\(u=u+10\\)<\/span>, <span class=\"arithmatex\">\\(n=n+1\\)<\/span>. Valeur finale de <span class=\"arithmatex\">\\(n\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(100;110;120;130;140\\)<\/span> : <span class=\"arithmatex\">\\(\\boxed{n=4}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-C6",
   "serie": "C",
   "theme": "Tableur et algorithme",
   "type": "flash",
   "enonce": "Dans un programme, pourquoi initialise-t-on <span class=\"arithmatex\">\\(n=0\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Pour partir du <span class=\"arithmatex\">\\(\\boxed{\\text{rang initial}}\\)<\/span>.",
   "methode": "La boucle « tant que » continue tant que la condition est vraie."
  },
  {
   "id": "N10-D1",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "Un capital de <span class=\"arithmatex\">\\(1000\\)<\/span> augmente de <span class=\"arithmatex\">\\(3\\%\\)<\/span>.",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(1030\\)<\/span>",
    "<span class=\"arithmatex\">\\(1003\\)<\/span>",
    "<span class=\"arithmatex\">\\(970\\)<\/span>",
    "<span class=\"arithmatex\">\\(3000\\)<\/span>"
   ],
   "bonne": 0,
   "corrige": "<span class=\"arithmatex\">\\(1000\\times1{,}03=1030\\)<\/span>.",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  },
  {
   "id": "N10-D2",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "Modèle <span class=\"arithmatex\">\\(u(n)=250-20n\\)<\/span>. Le seuil <span class=\"arithmatex\">\\(u(n)\\leqslant150\\)<\/span> est atteint au rang",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(4\\)<\/span>",
    "<span class=\"arithmatex\">\\(5\\)<\/span>",
    "<span class=\"arithmatex\">\\(6\\)<\/span>",
    "<span class=\"arithmatex\">\\(100\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(250-20\\times5=150\\)<\/span>.",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  },
  {
   "id": "N10-D3",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "Une formule <code>=B2*1,07<\/code> correspond à",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(+7\\)<\/span>",
    "<span class=\"arithmatex\">\\(+7\\%\\)<\/span>",
    "<span class=\"arithmatex\">\\(-7\\%\\)<\/span>",
    "<span class=\"arithmatex\">\\(\\times7\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "coefficient <span class=\"arithmatex\">\\(1{,}07\\)<\/span>.",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  },
  {
   "id": "N10-D4",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "La somme <span class=\"arithmatex\">\\(10+15+20+25\\)<\/span> vaut",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(60\\)<\/span>",
    "<span class=\"arithmatex\">\\(70\\)<\/span>",
    "<span class=\"arithmatex\">\\(75\\)<\/span>",
    "<span class=\"arithmatex\">\\(80\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(10+15+20+25=70\\)<\/span>.",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  },
  {
   "id": "N10-D5",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "Dans une boucle de seuil, la variable <span class=\"arithmatex\">\\(n\\)<\/span> sert à",
   "contexte": [],
   "choix": [
    "compter les rangs",
    "stocker le seuil",
    "calculer un pourcentage",
    "écrire le titre"
   ],
   "bonne": 0,
   "corrige": "compter les rangs",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  },
  {
   "id": "N10-D6",
   "serie": "D",
   "theme": "QCM : évolutions et seuils",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(u(0)=500\\)<\/span> et <span class=\"arithmatex\">\\(u(n+1)=0{,}8u(n)\\)<\/span>, le stock",
   "contexte": [],
   "choix": [
    "augmente",
    "diminue",
    "reste constant",
    "double"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(0&lt;0{,}8&lt;1\\)<\/span>.",
   "methode": "Les automatismes de seuil combinent calcul, comparaison et interprétation."
  }
 ]
}
</script>

<noscript>Le QCM interactif nécessite JavaScript. Les énoncés et corrigés sont aussi disponibles <a href="../automatismes-N10-evolution-seuils-python/">en lecture</a>.</noscript>
