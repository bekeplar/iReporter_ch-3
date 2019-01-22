import datetime
from database.db import DatabaseConnection
from flask import jsonify
from api.validators.user import Validation
from api.models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
db = DatabaseConnection()


class UserController:
    """
    Class containing all logic connecting user views and models.
    """
    def create_user(self, data):
        """Method for creating a new user."""
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othernames = data.get('othernames')
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        username = data.get('username')
        registered = datetime.datetime.utcnow()
        isAdmin = data.get('isAdmin')
        password = data.get('password')
        
        # creating a user object
        user = User(firstname, lastname, othernames,
                    email, phoneNumber, username, 
                    registered, isAdmin, password
                    )
                
        # Validating user inputs
        error = Validation.validate_input(user)
        errors = Validation.validate_inputs(user)
        exists = user.check_user_exist()

        if error != None:
            return jsonify({'Error': error}), 400
        if errors != None:
            return jsonify({'Error': errors}), 400
        # check if user already registered
        if exists:
            return jsonify({
                'message':  'user already registered.',
                'status': 406
                }), 406
        password_hash = generate_password_hash(password, method='sha256')
        db.add_user(id, firstname, lastname,
                    othernames, email, password_hash,
                    username, registered, isAdmin)
        access_token = create_access_token(username)
        return jsonify({
            'status': 201,
            'token': access_token,
            'message': f'{username} successfully registered.',
            'user': user.__dict__
            }), 201

    def signin_user(self, data):
        """Method for signingin a known user."""
        username = data.get('username')
        password = data.get('password')

        # validating user input data
        error = Validation.login_validate(username, password)

        if error != None:
            return jsonify({'Error': error}), 400

        user = db.login(username)
        if user == None:
            return jsonify({'message': 'Wrong login credentials.'}), 400
        # checking for known user credentials
        if check_password_hash(user['password'], password) and user['username'] == username:
            access_token = create_access_token(username)
            return jsonify({
                'status': 200,
                'token': access_token,
                'message': f'{username} successfully logged in.'
            }), 200
        else:
            return jsonify({'message': 'Wrong login credentials.'}), 400


# courtesy of bekeplar.
        
