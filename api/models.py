import datetime
import re


class User:
    users = []
    """ A class stores user object details """
    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.othernames = args[2]
        self.email = args[3]
        self.phoneNumber = args[4]
        self.username = args[5]
        self.registered = args[6]
        self.isAdmin = args[7]
        self.password = args[8]

    def create_user(self, username, password):
        for user in self.users:
            if user.username == None:
                self.users.append(user)

    def check_user_exist(self, email, username):
        for user in self.users:
            if self.username != None:
                return 'username already taken!'
            if self.email != None:
                return 'Email already has an account!'

    @staticmethod
    def validate_input(self):
        error = None
        if not self.firstname or self.firstname.isspace():
            error = 'Please fill in firstname field!'
        elif not self.lastname or self.lastname.isspace():
            error = 'Please fill in lastname field!'
        elif not self.othernames or self.othernames.isspace():
            error = 'Please fill in othernames field!'
        if not self.username or self.username.isspace():
            error = 'Please fill in username field!' 
        if not self.isAdmin or self.isAdmin.isspace():
            error = 'Please select user role!'    
        elif not self.email or self.email.isspace():
            error = 'Please fill in email field!'
        elif not self.phoneNumber or self.phoneNumber.isspace():
            error = 'Please fill in phoneNumber field!'
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", self.email):
            error = 'Please fill in right email format!.'
        elif not self.password or self.password.isspace():
            error = 'Plese fill in password field!'
        elif len(self.password) < 8:
            error = 'Password must be of 8 characters long!'
        return error     

    @staticmethod
    def login_validate(email, password):
        if not email or email.isspace():
            return 'Plese fill in email field!'
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return 'Please fill in right email format!.'   
        elif not password or password.isspace():
            return 'Plese fill in password field!'
        else:
            return None

    
class Incident:
    incidents = []
    """This class contains all incident objects"""

    def __init__(self, *args):
        self.id = args[0]
        self.createdBy = args[1]
        self.type = args[2]
        self.title = args[3]
        self.location = args[4]
        self.comment = args[5]
        self.status = args[6]
        self.createdOn = args[7]  

    def check_incident_exist(self, title):
        for incident in self.incidents:
            if incident.title != None:
                return 'Incident already reported!'

    def validate_input(self):
        error = None
        if not self.title or self.title.isspace():
            error ='Please fill in title field!'
        elif not self.location or self.location.isspace():
            error = 'Please fill in location field!'
        elif not self.type or self.type.isspace():
            error = 'Please select incident type!'
        elif not self.createdBy or self.createdBy.isspace():
            error = 'Please fill in reporter field!'
        elif not self.comment or self.comment.isspace():
            error = 'Please fill in the comments field!'
        elif not self.status or self.status.isspace():
            error = 'Please select draft as status!'
        return error

    def validate_del(self, id):
        if not id or id().isspace() or not isinstance(id, int):
                return 'Please enter an integer!'              

