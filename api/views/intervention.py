import json
from database.db import DatabaseConnection
from flask import request, Blueprint
from api.controllers.incident import IncidentController
from flask_jwt_extended import jwt_required, get_jwt_identity
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
    return intervention_controller.create_new_incident(data,
                                                       'intervention')


@intervention_blueprint.route('/interventions', methods=['GET'])
@jwt_required
def get_all_interventions():
    """
    View function containing route for getting all intervention records.
    """

    return intervention_controller.fetch_all_incidents('interventions')


@intervention_blueprint.route('/interventions/<int:intervention_id>',
                              methods=['GET'])
@jwt_required
def get_specific_intervention(intervention_id):
    """
    View function for getting a specific intervention from the report.
    """
    return intervention_controller.fetch_one_incident(intervention_id,
                                                      'intervention')


@intervention_blueprint.route('/interventions/<int:intervention_id>',
                              methods=['DELETE']
                              )
@jwt_required
def delete_specific_redflag(intervention_id):
    """
    View function with route for getting a specific redflag from the report.
    """
    return intervention_controller.delete_one_incident(intervention_id,
                                                       'intervention')


@intervention_blueprint.route('/interventions/<int:intervention_id>/location',
                              methods=['PATCH']
                              )
@jwt_required
def edit_location_of_intervention(intervention_id):
    """
    Function wirh a route for editing an intervention's location.
    """
    data = json.loads(request.data)
    return intervention_controller.update_location(intervention_id,
                                                   data, 'intervention'
                                                   )


@intervention_blueprint.route('/interventions/<int:intervention_id>/status',
                              methods=['PATCH'])
@jwt_required
def edit_intervention_status(intervention_id):
    """
    Function for editing an intervention's status.
    """
    data = request.get_json()['status']
    return intervention_controller.update_status(intervention_id, data,
                                                 'intervention')


@intervention_blueprint.route('/interventions/<int:intervention_id>/comment',
                              methods=['PATCH']
                              )
@jwt_required
def edit_intervention_comment(intervention_id):
    """
    Function wirh a route for editing an intervention's comment.
    """
    data = json.loads(request.data)
    return intervention_controller.update_comment(intervention_id, data,
                                                  'intervention')
# courtesy of bekeplar
