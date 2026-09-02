"""Tests ciblés du correctif I15 sur l'outil actif STMG (filet de sécurité).

Ne couvre que ``deployed_site_path``/``deployed_site_paths`` de
``publier_ressources_gui.py`` : la conversion chemin source ``docs/...``
-> sortie MkDocs réelle, utilisée par le contrôle post-déploiement.
Reprend les scénarios réels observés lors de l'audit du retrait de
l'automatisme N01 (2026-09-02) : le contrôle comparait auparavant des
chemins ``.md`` à ``origin/gh-pages``, qui n'en contient jamais.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from publier_ressources_gui import (
    deployed_site_path,
    deployed_site_paths,
    missing_expected_outputs,
)


def _git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def gh_pages_repo(tmp_path: Path) -> Path:
    """Dépôt temporaire avec une branche gh-pages simulant une sortie MkDocs
    réelle (.nojekyll, sitemap.xml, un index.html de section, une page de
    notion, un PDF)."""
    repo = tmp_path / "site"
    repo.mkdir()
    _git(repo, "init", "-q", "-b", "gh-pages")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "Test")
    (repo / ".nojekyll").write_text("")
    (repo / "sitemap.xml").write_text("<urlset/>")
    (repo / "automatismes").mkdir()
    (repo / "automatismes" / "index.html").write_text("<html/>")
    (repo / "automatismes" / "AUTOMATISMES_N01.pdf").write_text("%PDF-1.4")
    (repo / "notions" / "N01-rentree-donnees-logique").mkdir(parents=True)
    (repo / "notions" / "N01-rentree-donnees-logique" / "index.html").write_text("<html/>")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "gh-pages simulée")
    return repo


def test_notion_md_devient_index_html():
    assert (
        deployed_site_path("docs/notions/N01-rentree-donnees-logique.md")
        == "notions/N01-rentree-donnees-logique/index.html"
    )


def test_section_index_md_devient_index_html():
    assert deployed_site_path("docs/automatismes/index.md") == "automatismes/index.html"


def test_pdf_inchange():
    assert (
        deployed_site_path("docs/automatismes/AUTOMATISMES_N01_RENTREE_DONNEES_LOGIQUE.pdf")
        == "automatismes/AUTOMATISMES_N01_RENTREE_DONNEES_LOGIQUE.pdf"
    )


def test_index_racine():
    assert deployed_site_path("docs/index.md") == "index.html"


def test_chemin_hors_docs_ignore():
    assert deployed_site_path("scripts/publier_ressources_gui.py") is None


def test_fichier_genere_present_ok(gh_pages_repo: Path):
    missing = missing_expected_outputs(
        gh_pages_repo, "HEAD", ("automatismes/index.html",)
    )
    assert missing == ()


def test_fichier_reellement_absent_echoue(gh_pages_repo: Path):
    missing = missing_expected_outputs(
        gh_pages_repo, "HEAD", ("automatismes/AUTOMATISMES_N01_INEXISTANT.pdf",)
    )
    assert missing == ("automatismes/AUTOMATISMES_N01_INEXISTANT.pdf",)


def test_ancien_controle_md_aurait_echoue_a_tort(gh_pages_repo: Path):
    """Reproduit le faux échec réel du 2026-09-02 : le contrôle avant
    correctif cherchait le .md directement (jamais présent dans gh-pages),
    alors que le déploiement avait réellement réussi (index.html présent)."""
    ancien_chemin_md = "automatismes/index.md"
    nouveau_chemin_html = deployed_site_path(f"docs/{ancien_chemin_md}")

    assert missing_expected_outputs(gh_pages_repo, "HEAD", (ancien_chemin_md,)) == (
        ancien_chemin_md,
    )
    assert missing_expected_outputs(
        gh_pages_repo, "HEAD", (nouveau_chemin_html,)
    ) == ()


def test_cas_reel_retrait_automatisme_n01():
    """Reproduit exactement les deux chemins staged du commit d0399ad :
    l'ancien contrôle cherchait ces .md littéralement dans gh-pages
    (toujours absent -> faux échec) ; le nouveau cherche le HTML généré."""
    staged = (
        "docs/automatismes/index.md",
        "docs/notions/N01-rentree-donnees-logique.md",
    )
    assert deployed_site_paths(staged) == (
        "automatismes/index.html",
        "notions/N01-rentree-donnees-logique/index.html",
    )
