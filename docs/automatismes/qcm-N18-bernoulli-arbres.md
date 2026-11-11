---
title: "QCM automatismes Première STMG – Épreuves indépendantes de Bernoulli et arbres (interactif, corrigé)"
description: "QCM en ligne d'automatismes de Première STMG (épreuves indépendantes de Bernoulli et arbres) : chronomètre, score immédiat et correction détaillée, sans calculatrice."
---

# QCM interactif — Épreuves indépendantes de Bernoulli et arbres

Entraînement **sans calculatrice**. Rien n'est enregistré ni envoyé : tout se passe dans le navigateur.

[← Énoncés et corrigés à lire](automatismes-N18-bernoulli-arbres.md)

<div class="auto-qcm" data-banque="banque-automatismes"></div>

<script type="application/json" id="banque-automatismes">
{
 "notion": "N18",
 "cle": "N18",
 "titre": "Épreuves indépendantes de Bernoulli et arbres",
 "niveau": "Première STMG",
 "series": [
  {
   "lettre": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "duree": "6 min",
   "consigne": "Identifier succès, échec et probabilité du succès.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "B",
   "theme": "Calculer des chemins d'arbre",
   "duree": "6 min",
   "consigne": "Multiplier les probabilités d'un chemin.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "C",
   "theme": "Au moins un succès",
   "duree": "6 min",
   "consigne": "Utiliser le complémentaire quand c'est plus rapide.",
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
   "id": "N18-A1",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Un client répond oui ou non à une offre. Est-ce une épreuve de Bernoulli ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Oui : deux issues, oui/non. <strong class=\"auto-resultat\">Bernoulli<\/strong>.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-A2",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Si la probabilité de succès est <span class=\"arithmatex\">\\(0{,}35\\)<\/span>, quelle est la probabilité d'échec ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(1-0{,}35=\\boxed{0{,}65}\\)<\/span>.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-A3",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}4\\)<\/span>, calculer la probabilité de deux succès successifs indépendants.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(0{,}4\\times0{,}4=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}16}\\)<\/span>.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-A4",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}4\\)<\/span>, calculer la probabilité de deux échecs successifs.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(0{,}6\\times0{,}6=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}36}\\)<\/span>.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-A5",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}4\\)<\/span>, calculer la probabilité du chemin succès puis échec.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(0{,}4\\times0{,}6=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}24}\\)<\/span>.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-A6",
   "serie": "A",
   "theme": "Reconnaître une épreuve de Bernoulli",
   "type": "flash",
   "enonce": "Dans un arbre de <span class=\"arithmatex\">\\(3\\)<\/span> épreuves, combien y a-t-il de niveaux de tirage ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Il y a <span class=\"arithmatex\">\\(\\boxed{3}\\)<\/span> niveaux de tirage.",
   "methode": "Une répétition indépendante de Bernoulli répète la même expérience à deux issues."
  },
  {
   "id": "N18-B1",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "On répète <span class=\"arithmatex\">\\(3\\)<\/span> fois une épreuve avec <span class=\"arithmatex\">\\(p=0{,}3\\)<\/span>. Calculer <span class=\"arithmatex\">\\(P(SSS)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(SSS)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}3^3=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}027}\\)<\/span>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-B2",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(SSE)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(SSE)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}3\\times0{,}3\\times0{,}7=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}063}\\)<\/span>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-B3",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "Calculer <span class=\"arithmatex\">\\(P(SES)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(P(SES)=\\)<\/span><wbr><span class=\"arithmatex\">\\(0{,}3\\times0{,}7\\times0{,}3=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}063}\\)<\/span>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-B4",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "Comparer <span class=\"arithmatex\">\\(P(SSE)\\)<\/span> et <span class=\"arithmatex\">\\(P(SES)\\)<\/span>.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Elles sont <strong class=\"auto-resultat\">égales<\/strong>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-B5",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "Combien de chemins donnent exactement deux succès en <span class=\"arithmatex\">\\(3\\)<\/span> épreuves ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Il y a <span class=\"arithmatex\">\\(\\boxed{3}\\)<\/span> chemins : <span class=\"arithmatex\">\\(SSE, SES, ESS\\)<\/span>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-B6",
   "serie": "B",
   "theme": "Calculer des chemins d'arbre",
   "type": "flash",
   "enonce": "En déduire la probabilité d'obtenir exactement deux succès.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Donc <span class=\"arithmatex\">\\(P=\\)<\/span><wbr><span class=\"arithmatex\">\\(3\\times0{,}063=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}189}\\)<\/span>.",
   "methode": "Pour « exactement », compter les chemins favorables puis additionner leurs probabilités."
  },
  {
   "id": "N18-C1",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(2\\)<\/span> épreuves indépendantes avec <span class=\"arithmatex\">\\(p=0{,}4\\)<\/span>, quelle est la probabilité d'aucun succès ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Aucun succès : <span class=\"arithmatex\">\\(0{,}6^2=\\boxed{0{,}36}\\)<\/span>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-C2",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "En déduire la probabilité d'au moins un succès.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Au moins un succès : <span class=\"arithmatex\">\\(1-0{,}36=\\boxed{0{,}64}\\)<\/span>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-C3",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(3\\)<\/span> épreuves avec <span class=\"arithmatex\">\\(p=0{,}5\\)<\/span>, calculer la probabilité d'aucun succès.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Aucun succès : <span class=\"arithmatex\">\\(0{,}5^3=\\boxed{0{,}125}\\)<\/span>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-C4",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "En déduire la probabilité d'au moins un succès.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Au moins un succès : <span class=\"arithmatex\">\\(1-0{,}125=\\)<\/span><wbr><span class=\"arithmatex\">\\(\\boxed{0{,}875}\\)<\/span>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-C5",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(4\\)<\/span> épreuves avec <span class=\"arithmatex\">\\(p=0{,}25\\)<\/span>, écrire la probabilité d'aucun succès sous forme de puissance.",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Aucun succès : <span class=\"arithmatex\">\\(\\boxed{0{,}75^4}\\)<\/span>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-C6",
   "serie": "C",
   "theme": "Au moins un succès",
   "type": "flash",
   "enonce": "Que signifie « au moins un » ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "« Au moins un » signifie <strong class=\"auto-resultat\">un ou plusieurs<\/strong>.",
   "methode": "Pour « au moins un », calculer souvent <span class=\"arithmatex\">\\(1-P(\\text{aucun})\\)<\/span>."
  },
  {
   "id": "N18-D1",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Une épreuve de Bernoulli a",
   "contexte": [],
   "choix": [
    "une seule issue",
    "deux issues",
    "trois issues",
    "une infinité d'issues"
   ],
   "bonne": 1,
   "corrige": "Réponse : deux issues.",
   "methode": "Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance."
  },
  {
   "id": "N18-D2",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Si <span class=\"arithmatex\">\\(p=0{,}2\\)<\/span>, la probabilité d'échec est",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(0{,}2\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}8\\)<\/span>",
    "<span class=\"arithmatex\">\\(1{,}2\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}02\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "Réponse : <span class=\"arithmatex\">\\(1-0{,}2=0{,}8\\)<\/span>.",
   "methode": "Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance."
  },
  {
   "id": "N18-D3",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Pour deux succès indépendants de probabilité <span class=\"arithmatex\">\\(0{,}5\\)<\/span>, la probabilité est",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(1\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}25\\)<\/span>",
    "<span class=\"arithmatex\">\\(0{,}5\\)<\/span>",
    "<span class=\"arithmatex\">\\(2\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "Réponse : <span class=\"arithmatex\">\\(0{,}5\\times0{,}5=0{,}25\\)<\/span>.",
   "methode": "Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance."
  },
  {
   "id": "N18-D4",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Le contraire de « au moins un succès » est",
   "contexte": [],
   "choix": [
    "exactement un succès",
    "aucun succès",
    "deux succès",
    "succès certain"
   ],
   "bonne": 1,
   "corrige": "Réponse : aucun succès.",
   "methode": "Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance."
  },
  {
   "id": "N18-D5",
   "serie": "D",
   "theme": "QCM type épreuve",
   "type": "qcm",
   "enonce": "Dans un arbre d'épreuves indépendantes, un chemin se calcule en",
   "contexte": [],
   "choix": [
    "additionnant",
    "multipliant",
    "dérivant",
    "moyennant"
   ],
   "bonne": 1,
   "corrige": "Réponse : en multipliant.",
   "methode": "Les automatismes de Bernoulli reposent sur trois mots : succès, échec, indépendance."
  }
 ]
}
</script>

<noscript>Le QCM interactif nécessite JavaScript. Les énoncés et corrigés sont aussi disponibles <a href="../automatismes-N18-bernoulli-arbres/">en lecture</a>.</noscript>
