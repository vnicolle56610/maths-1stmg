---
title: "QCM automatismes Première STMG – Probabilités conditionnelles et indépendance (interactif, corrigé)"
description: "QCM en ligne d'automatismes de Première STMG (probabilités conditionnelles et indépendance) : chronomètre, score immédiat et correction détaillée, sans calculatrice."
---

# QCM interactif — Probabilités conditionnelles et indépendance

Entraînement **sans calculatrice**. Rien n'est enregistré ni envoyé : tout se passe dans le navigateur.

[← Énoncés et corrigés à lire](automatismes-N17-probabilites-conditionnelles.md)

<div class="auto-qcm" data-banque="banque-automatismes"></div>

<script type="application/json" id="banque-automatismes">
{
 "notion": "N17",
 "cle": "N17",
 "titre": "Probabilités conditionnelles et indépendance",
 "niveau": "Première STMG",
 "series": [
  {
   "lettre": "A",
   "theme": "Distinguer intersection et conditionnement",
   "duree": "6 min",
   "consigne": "Identifier la probabilité demandée avant de calculer.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "B",
   "theme": "Lire un arbre pondéré",
   "duree": "6 min",
   "consigne": "Calculer avec les branches d'un arbre simple.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "C",
   "theme": "Tableau croisé et indépendance",
   "duree": "6 min",
   "consigne": "Passer d'un tableau à des probabilités.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "D",
   "theme": "QCM type épreuve",
   "duree": "6 min",
   "consigne": "Choisir une seule réponse. Aucune justification demandée.",
   "qcm": true,
   "figure": ""
  }
 ],
 "questions": [
  {
   "id": "N17-A1",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Traduire <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span> en phrase courte.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span> : <strong class=\"auto-resultat\"><span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span><\/strong>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-A2",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Traduire <span class=\"arithmatex\">\\(P_A(B)\\)<\/span> en phrase courte.",
   "contexte": [
    "<strong>Q1.<\/strong> Traduire <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span> en phrase courte."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P_A(B)\\)<\/span> : <strong class=\"auto-resultat\">probabilité de <span class=\"arithmatex\">\\(B\\)<\/span> sachant <span class=\"arithmatex\">\\(A\\)<\/span><\/strong>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-A3",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(P(A)=0{,}6\\)<\/span> et <span class=\"arithmatex\">\\(P_A(B)=0{,}3\\)<\/span>, calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A\\cap B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}6\\times0{,}3=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}18}\\)<\/span>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-A4",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(P(B)=0{,}4\\)<\/span> et <span class=\"arithmatex\">\\(P_B(A)=0{,}5\\)<\/span>, calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A\\cap B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}4\\times0{,}5=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}20}\\)<\/span>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-A5",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(P(A\\cap B)=0{,}18\\)<\/span> et <span class=\"arithmatex\">\\(P(A)=0{,}6\\)<\/span>, calculer <span class=\"arithmatex\">\\(P_A(B)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P_A(B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{0{,}18}{0{,}6}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}3}\\)<\/span>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-A6",
   "serie": "A",
   "theme": "Distinguer intersection et conditionnement",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span> sont indépendants, quelle égalité utilise-t-on ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span> indépendants : <span class=\"arithmatex\">\\(\\boxed{P(A\\cap B)=P(A)P(B)}\\)<\/span>.",
   "methode": "Pour une probabilité conditionnelle, diviser par la probabilité de l'événement qui est déjà réalisé."
  },
  {
   "id": "N17-B1",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "On a <span class=\"arithmatex\">\\(P(A)=0{,}7\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(\\overline A)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(\\overline A)=\\)<\/span><wbr><span class=\"arithmatex\">\\(1-0{,}7=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}3}\\)<\/span>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-B2",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "On a <span class=\"arithmatex\">\\(P(A)=0{,}7\\)<\/span> et <span class=\"arithmatex\">\\(P_A(B)=0{,}2\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A\\cap B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}7\\times0{,}2=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}14}\\)<\/span>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-B3",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "On a <span class=\"arithmatex\">\\(P(\\overline A)=0{,}3\\)<\/span> et <span class=\"arithmatex\">\\(P_{\\overline A}(B)=0{,}5\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(\\overline A\\cap B)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(\\overline A\\cap B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}3\\times0{,}5=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}15}\\)<\/span>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-B4",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span> avec les deux résultats précédents.",
   "contexte": [
    "<strong>Q1.<\/strong> On a <span class=\"arithmatex\">\\(P(A)=0{,}7\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(\\overline A)\\)<\/span>.",
    "<strong>Q2.<\/strong> On a <span class=\"arithmatex\">\\(P(A)=0{,}7\\)<\/span> et <span class=\"arithmatex\">\\(P_A(B)=0{,}2\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
    "<strong>Q3.<\/strong> On a <span class=\"arithmatex\">\\(P(\\overline A)=0{,}3\\)<\/span> et <span class=\"arithmatex\">\\(P_{\\overline A}(B)=0{,}5\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(\\overline A\\cap B)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}14+0{,}15=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}29}\\)<\/span>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-B5",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "Dans un arbre, additionne-t-on ou multiplie-t-on le long d'un chemin ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Le long d'un chemin, on <strong class=\"auto-resultat\">multiplie<\/strong>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-B6",
   "serie": "B",
   "theme": "Lire un arbre pondéré",
   "type": "flash",
   "enonce": "Dans un arbre, additionne-t-on ou multiplie-t-on des chemins incompatibles ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Des chemins incompatibles, on <strong class=\"auto-resultat\">additionne<\/strong>.",
   "methode": "Arbre pondéré : multiplier sur les branches d'un chemin, additionner les chemins favorables."
  },
  {
   "id": "N17-C1",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{24+36}{100}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}60}\\)<\/span>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-C2",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span>.",
   "contexte": [
    "<strong>Q1.<\/strong> Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{24+16}{100}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}40}\\)<\/span>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-C3",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
   "contexte": [
    "<strong>Q1.<\/strong> Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>.",
    "<strong>Q2.<\/strong> Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(A\\cap B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{24}{100}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}24}\\)<\/span>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-C4",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P_A(B)\\)<\/span>.",
   "contexte": [
    "<strong>Q1.<\/strong> Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>.",
    "<strong>Q2.<\/strong> Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span>.",
    "<strong>Q3.<\/strong> Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P_A(B)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{24}{60}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}40}\\)<\/span>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-C5",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P_B(A)\\)<\/span>.",
   "contexte": [
    "<strong>Q1.<\/strong> Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>.",
    "<strong>Q2.<\/strong> Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span>.",
    "<strong>Q3.<\/strong> Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
    "<strong>Q4.<\/strong> Calculer <span class=\"arithmatex\">\\(P_A(B)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P_B(A)=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\frac{24}{40}=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}60}\\)<\/span>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-C6",
   "serie": "C",
   "theme": "Tableau croisé et indépendance",
   "type": "flash",
   "enonce": "Les événements <span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span> sont-ils indépendants ?",
   "contexte": [
    "<strong>Q1.<\/strong> Dans un groupe de <span class=\"arithmatex\">\\(100\\)<\/span> élèves : <span class=\"arithmatex\">\\(A\\cap B=24\\)<\/span>, <span class=\"arithmatex\">\\(A\\cap\\overline B=36\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap B=16\\)<\/span>, <span class=\"arithmatex\">\\(\\overline A\\cap\\overline B=\\)<\/span><wbr><span class=\"arithmatex\">\\(24\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(A)\\)<\/span>.",
    "<strong>Q2.<\/strong> Calculer <span class=\"arithmatex\">\\(P(B)\\)<\/span>.",
    "<strong>Q3.<\/strong> Calculer <span class=\"arithmatex\">\\(P(A\\cap B)\\)<\/span>.",
    "<strong>Q4.<\/strong> Calculer <span class=\"arithmatex\">\\(P_A(B)\\)<\/span>.",
    "<strong>Q5.<\/strong> Calculer <span class=\"arithmatex\">\\(P_B(A)\\)<\/span>."
   ],
   "choix": [],
   "bonne": null,
   "corrige": "Oui, car <span class=\"arithmatex\">\\(0{,}60\\times0{,}40=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}24\\)<\/span>. <strong class=\"auto-resultat\">Indépendants<\/strong>.",
   "methode": "Dans un tableau, la condition fixe le total de référence."
  },
  {
   "id": "N17-D1",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(P(A)=0{,}4\\)<\/span>, alors <span class=\"arithmatex\">\\(P(\\overline A)=\\)<\/span>",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}4\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}6\\)<\/span>",
    "<span class=\"arithmatex\">\\(1{,}4\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}04\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "Réponse : <span class=\"arithmatex\">\\(1-0{,}4=0{,}6\\)<\/span>.",
   "methode": "En probabilités, commencer par traduire la notation en mots."
  },
  {
   "id": "N17-D2",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(P(A)=0{,}5\\)<\/span> et <span class=\"arithmatex\">\\(P_A(B)=0{,}2\\)<\/span>, alors <span class=\"arithmatex\">\\(P(A\\cap B)=\\)<\/span>",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}7\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}3\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}1\\)<\/span>",
    "<span class=\"arithmatex\">\\(2{,}5\\)<\/span>"
   ],
   "bonne": 2,
   "corrige": "Réponse : <span class=\"arithmatex\">\\(0{,}5\\times0{,}2=0{,}1\\)<\/span>.",
   "methode": "En probabilités, commencer par traduire la notation en mots."
  },
  {
   "id": "N17-D3",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "<span class=\"arithmatex\">\\(P_A(B)\\)<\/span> signifie",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span>",
    "<span class=\"arithmatex\">\\(B\\)<\/span> sachant <span class=\"arithmatex\">\\(A\\)<\/span>",
    "<span class=\"arithmatex\">\\(A\\)<\/span> sachant <span class=\"arithmatex\">\\(B\\)<\/span>",
    "ni <span class=\"arithmatex\">\\(A\\)<\/span> ni <span class=\"arithmatex\">\\(B\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "Réponse : <span class=\"arithmatex\">\\(B\\)<\/span> sachant <span class=\"arithmatex\">\\(A\\)<\/span>.",
   "methode": "En probabilités, commencer par traduire la notation en mots."
  },
  {
   "id": "N17-D4",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Sur un chemin d'arbre, on",
   "contexte": [],
   "choix": [
    "additionne",
    "multiplie",
    "dérive",
    "moyenne"
   ],
   "bonne": 1,
   "corrige": "Réponse : on multiplie.",
   "methode": "En probabilités, commencer par traduire la notation en mots."
  },
  {
   "id": "N17-D5",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(P(A\\cap B)=P(A)P(B)\\)<\/span>, alors <span class=\"arithmatex\">\\(A\\)<\/span> et <span class=\"arithmatex\">\\(B\\)<\/span> sont",
   "contexte": [],
   "choix": [
    "incompatibles",
    "indépendants",
    "contraires",
    "égaux"
   ],
   "bonne": 1,
   "corrige": "Réponse : indépendants.",
   "methode": "En probabilités, commencer par traduire la notation en mots."
  }
 ]
}
</script>

<noscript>Le QCM interactif nécessite JavaScript. Les énoncés et corrigés sont aussi disponibles <a href="../automatismes-N17-probabilites-conditionnelles/">en lecture</a>.</noscript>
