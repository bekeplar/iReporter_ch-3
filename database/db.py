import psycopg2
from psycopg2.extras import RealDictCursor
from pprint import pprint
import os
# from instance.config import DevelopmentConfig


class DatabaseConnection:
    """Class for all database operations."""

    def __init__(self):

        self.db_name = os.getenv('DB_NAME')

        try:
            self.connection = psycopg2.connect(
                dbname='postgres', host='localhost',
                password='bekeplar', port=5432,
                user='postgres'
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            self.dict_cursor = self.connection.cursor(
                cursor_factory=RealDictCursor)
            # pprint('Connected to the database')
            # pprint(self.db_name)

            create_user_table = """CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            othernames VARCHAR(50) NOT NULL,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            phoneNumber int,
            password TEXT NOT NULL,
            registered TEXT NOT NULL,
            isAdmin BOOL NOT NULL
                );"""

            create_Incidents_table = """CREATE TABLE IF NOT EXISTS incidents(
            id SERIAL NOT NULL PRIMARY KEY,
            createdBy VARCHAR(50) NOT NULL,
            incident_type VARCHAR(50) NOT NULL,
            title VARCHAR(50) NOT NULL,
            location VARCHAR(50) NOT NULL,
            comment VARCHAR(50) NOT NULL,
            status VARCHAR(50) NOT NULL,
            createdOn TEXT NOT NULL,
            images TEXT NOT NULL,
            videos TEXT NOT NULL
                );"""
            self.cursor.execute(create_Incidents_table)
            self.cursor.execute(create_user_table)

        except (Exception, psycopg2.DatabaseError) as error:
            pprint(error)

    def insert_incident(
        self, incident_id, createdBy,
        incident_type, title, location,
        comment, status, createdOn,
        images, videos
    ):
        """Method for adding a new incident record to incidents"""
        insert_incident = """INSERT INTO incidents(
           createdBy,
           incident_type,
           title,
           location,
           comment,
           status,
           createdOn,
           images,
           videos
            ) VALUES\
            ('{}', '{}','{}', '{}', '{}', '{}','{}', '{}', '{}')""".format(
            createdBy, incident_type,
            title, location, comment,
            status, createdOn,
            images, videos)
        pprint(insert_incident)
        self.dict_cursor.execute(insert_incident)

    def add_user(self, id, firstname, lastname,
                 othernames, email, password,
                 username, registered, isAdmin
                 ):
        """Method for adding a new user to users"""
        insert_user = """INSERT INTO users(
           firstname,
           lastname,
           othernames,
           email,
           password,
           username,
           registered,
           isAdmin
            ) VALUES('{}', '{}','{}', '{}', '{}', '{}','{}', '{}')""".format(
            firstname, lastname,
            othernames, email, password,
            username, registered, isAdmin)
        pprint(insert_user)
        self.dict_cursor.execute(insert_user)

    def check_username(self, username):
        """
        Check if a username already exists.
        """
        query = f"SELECT * FROM users WHERE username='{username}';"
        pprint(query)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def check_status(self, status):
        """
        Check if an incident status is  editable.
        """
        query = f"SELECT * FROM incidents WHERE status='{status}';"
        pprint(query)
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        return incident

    def check_title(self, title):
        """
        Check if a incident title already exists.
        """
        query = f"SELECT * FROM incidents WHERE title='{title}';"
        pprint(query)
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        return incident

    def check_comment(self, comment):
        """
        Check if an incident comment already exists.
        """
        query = f"SELECT * FROM incidents WHERE comment='{comment}';"
        pprint(query)
        self.cursor.execute(query)
        incident = self.cursor.fetchone()
        return incident

    def check_email(self, email):
        """
        Check if a email already exists.
        """
        query = f"SELECT * FROM users WHERE email='{email}';"
        pprint(query)
        self.dict_cursor.execute(query)
        user = self.dict_cursor.fetchone()
        return user

    def login(self, username):
        """Method to login an existing user"""
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        pprint(query)
        self.dict_cursor.execute(query)
        user = self.dict_cursor.fetchone()
        return user

    def user(self, username):
        """Returning a user id from database"""
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        pprint(query)
        self.dict_cursor.execute(query)
        user = self.dict_cursor.fetchone()
        return user

    def fetch_all_incidents(self):
        """Method to return all existing specified incident types"""
        query_all = "SELECT * FROM incidents;"
        pprint(query_all)
        self.dict_cursor.execute(query_all)
        incidents = self.dict_cursor.fetchall()
        return incidents

    def fetch_incident(self, id):
        """Method to return a given incident by its id."""
        query_one = "SELECT * FROM incidents WHERE id='{}'".format(id)
        pprint(query_one)
        self.dict_cursor.execute(query_one)
        incidents = self.dict_cursor.fetchone()
        return incidents

    def delete_incident(self, id):
        query = "DELETE FROM incidents  WHERE id='{}'".format(id)
        pprint(query)
        self.cursor.execute(query)

    def update_status(self, id, status):
        query = "UPDATE incidents SET status='{}' WHERE id='{}'".format(
            status, id)
        pprint(query)
        self.cursor.execute(query)

    def update_comment(self, id, comment):
        query = """UPDATE incidents SET comment='{}' WHERE id='{}'""".format(
            comment, id)
        pprint(query)
        self.dict_cursor.execute(query)

    def update_location(self, id, location):
        """Method to edit  an incident location."""
        query = """UPDATE incidents SET location='{}' WHERE id='{}'""".format(
            location, id)
        pprint(query)
        self.dict_cursor.execute(query)

    def create_admin(self, userId, admin):
        "Method to create an admin"
        query = """UPDATE  users SET admin='{}' WHERE userId='{}'""".format(
            True, userId)
        pprint(query)
        self.dict_cursor.execute(query)

    def drop_tables(self):
        drop = "DROP TABLE Incidents, users"
        pprint(drop)
        self.cursor.execute(drop)

    # if __name__ == '__main__':
    #     database_connection = DatabaseConnection()
# dbname = os.environ["DATABASE_URL"]
