from flask import Flask, jsonify
import datetime
from instance.config import app_config
from api.views.redflag import blueprint
from api.views.intervention import intervention_blueprint
from api.views.user import user_blueprint
from flask_jwt_extended import JWTManager


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_SECRET_KEY'] = 'undertakenby!'
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['JWT_SECRET_KEY']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)
    JWTManager(app)

    #  Register blueprints
    app.register_blueprint(blueprint, url_prefix='/api/v1')
    app.register_blueprint(user_blueprint, url_prefix='/api/v1')
    app.register_blueprint(intervention_blueprint, url_prefix='/api/v1')

    valid_urls = [
            "GET /api/v1/",
            "POST /api/v1/auth/signup",
            "POST /api/v1/auth/login",
            "GET /api/v1/redflags",
            "POST /api/v1/redflags",
            "POST /api/v1/interventions",
            "GET /api/v1/interventions",
            "GET /api/v1 /redflags/<int:redflag_id>",
            "PATCH /api/v1/redflags/<int:redflag_id>/location",
            "PATCH /api/v1/redflags/<int:redflag_id>/status",
            "PATCH /api/v1/redflags/<int:redflag_id>/comment",
            "DELETE /api/v1/redflags/<int:redflag_id>",
            "GET /api/v1 /interventions/<int:intervention_id>",
            "PATCH /api/v1/intervention/<int:intervention_id>/location",
            "PATCH /api/v1/interventions/<int:intervention_id>/status",
            "PATCH /api/v1/interventions/<int:intervention_id>/comment",
            "DELETE /api/v1/interventions/<int:intervention_id>"
        ]

    @app.errorhandler(Exception)
    def errors(error):
        """
        This funcion handles the 404 and 405 HTTP STATUS CODES.
        """
        response = None
        if error == 404:
            response = jsonify({
                'Issue': 'You have entered an unknown URL.',
                'Valid URLs': valid_urls,
                'status': 404,
                'message': 'Please contact Admin for more details on this API.'
            }), 404
        else:
            response = jsonify({
                'status': 405,
                'error': 'Method Not Allowed.',
                'Supported Methods': valid_urls,
                'message': 'Please follow this guide for details on this API.'
            }), 405
        return response

    return app
