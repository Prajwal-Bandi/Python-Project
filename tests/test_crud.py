import pytest
from app.crud import create_patient, get_patient, delete_patient, PatientNotFound

def test_create_get_delete_patient():
    patient = create_patient("Test Patient", 30, "Flu")
    assert patient.name == "Test Patient"
    
    fetched = get_patient(patient.id)
    assert fetched.id == patient.id
    
    delete_patient(patient.id)
    
    with pytest.raises(PatientNotFound):
        get_patient(patient.id)
