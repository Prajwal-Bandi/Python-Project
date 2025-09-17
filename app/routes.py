"""
Flask routes and global error handlers for HMS.
"""

from flask import request, jsonify
from .crud import create_patient, get_patient, update_patient, delete_patient
from .emailer import send_email_background
from .exceptions import PatientNotFound


def init_routes(app):
    """Register all patient routes and error handlers."""
    
    @app.route("/patients", methods=["POST"])
    def create():
        data = request.json
        patient = create_patient(data["name"], data["age"], data["disease"])
        send_email_background(patient)
        return jsonify({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "disease": patient.disease
        }), 201

    @app.route("/patients/<int:patient_id>", methods=["GET"])
    def read(patient_id):
        patient = get_patient(patient_id)
        return jsonify({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "disease": patient.disease
        })

    @app.route("/patients/<int:patient_id>", methods=["PUT"])
    def update(patient_id):
        data = request.json
        patient = update_patient(patient_id, data["name"], data["age"], data["disease"])
        return jsonify({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "disease": patient.disease
        })

    @app.route("/patients/<int:patient_id>", methods=["DELETE"])
    def delete(patient_id):
        delete_patient(patient_id)
        return jsonify({"message": "Patient deleted successfully."})


    @app.errorhandler(PatientNotFound)
    def handle_patient_not_found(error):
        return jsonify({"error": str(error)}), 404

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        return jsonify({"error": "An unexpected error occurred"}), 500
