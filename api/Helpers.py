from api.models import users, incidents


def get_user(current_user):
    """function returns data attached to the current user """
    for user in users:
        if user['email'] == current_user:
            return user

 
def check_is_admin(current_user):
    """function checks if a user is an admin """
    return current_user['isAdmin']  


def create_user(username, password):
    """function to create a new user. """
    for user in users:
        if user.username == None:
            users.append(user)


def login_user(email):
    """function that allows a known user login """
    for user in users:
        if user.email == user['email']:
            return user['username']
    return {"message": "user doesn't exist"}


def check_user_exist(email, username):
    for user in users:
        if username != None:
            return 'username already taken!'
        if email != None:
            return 'Email already has an account!'


def check_incident_exist(title):
    for redflag in incidents:
        if redflag.title != None:
            return 'Incident already reported!'


