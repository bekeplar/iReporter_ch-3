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
        self.assertEqual(message['message'],
                         "bekeplar successfully registered.")

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
        self.assertEqual(message['Error'],
                         'Please fill in the comments field!')

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
        """Test that a non-user cannot get created records
        """

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

    def test_get_specific_intervention_not_existing(self):
        """Test that a user cannot get a non existing intervention record"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        response = self.test_client.get(
            '/api/v1/interventions/1'
        )
        self.assertEqual(response.status_code, 401)

    def test_get_specific_incident_from_empty_list(self):
        """Test that a user cannot get an intervention from empty list"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        response = self.test_client.get(
            '/api/v1/interventions/1',
            headers={'Authorization': 'Bearer ' + access_token['token']}
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_intervention(self):
        """Test that a user can delete a specific created intervention"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        response = self.test_client.delete(
            '/api/v1/interventions/1',
            headers={'Authorization': 'Bearer ' + access_token['token']}
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_intervntion_not_in_list(self):
        """Test that a user cannot delete non existing"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/intervention',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        response = self.test_client.delete(
            '/api/v1/interventions/1000',
            headers={'Authorization': 'Bearer ' + access_token['token']}
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_specific_intrvention_unauthorized(self):
        """Test that a non user cannot delete an intervention record"""

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            data=json.dumps(self.intervention)
        )
        response = self.test_client.delete(
            '/api/v1/interventions/2',
        )
        self.assertEqual(response.status_code, 401)

    def test_update_location_specific_intervention(self):
        """Test that a user can update location of an intervention"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        new_location = {

            "location": "1.784, 4.0987"
        }

        response = self.test_client.patch(
            'api/v1/interventions/2/location',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(new_location)
        )
        self.assertEqual(response.status_code, 200)

    def test_update_location_specific_intervention_not_in_list(self):
        """Test that a user cannot update non existing intervention"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        new_location = {

            "location": "1.784, 4.0987"
        }
        response = self.test_client.patch(
            'api/v1/interventions/1/location',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(new_location)
        )
        self.assertEqual(response.status_code, 404)

    def test_update_status_of_intervention(self):
        """Test that a user can update comment of an intervention record"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        new_status = {
            "status": "resolved"
        }

        response = self.test_client.patch(
            'api/v1/interventions/2/status',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(new_status)
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(reply['message'],
                         'intervention status successfully updated!')
        self.assertEqual(response.status_code, 200)

    def test_edit_status_not_in_list(self):
        """Test that a user cannot update status for non existing incident"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        new_location = {
            "status": "resolved"
        }

        response = self.test_client.patch(
            'api/v1/interventions/10000/status',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(new_location)
        )
        self.assertEqual(response.status_code, 404)

    def test_edit_comment_not_existing(self):
        """Test that a user cannot update comment for non existing incident"""

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        new_location = {
            "comment": "Nurses stock drugs in their drugshops"
        }

        response = self.test_client.patch(
            'api/v1/interventions/10000/comment',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(new_location)
        )
        self.assertEqual(response.status_code, 404)

    def test_update_comment_specific_intervention(self):
        """Test that a user can update comment
           of a specific created intervention
        """

        response = self.test_client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(self.login_user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        response = self.test_client.post(
            'api/v1/interventions',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(self.intervention)
        )
        updated_comment = {
            "comment": "Nurses stock drugs in their drugshops"
        }

        response = self.test_client.patch(
            'api/v1/interventions/2/comment',
            content_type='application/json',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            data=json.dumps(updated_comment)
        )
        self.assertEqual(response.status_code, 200)
