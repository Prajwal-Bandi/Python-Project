from flask import jsonify
from .exceptions import PatientNotFound

def init_routes(app):
    # ... your routes

    @app.errorhandler(PatientNotFound)
    def handle_not_found(error):
        response = jsonify({"error": str(error)})
        response.status_code = 404
        return response
