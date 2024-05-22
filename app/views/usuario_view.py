from flask import render_template
from flask_login import current_user


def registro():
    return render_template(
        "register.html", title="Registro de usuarios", current_user=current_user
    )

    
def login():
    return render_template(
        "login.html", title="Inicio de sesión", current_user=current_user
    )
