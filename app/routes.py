from flask import request, jsonify
from .crud import create_patient, get_patient, update_patient, delete_patient, PatientNotFound
from .emailer import send_email_background

def init_routes(app):
    @app.route('/patients', methods=['POST'])
    def create():
        data = request.json
        patient = create_patient(data['name'], data['age'], data['disease'])
        
        send_email_background(patient)
        return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease}), 201

    @app.route('/patients/<int:patient_id>', methods=['GET'])
    def read(patient_id):
        try:
            patient = get_patient(patient_id)
            return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease})
        except PatientNotFound as e:
            return jsonify({"error": str(e)}), 404

    @app.route('/patients/<int:patient_id>', methods=['PUT'])
    def update(patient_id):
        data = request.json
        try:
            patient = update_patient(patient_id, data['name'], data['age'], data['disease'])
            return jsonify({"id": patient.id, "name": patient.name, "age": patient.age, "disease": patient.disease})
        except PatientNotFound as e:
            return jsonify({"error": str(e)}), 404

    @app.route('/patients/<int:patient_id>', methods=['DELETE'])
    def delete(patient_id):
        try:
            delete_patient(patient_id)
            return jsonify({"message": "Patient deleted successfully."})
        except PatientNotFound as e:
            return jsonify({"error": str(e)}), 404
