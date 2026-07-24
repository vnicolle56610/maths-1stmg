#!/usr/bin/env bash
# Lance la synchronisation + le build du site, quel que soit le dossier
# depuis lequel on l'appelle.
#
#   ./scripts/lancer_publication.sh              synchronise + mkdocs build
#   ./scripts/lancer_publication.sh --deploy     + publication GitHub Pages
#   ./scripts/lancer_publication.sh --sync-only  synchronise sans build
#   ./scripts/lancer_publication.sh --gui        interface graphique de sélection des PDF
#
# Contrairement à maths-seconde et maths-premiere-specialite, ce lanceur
# appelle directement scripts/publier_ressources_site.py : il n'y a pas de
# scripts/synchroniser.py ni scripts/publier.py à côté (ces fichiers sont
# absents dans les deux autres dépôts, voir MEMO_RESTAURATION_SCRIPTS.md
# là-bas — le pipeline y est cassé). Le comportement des quatre commandes
# reste identique pour l'utilisateur.

set -euo pipefail

RACINE_PROJET="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RACINE_PROJET"

if [[ -f ".venv/bin/activate" ]]; then
    # shellcheck disable=SC1091
    source ".venv/bin/activate"
fi

if [[ "${1:-}" == "--gui" ]]; then
    exec python3 scripts/publier_ressources_gui.py
fi

if [[ "${1:-}" == "--sync-only" ]]; then
    exec python3 scripts/publier_ressources_site.py
fi

python3 scripts/publier_ressources_site.py
mkdocs build

if [[ "${1:-}" == "--deploy" ]]; then
    mkdocs gh-deploy
fi
