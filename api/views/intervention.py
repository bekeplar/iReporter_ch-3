import json
from database.db import DatabaseConnection
from flask import request, Blueprint
from api.controllers.incident import IncidentController
from flask_jwt_extended import jwt_required
db = DatabaseConnection()

intervention_blueprint = Blueprint('intervention blueprint', __name__)

intervention_controller = IncidentController()


@intervention_blueprint.route('/interventions', methods=['POST'])
@jwt_required
def create_intervention():
    """
    Function that adds an intervention record incidents.
   
    """
    data = json.loads(request.data)
    return intervention_controller.create_new_incident(data, 'intervention')

@intervention_blueprint.route('/interventions', methods=['GET'])
@jwt_required
def get_all_interventions():
    """
    View function containing route for getting all intervention records.
    """

    return intervention_controller.fetch_all_incidents('interventions')

@intervention_blueprint.route('/interventions/<int:intervention_id>', methods=['GET'])
@jwt_required
def get_specific_intervention(intervention_id):
    """
    View function for getting a specific intervention from the report.
    """
    return intervention_controller.fetch_one_incident(intervention_id, 'intervention')
  

