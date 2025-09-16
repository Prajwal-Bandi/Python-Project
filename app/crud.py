from sqlalchemy.exc import NoResultFound
from .models import Patient
from .db import SessionLocal

class PatientNotFound(Exception):
    pass

def create_patient(name: str, age: int, disease: str) -> Patient:
    session = SessionLocal()
    patient = Patient(name=name, age=age, disease=disease)
    session.add(patient)
    session.commit()
    session.refresh(patient)
    session.close()
    return patient

def get_patient(patient_id: int) -> Patient:
    session = SessionLocal()
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    session.close()
    if not patient:
        raise PatientNotFound(f"Patient with id {patient_id} not found.")
    return patient

def update_patient(patient_id: int, name: str, age: int, disease: str) -> Patient:
    session = SessionLocal()
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        session.close()
        raise PatientNotFound(f"Patient with id {patient_id} not found.")
    patient.name = name
    patient.age = age
    patient.disease = disease
    session.commit()
    session.refresh(patient)
    session.close()
    return patient

def delete_patient(patient_id: int) -> None:
    session = SessionLocal()
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        session.close()
        raise PatientNotFound(f"Patient with id {patient_id} not found.")
    session.delete(patient)
    session.commit()
    session.close()
