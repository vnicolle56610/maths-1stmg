# Guide d'utilisation — `lancer_publication.sh`

Ce script synchronise le site depuis `CLAUDE/Niveau_1stmg` (voir
`config_site.yaml`), construit le site MkDocs, et peut le publier sur
GitHub Pages.

## D'où le lancer

```bash
cd ~/ENSEIGNEMENT/maths-1stmg
./scripts/lancer_publication.sh
```

Fonctionne aussi avec le chemin complet depuis n'importe où :

```bash
~/ENSEIGNEMENT/maths-1stmg/scripts/lancer_publication.sh
```

## Les commandes disponibles

| Commande | Ce qu'elle fait |
|---|---|
| `./scripts/lancer_publication.sh --sync-only` | Scanne `Niveau_1stmg`, régénère les pages/nav/index, affiche le rapport. **Ne construit pas le site, ne publie rien.** |
| `./scripts/lancer_publication.sh` | Fait tout ce que fait `--sync-only`, puis lance `mkdocs build` (construit le site dans `site/`, en local). **Ne publie toujours rien en ligne.** |
| `./scripts/lancer_publication.sh --deploy` | Fait tout ce qui précède, **puis publie sur GitHub Pages** (`mkdocs gh-deploy`, qui pousse sur `origin`). |
| `./scripts/lancer_publication.sh --gui` | Ouvre l'interface graphique (`publier_ressources_gui.py`) avec les cases à cocher pour choisir précisément quels PDF publier. |

## Dans quel ordre travailler

1. **Vérifier d'abord sans rien publier** :
   ```bash
   ./scripts/lancer_publication.sh --sync-only
   ```
   Regarder le rapport : PDF reconnus, pages créées/modifiées, avertissements.

2. **Si le rapport est satisfaisant, publier en ligne** :
   ```bash
   ./scripts/lancer_publication.sh --deploy
   ```

3. **Après un déploiement**, si le site semble ne pas avoir changé dans le
   navigateur, faire un rechargement forcé (`Ctrl+Maj+R`) avant de s'inquiéter.

## Ne pas alterner avec l'interface graphique sur les mêmes notions

Le pipeline automatique (`--sync-only`, sans argument, `--deploy`) republie
**tout** ce qu'il reconnaît dans `Niveau_1stmg`, sans sélection manuelle.
L'interface graphique (`--gui`) permet de **décocher** certains PDF. Pour
une notion donnée, choisir un seul des deux outils tant que le contenu
source n'a pas changé.

## Prérequis

- Être dans un terminal Linux, avec `bash`.
- Un environnement virtuel Python dans `.venv/` (le script l'active tout
  seul s'il existe) contenant `mkdocs`, `mkdocs-material` et `pyyaml` :
  ```bash
  cd ~/ENSEIGNEMENT/maths-1stmg
  python3 -m venv .venv
  source .venv/bin/activate
  pip install mkdocs mkdocs-material pyyaml
  ```
- Le dossier `CLAUDE/Niveau_1stmg` accessible au chemin indiqué dans
  `config_site.yaml`.

## Commande personnelle dans `~/bin` (optionnel)

Pour coexister avec `lancer_publication_seconde` et
`lancer_publication_premiere` :

```bash
mkdir -p ~/bin

cat > ~/bin/lancer_publication_1stmg <<'EOF'
#!/usr/bin/env bash
exec "$HOME/ENSEIGNEMENT/maths-1stmg/scripts/lancer_publication.sh" --gui "$@"
EOF

chmod +x ~/bin/lancer_publication_1stmg
```

`~/bin` doit être dans le `PATH` (déjà fait si les lanceurs Seconde/Première
fonctionnent).
