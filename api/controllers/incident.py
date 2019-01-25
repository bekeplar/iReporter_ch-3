# importing required dependencies
import datetime
import uuid
from database.db import DatabaseConnection
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from api.models.incident import Incident
db = DatabaseConnection()


class IncidentController:
    """
    Class containing all logic connecting incident views and models.
    """

    def create_new_incident(self, data, ireporter):
        """
        Method for creating a new incident record.
        """
        incident_id = uuid.uuid4()
        createdBy = data.get('createdBy')
        incident_type = data.get('type')
        title = data.get('title')
        location = data.get('location')
        comment = data.get('comment')
        status = 'draft'
        createdOn = datetime.datetime.utcnow()
        images = data.get('images')
        videos = data.get('videos')

        # view of an incident object/instance.
        incident = Incident(incident_id, createdBy, incident_type,
                            title, location, comment,
                            status, createdOn, images, videos)

        
        # Validating user's incident inputs
        error = incident.validate()
        exists = incident.check_incident_exist()
        if error is not None:
            return jsonify({'Error': error, 'status': 400}), 400
        # check if already existing incident record.
        if exists:
            return jsonify({
                'Error': f'{ireporter} record already reported!',
                'status': 406}), 406
        # create a new incident in the database of records
        db.insert_incident(incident_id, createdBy, incident_type,
                           title, location, comment,
                           status, createdOn, images, videos)

        print('after the database insert.. ')
        return jsonify({
            'status': 201,
            'message': f'created {ireporter} reccord!',
            'id': incident_id,
            'data': incident.__dict__
        }), 201

    def fetch_all_incidents(self, ireporter):
        """
        function to enable a user get all reported incidents
        :returns:
        The entire incidents reported by a user.
        """
        username = get_jwt_identity()
        all_incidents = db.fetch_all_incidents()
        # Verify that there are records in the database
        if not username and all_incidents:
            return jsonify({
                'satus': 400,
                'message': f'You haven/t reported any {ireporter}!',
                'data': all_incidents
            }), 400
        # Ruturning all existing incident type records.
        return jsonify({
            'status': 200,
            'data': all_incidents,
            'message': 'These are your reports!'
        }), 200

    def fetch_one_incident(self, incident_id, ireporter):
        """
        This method enables a registered
        user fetch a specific incident record.
        :params:
        :returns:
        For any given right id
        """
        try:
            get_one = db.fetch_incident(incident_id)
            if not get_one:
                return jsonify({
                    'status': 404,
                    'message': f'No such {ireporter} record found!'
                    }), 404
            return jsonify({
                'status': 404,
                'data': get_one,
                'message': f'{ireporter} record found succesfully.',
            }), 200
        except TypeError:
            return jsonify({
                'message': f'{ireporter} Id must be a number.'
                }), 400

    def delete_one_incident(self, incident_id, ireporter):
        """
        A method for deleting a specific incident from the report.
        """
        try:
            username = get_jwt_identity()
            get_one = db.fetch_incident(incident_id)

            if username and get_one:
                db.delete_incident(incident_id)
                return jsonify({
                    'message': f'{ireporter} record deleted succesfully.',
                    'data': get_one,
                    'status': 200
                }), 200
            else:
                return jsonify({
                    'message': f'No such {ireporter} record found!',
                    'status': 404
                }), 404
        except TypeError:
            return jsonify({'message': 'Only the reporter can delete this.',
                            'status': 401}), 401

    def update_status(self, incident_id, data, ireporter):
        """
        A method for updating status a specific incident from the report.
        """
        try:

            get_one = db.fetch_incident(incident_id)
            if get_one:
                db.update_status(incident_id, data)
                return jsonify({
                    'status': 200,
                    'data': db.fetch_incident(incident_id),
                    'message': f'{ireporter} status successfully updated!'
                }), 200
            else:
                return jsonify({'status': 404,
                                'message': f'No such {ireporter} record found!'
                                }), 404
        except ValueError:
            return jsonify({
                'status': 400,
                'message': 'Please provide right inputs'
            }), 400

    def update_location(self, incident_id, data, ireporter):
        """
        A method for updating location a specific incident from the report.
        """
        location = data.get('location')
        try:
            get_one = db.fetch_incident(incident_id)
            if get_one:
                db.update_location(incident_id, location)
                return jsonify({
                    'status': 200,
                    'data': db.fetch_incident(incident_id),
                    'message': f'{ireporter} location successfully updated!'
                }), 200
            else:
                return jsonify({
                    'status': 404,
                    'message': f'No such {ireporter} record found!'
                }), 404
        except ValueError:
            return jsonify({
                'message': 'Please provide right inputs'
            }), 400

    def update_comment(self, incident_id, data, ireporter):
        """
        A method for updating a comment of a specific incident from the report.
        """
        comment = data.get('comment')
        try:
            get_one = db.fetch_incident(incident_id)
            if get_one:
                db.update_comment(incident_id, comment)
                return jsonify({
                    'status': 200,
                    'data': db.fetch_incident(incident_id),
                    'message': f'{ireporter} comment successfully updated!'
                                }), 200
            else:
                return jsonify({'status': 404,
                                'message': f'No such {ireporter} record found!'
                                }), 404
        except ValueError:
            return jsonify({
                'status': 400,
                'message': 'Please provide right inputs'
            }), 400
# courtesy of bekeplar