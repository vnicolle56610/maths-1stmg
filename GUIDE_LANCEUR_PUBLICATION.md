# Guide d'utilisation — `lancer_publication.sh`

Ce script régénère le site depuis `CLAUDE/Niveau_1stmg` (voir
`config_site.yaml`), construit le site MkDocs, et peut le publier sur
GitHub Pages.

**Modèle de l'outil : un état de publication, pas une sélection
temporaire.** `publication_manifest.json` (à la racine du projet, suivi
par Git) enregistre explicitement ce qui doit être publié. Le CLI
(`--sync-only`, sans argument, `--deploy`) ne fait que régénérer `docs/`
pour qu'il corresponde exactement à ce manifeste — il ne décide jamais
lui-même d'ajouter ou de retirer une ressource. Seul `--gui` permet de
cocher/décocher l'état final souhaité.

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
| `./scripts/lancer_publication.sh --sync-only` | Régénère `docs/` (copies de PDF, blocs AUTO-DOCS) pour qu'il corresponde exactement à `publication_manifest.json` — n'ajoute, ne retire jamais rien de lui-même. **Ne construit pas le site, ne publie rien.** |
| `./scripts/lancer_publication.sh` | Fait tout ce que fait `--sync-only`, puis lance `mkdocs build` (construit le site dans `site/`, en local). **Ne publie toujours rien en ligne.** |
| `./scripts/lancer_publication.sh --deploy` | Fait tout ce qui précède, vérifie que le dépôt local est propre et strictement synchronisé avec `origin/main` (même garde-fou que le bouton « Déployer » du GUI), puis **publie sur GitHub Pages** (`mkdocs gh-deploy`, qui pousse sur `origin`). S'il y a du nouveau contenu à régénérer, ce premier lancement l'écrit sans le publier : il faut le relire, le committer, puis relancer `--deploy`. |
| `./scripts/lancer_publication.sh --gui` | Ouvre l'interface graphique (`publier_ressources_gui.py`) : cases à cocher représentant l'état de publication final souhaité, prévisualisation en diff (ajouts/retraits), application avec commit automatique, puis boutons dédiés « Pousser vers GitHub » et « Déployer sur GitHub Pages ». Seul moyen de faire évoluer ce qui est publié. |
| `./scripts/lancer_publication.sh --bootstrap-manifest` | Reconstruit `publication_manifest.json` depuis ce qui est déjà référencé dans les pages. Opération de migration, à ne lancer qu'une fois (ou avec `--force`) ; n'écrit jamais dans `docs/`. |

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

## Le pipeline automatique ne change jamais ce qui est publié

`--sync-only`, le mode par défaut et `--deploy` régénèrent `docs/`
strictement à l'identique de `publication_manifest.json`. Une ressource
absente de la source (`Niveau_1stmg`) mais toujours dans le manifeste
**reste publiée** — elle n'est jamais retirée silencieusement parce
qu'un fichier a disparu du dossier de travail. Seule une action explicite
dans le GUI (décocher, puis confirmer le retrait) peut faire disparaître
une ressource du catalogue.

Pour ajouter une nouveauté ou retirer quoi que ce soit, il faut donc
toujours passer par `--gui`.

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
