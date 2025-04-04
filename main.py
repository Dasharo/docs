def define_env(env):
    """ Define macros for MkDocs """
    
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
