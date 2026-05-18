"""
Red/green tests for the ToS gate feature (Tasks 0 & 1).

Covers:
  - tos_gated_downloads macro unit tests
  - tos-gate.js static assertions
  - Markdown source files: no plain dl.3mdeb.com links in gated sections
  - mkdocs.yml / overrides configuration
"""
import base64
import json
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_macros():
    """Collect macro functions from main.py by simulating define_env."""
    sys.path.insert(0, str(REPO_ROOT))
    import main  # noqa: PLC0415

    macros: dict = {}

    class _Env:
        def macro(self, fn):
            macros[fn.__name__] = fn
            return fn

    main.define_env(_Env())
    return macros


@pytest.fixture(scope="session")
def macros():
    return _load_macros()


@pytest.fixture(scope="session")
def tos_gate_js():
    return (REPO_ROOT / "docs/javascripts/tos-gate.js").read_text()


# ---------------------------------------------------------------------------
# tos_gated_downloads – unit tests
# ---------------------------------------------------------------------------

class TestTosGatedDownloads:
    def test_url_not_in_html_source(self, macros):
        """URLs must be absent from rendered HTML — only encoded in data-payload."""
        url = "https://dl.3mdeb.com/secret/firmware.zip"
        html = macros["tos_gated_downloads"]("s", [{"label": "f", "url": url}])
        assert url not in html

    def test_payload_is_valid_base64_json(self, macros):
        files = [{"label": "sha256", "url": "https://dl.3mdeb.com/file.sha256"}]
        html = macros["tos_gated_downloads"]("s", files)
        m = re.search(r'data-payload="([^"]+)"', html)
        assert m, "data-payload attribute missing from output"
        decoded = json.loads(base64.b64decode(m.group(1)))
        assert decoded == files

    def test_group_format_encodes_correctly(self, macros):
        files = [{"group": "Raw image", "note": "(fw.rom)", "items": [
            {"label": "sha256", "url": "https://dl.3mdeb.com/fw.sha256"},
        ]}]
        html = macros["tos_gated_downloads"]("s", files)
        assert "dl.3mdeb.com" not in html
        m = re.search(r'data-payload="([^"]+)"', html)
        decoded = json.loads(base64.b64decode(m.group(1)))
        assert decoded[0]["group"] == "Raw image"
        assert decoded[0]["note"] == "(fw.rom)"
        assert decoded[0]["items"][0]["url"] == "https://dl.3mdeb.com/fw.sha256"

    def test_checkbox_required_attributes(self, macros):
        html = macros["tos_gated_downloads"]("my-section", [])
        assert 'data-section="my-section"' in html
        assert 'onchange="revealGated(this)"' in html
        assert 'class="tos-gate__checkbox"' in html

    def test_section_content_div_present(self, macros):
        html = macros["tos_gated_downloads"]("my-section", [])
        assert 'id="my-section"' in html
        assert "tos-gate-content" in html

    def test_prose_section_id_emits_data_attribute(self, macros):
        html = macros["tos_gated_downloads"]("s", [], prose_section_id="my-prose")
        assert 'data-prose-section="my-prose"' in html

    def test_no_prose_section_id_omits_data_attribute(self, macros):
        html = macros["tos_gated_downloads"]("s", [])
        assert "data-prose-section" not in html

    def test_default_tos_url(self, macros):
        html = macros["tos_gated_downloads"]("s", [])
        assert 'href="https://www.dasharo.com/pages/terms/"' in html

    def test_custom_tos_url_override(self, macros):
        html = macros["tos_gated_downloads"]("s", [], tos_url="https://example.com/tos")
        assert 'href="https://example.com/tos"' in html
        assert "dasharo.com/pages/terms" not in html


# ---------------------------------------------------------------------------
# tos-gate.js – static assertions
# ---------------------------------------------------------------------------

