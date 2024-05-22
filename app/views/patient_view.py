from flask import render_template
from flask_login import current_user


def list_patients(patients):
    return render_template(
        "patients.html",
        patient=patients,
        title="Lista de Pacientes",
        current_user=current_user,
    )

def create_patients():
    return render_template(
        "create_patients.html", title="Crear Paciente", current_user=current_user
    )

def update_patients(patients):
    return render_template(
        "update_patient.html",
        title="Editar Paciente",
        patient=patients,
        current_user=current_user,
    )
