import base64
import json


def define_env(env):
    """ Define macros for MkDocs """

    @env.macro
    def tos_gated_downloads(section_id, files, tos_url="https://www.dasharo.com/pages/terms/",
                            prose_section_id=None):
        """Render a ToS checkbox that reveals base64-encoded download links on acceptance.

        files: flat list of {"label": str, "url": str} dicts, or grouped list of
               {"group": str, "items": [...], "note": str (optional)} dicts.
               URLs are not emitted into HTML source — base64-encoded in a data
               attribute and injected by tos-gate.js when the checkbox is checked.

        prose_section_id: when set, tos-gate.js also toggles all elements carrying
               data-prose-group="{prose_section_id}". Multiple elements may share
               the same value, allowing one checkbox to reveal several prose blocks.
        """
        payload = base64.b64encode(json.dumps(files).encode()).decode()
        checkbox_id = f"tos-cb-{section_id}"
        prose_attr = f' data-prose-section="{prose_section_id}"' if prose_section_id else ""
        return (
            '<div class="tos-gate">'
            f'<label class="tos-gate__label" for="{checkbox_id}">'
            f'<input type="checkbox" id="{checkbox_id}" class="tos-gate__checkbox" '
            f'data-section="{section_id}"{prose_attr} onchange="revealGated(this)"> '
            'I confirm that I have read and agree to the '
            f'<a href="{tos_url}" target="_blank" rel="noopener noreferrer">'
            'Dasharo Terms of Service</a> and all applicable open-source '
            'licensing terms governing this firmware release.'
            '</label>'
            f'<div id="{section_id}" class="tos-gate-content" data-payload="{payload}"></div>'
            '</div>'
        )

    @env.macro
    def tos_checkbox(section_id, tos_url="https://www.dasharo.com/pages/terms/"):
        """Render a ToS acceptance checkbox that reveals the section with the given id."""
        checkbox_id = f"tos-cb-{section_id}"
        onchange = (
            f"document.getElementById('{section_id}').style.display="
            f"this.checked?'':'none'"
        )
        return (
            '<div class="tos-gate">'
            f'<label class="tos-gate__label" for="{checkbox_id}">'
            f'<input type="checkbox" id="{checkbox_id}" '
            f'class="tos-gate__checkbox" onchange="{onchange}"> '
            'I confirm that I have read and agree to the '
            f'<a href="{tos_url}" target="_blank" rel="noopener noreferrer">'
            'Dasharo Terms of Service</a> and all applicable open-source '
            'licensing terms governing this firmware release.'
            '</label>'
            '</div>'
        )

    @env.macro
    def subscribe_form(list_id, btn_text):
        return (
        f'<form action="https://listmonk.3mdeb.com/subscription/form" method="post" class="subscribe-form">'
        f'    <input type="email" name="email" placeholder="Enter your email" required />'
        f'    <input type="checkbox" name="l" checked value="{list_id}" style="display: none"/>'
        f'    <button type="submit" class="md-button md-button--primary">'
        f'        {btn_text}'
        f'    </button>'
        f'</form>'
        )
