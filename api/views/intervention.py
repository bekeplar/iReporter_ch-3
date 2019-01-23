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
