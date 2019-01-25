from database.db import DatabaseConnection

db = DatabaseConnection()


class Incident:
    """This class contains all incident objects"""

    def __init__(self, *args):
        self.incident_id = args[0]
        self.createdBy = args[1]
        self.incident_type = args[2]
        self.title = args[3]
        self.location = args[4]
        self.comment = args[5]
        self.status = args[6]
        self.createdOn = args[7]
        self.images = args[8]
        self.videos = args[9]

    def check_incident_exist(self):
        """Function to check whether an incident already exists."""
        title = db.check_title(self.title)
        comment = db.check_comment(self.comment)
        if title:
            return 'Title already reported.'
        if comment:
            return 'comment already reported.'

    def validate(self):
        """Method for validating user data"""
        if self.title.isspace() or not self.title:
            return 'Please fill in title field!'
        elif self.location.isspace() or not self.location:
            return 'Please fill in location field!'
        elif self.incident_type.isspace() or not self.incident_type:
            return 'Please select incident type!'
        elif self.comment.isspace() or not self.comment:
            return 'Please fill in the comments field!'
        elif self.incident_type.isspace() or not self.incident_type:
            return 'Please select incident type!'
        else: 
            return None