class TestTosGateJs:
    def test_file_exists(self):
        assert (REPO_ROOT / "docs/javascripts/tos-gate.js").exists()

    def test_reveal_gated_function_defined(self, tos_gate_js):
        assert "function revealGated" in tos_gate_js

    def test_noreferrer_absent_from_link_template(self, tos_gate_js):
        """noreferrer on injected download links would strip the Referer header,
        breaking the MinIO bucket policy gate."""
        for line in tos_gate_js.splitlines():
            if "md-button" in line:
                assert "noreferrer" not in line, (
                    f"noreferrer must not appear in the injected link template: {line!r}"
                )

    def test_noreferrer_warning_comment_present(self, tos_gate_js):
        """The intentional absence of noreferrer should be documented."""
        assert "noreferrer" in tos_gate_js

    def test_prose_group_queryselector_present(self, tos_gate_js):
        """Multiple prose divs must be toggled via data-prose-group selector."""
        assert "data-prose-group" in tos_gate_js

    def test_group_rendering_branch_present(self, tos_gate_js):
        assert "f.group" in tos_gate_js

    def test_prose_elements_toggled_on_uncheck(self, tos_gate_js):
        """Unchecking must hide prose sections, not just clear download buttons."""
        assert 'display = "none"' in tos_gate_js or "display='none'" in tos_gate_js or \
               'style.display = "none"' in tos_gate_js


# ---------------------------------------------------------------------------
# Static file tests – variant markdown files (parameterized, opt-in)
#
# Tests run against every *.md under docs/variants/.
# Files that do not use tos_gated_downloads are skipped automatically,
# so adding the gate to a new variant is covered without touching this file.
# ---------------------------------------------------------------------------

_VARIANT_MD_FILES = sorted((REPO_ROOT / "docs/variants").rglob("*.md"))
_VARIANT_IDS = [str(f.relative_to(REPO_ROOT)) for f in _VARIANT_MD_FILES]


@pytest.mark.parametrize("md_file", _VARIANT_MD_FILES, ids=_VARIANT_IDS)
def test_no_plain_dl_links_in_gated_file(md_file):
    """Any file using tos_gated_downloads must not expose dl.3mdeb.com URLs
    as plain markdown links (inline or reference-style)."""
    content = md_file.read_text()
    if "tos_gated_downloads" not in content:
        pytest.skip("file does not use tos_gated_downloads")
    assert not re.search(r"^\[.*\]:\s+https://dl\.3mdeb\.com/", content, re.MULTILINE), \
        f"Reference-style link to dl.3mdeb.com found in {md_file.name}"
    assert not re.search(r"\]\(https://dl\.3mdeb\.com/", content), \
        f"Inline markdown link to dl.3mdeb.com found in {md_file.name}"


@pytest.mark.parametrize("md_file", _VARIANT_MD_FILES, ids=_VARIANT_IDS)
def test_prose_section_id_has_matching_div(md_file):
    """Any file using prose_section_id must have at least one data-prose-group div."""
    content = md_file.read_text()
    if "prose_section_id" not in content:
        pytest.skip("file does not use prose_section_id")
    assert "data-prose-group" in content, \
        f"prose_section_id used but no data-prose-group div found in {md_file.name}"


def test_at_least_one_variant_uses_tos_gated_downloads():
    """Sanity check: ensure the feature is actually in use and hasn't been
    accidentally removed from all variant files."""
    gated = [f for f in _VARIANT_MD_FILES if "tos_gated_downloads" in f.read_text()]
    assert gated, "No variant file uses tos_gated_downloads — feature may have been removed"


# ---------------------------------------------------------------------------
# Static file tests – infrastructure configuration
# ---------------------------------------------------------------------------

class TestInfrastructure:
    def test_mkdocs_yml_includes_tos_gate_js(self):
        content = (REPO_ROOT / "mkdocs.yml").read_text()
        assert "javascripts/tos-gate.js" in content

    def test_mkdocs_yml_permalink_enabled(self):
        content = (REPO_ROOT / "mkdocs.yml").read_text()
        assert "permalink: true" in content

    def test_overrides_main_html_referrer_meta(self):
        content = (REPO_ROOT / "overrides/main.html").read_text()
        assert 'name="referrer"' in content
        assert "strict-origin-when-cross-origin" in content
