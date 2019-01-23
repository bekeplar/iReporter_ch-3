import unittest
from database.db import DatabaseConnection
from api import create_app
import json


class TestIntervention(unittest.TestCase):
    """class for testing intervention records"""
    def setUp(self):
        """
        Setting up a test client
        """
        self.db = DatabaseConnection()
        self.app = create_app('Testing')
        self.test_client = self.app.test_client()
        self.user = {
            "firstname": "bekelaze",
            "lastname": "Joseph",
            "othernames": "beka",
            "email": "bekeplar@gmail.com",
            "phoneNumber": "0789057968",
            "username": "bekeplar",
            "isAdmin": "False",
            "password": "bekeplar1234"
        }

        self.login_user = {
            'username': 'bekeplar',
            'password': 'bekeplar1234'
        }

        self.intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }
 
    def test_create_an_intervention(self):
        """
        Test if a user can create an intervention successfully.
        """
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(self.user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'], "bekeplar successfully registered.")
       
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        
        response = self.test_client.post(
            'api/v1/interventions',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        self.assertEqual(response.status_code, 201)

    def test_create_intervention_twice(self):
        """
        Test if a user can create an intervention twice successfully.
        """
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        self.assertEqual(response.status_code, 401)

    def test_create_intervention_unauthorised_user(self):
        """
        Test if a non user can create an intervention record successfully.
        """
        
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        self.assertEqual(response.status_code, 401)

    def test_create_intervention_no_token(self):
        """
        Test if a user can create a redflag successfully.
        """
        
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        self.assertEqual(response.status_code, 401)    

    def test_create_intervention_empty_createdBy(self):
        """
        Test if a user can create an intervention with missing createdBy.
        """
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        intervention = {
            "createdBy": "",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['Error'], 'Please fill in reporter field!')

    def test_create_intervention_empty_type(self):
        """
        Test if a user can be created with no type of incident.
        """
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )

        message = json.loads(response.data.decode())
        self.assertEqual(message['Error'], 'Please select incident type!')

    def test_create_intervention_empty_title(self):
        """
        check if a user can create an intervention with no title.
        """

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['Error'], 'Please fill in title field!')
        
    def test_create_intervention_empty_video(self):
        """
        check if a user can create an incident with no video.
        """
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": ""
            
        }
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )
        self.assertEqual(response.status_code, 406)

    def test_create_intervention_empty_images(self):
        """
        check if a user can create an intervention with no images.
        """
        
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "",
            "videos": "nn.mp4"
            
        }
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )
        self.assertEqual(response.status_code, 406)

    def test_create_intervention_no_location(self):
        """
        check if a user can create an intervention with no location.
        """

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "",
            "comment": "There are no drugs at Mukono Health center IV",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['Error'], 'Please fill in location field!')

    def test_create_intervention_no_comment(self):
        """
        check if a user can create an intervention with no comment.
        """

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        intervention = {
            "createdBy": "Bekalaze",
            "type": "intervention",
            "title": "insufficient drugs",
            "location": "1.33, 2.045",
            "comment": "",
            "status": "draft",
            "images": "nn.jpg",
            "videos": "nn.mp4"
        }

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(intervention)
        )

        message = json.loads(response.data.decode())
        self.assertEqual(message['Error'], 'Please fill in the comments field!')

    def test_get_all_intervention_records(self):
        """Test that a user can get all his created intervention records"""
        
        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        
        response = self.test_client.post(
            'api/v1/interventions',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        response = self.test_client.get(
            '/api/v1/interventions',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            content_type='application/json'

        )
        reply = json.loads(response.data.decode())
        self.assertEqual(reply['message'], 'These are your reports!')
        self.assertEqual(response.status_code, 200)

    def test_get_all_interventions_non_user(self):
        """Test that a non-user cannot get created records"""
        
        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        response = self.test_client.get(
            '/api/v1/interventions',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 401)
