import os
import unittest
import json
import datetime
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_test_db, db, session, institution, musician
from dotenv import load_dotenv

load_dotenv()

# import env variable
inst_jwt = os.environ.get('inst_jwt')
if not inst_jwt:
    inst_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNabi1XMmNwNDBBTEh5Z1ctWnloVCJ9.eyJpc3MiOiJodHRwczovL2ZpbmR5b3VyamFtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDQ1ZTdiNmI4NDU4NjAwNjkzYTUxOGMiLCJhdWQiOlsiamFtc2Vzc2lvbnMiLCJodHRwczovL2ZpbmR5b3VyamFtLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTUxOTY1OTEsImV4cCI6MTYxNTI4Mjk5MSwiYXpwIjoibkxaeUdEWHNyVG9XWDJ4c0hyTW9BaXhlS1N0V1VEakQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmluc3RpdHV0aW9ucyIsImRlbGV0ZTpzZXNzaW9ucyIsImdldDppbnN0aXR1dGlvbnMiLCJnZXQ6bXVzaWNpYW5zIiwiZ2V0OnNlc3Npb25zIiwicGF0Y2g6aW5zdGl0dXRpb25zIiwicGF0Y2g6c2Vzc2lvbnMiLCJwb3N0Omluc3RpdHV0aW9ucyIsInBvc3Q6c2Vzc2lvbnMiXX0.bzI9Gdnn8TMDTDfNuRfktYg40oAhQ-uY3rzM9Pl2WiDzUog9QgYY8VSDMftM9n5mAlLQ-dc5g2oLI4xDa96TM4cBmqWM2eqQJJtDq58rQayDFGJ4K7VB63MaWfDDkj6S5YmfIrwus5JJmJ3xlQu8HhZOVm7bh0W_4Vi1pdKCfXvU8lLpThI560i1lndFKmz9z4RNPEQy7UJR91zeru4MueCh8SV95fcdvN21-bPLi8s1ItYk_wXZxs6oGwVfwqcBhtoURUiZIxdV4B4IA4Ki77r8JxNrWXzbXMkI_zPCa_xKPdRNeOO-dzyNyB4pUBBK6ri9mYbX83DQNBWNc1ECfA"

musician_jwt = os.environ.get('musician_jwt')
if not musician_jwt:
    musician_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNabi1XMmNwNDBBTEh5Z1ctWnloVCJ9.eyJpc3MiOiJodHRwczovL2ZpbmR5b3VyamFtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDQ1ZWEyZDM1MTlkOTAwNjhmODYwMmEiLCJhdWQiOlsiamFtc2Vzc2lvbnMiLCJodHRwczovL2ZpbmR5b3VyamFtLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTUxOTY2NzUsImV4cCI6MTYxNTI4MzA3NSwiYXpwIjoibkxaeUdEWHNyVG9XWDJ4c0hyTW9BaXhlS1N0V1VEakQiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOm11c2ljaWFucyIsImdldDppbnN0aXR1dGlvbnMiLCJnZXQ6bXVzaWNpYW5zIiwiZ2V0OnNlc3Npb25zIiwicGF0Y2g6bXVzaWNpYW5zIiwicG9zdDptdXNpY2lhbnMiXX0.bWP1GbjNTx8mvIbM9XgrI9xIcBz2WswCJ7LmHNJkB0J71FGm4kHfoTXFAZpr7IzLrbA2Mklc5Syq73YYkXbn0UPqC0mVSZRRbl1pHP27owmIs55wQRtpPRTgJm2Eb37YiVx3oYxX1fXKVmlhkwlRH3HpqkpW40z634-V7QyPbMeNoW4E3fTInIZrTl-eWluIIy5X2hH8MDDUZQiLJBGitwFHHIQdKIC9Ly-iA5rEMdZXDWN4IAPrfxX7av3XX8D6h4ZzdHWDx8gmt9mYW0QkRWCRUeSTcbFbDxywyDq56DQghxQYI7541x-G38-g8UvyYyX3u_BsE7Z25C0_kxXUFw"

# get jwt token for authorization
def get_headers(token):
    return {'Authorization': f'Bearer {token}'}

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Define test variables and initialize app
        self.app = create_app()
        self.client = self.app.test_client

        setup_test_db(self.app)
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # drop all existing table
            self.db.drop_all()
            # create all tables
            self.db.create_all()
            # seed data
            self.db.session.add(session)
            self.db.session.add(institution)
            self.db.session.add(musician)
            self.db.session.commit()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # successful/fail tests for each endpoint
    # get route
    # get sessions
    def test_get_sessions(self):
        res = self.client().get('/api/sessions/inst@email.com',
        headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['sessions'])
        self.assertTrue(data['isInstitution'])

    def test_404_get_sessions_failed(self):
        res = self.client().get('/api/sessions/fakeEmail',
        headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')

    # auth test
    def test_get_sessions_auth_failed(self):
        res = self.client().get('/api/sessions/inst@email.com')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

    # get session info
    def test_get_session_info(self):
        res = self.client().get('/api/session/2', headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['session'])

    def test_404_session_info_failed(self):
        res = self.client().get('/api/session/1000', headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')

    # get institutions
    def test_get_institutions(self):
        res = self.client().get('/api/institutions',
        headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['institutions'])

    def test_get_institutions_auth_failed(self):
        res = self.client().get('/api/institutions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

    # get musicians
    def test_get_musicians(self):
        res = self.client().get('/api/musicians',
        headers=get_headers(musician_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['musicians'])

    def test_get_musicians_auth_failed(self):
        res = self.client().get('/api/musicians')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

    # post route
    # add session
    def test_add_session(self):
        res = self.client().post('/api/sessions',
            json={
                'institution_email': 'inst@email.com',
                'title': 'new session',
                'description': 'something about a new session...',
                'location': 'Montreal, QC, CA',
                'schedule': '2022-02-25 18:00:00',
                'imgURL': ''
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_session'])

    def test_422_add_session_failed(self):
        res = self.client().post('/api/sessions',
            json={
                'institution_email': 'inst@email.com',
                'title': 'new session',
                'description': 'something about a new session...'
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    #auth test
    def test_add_session_auth_failed(self):
        res = self.client().post('/api/sessions',
            json={
                'institution_email': 'inst@email.com',
                'title': 'new session',
                'description': 'something about a new session...',
                'location': 'Montreal, QC, CA',
                'schedule': '2022-02-25 18:00:00',
                'imgURL': ''
            },
            headers=get_headers(musician_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    # add institution
    def test_add_institution(self):
        res = self.client().post('/api/institutions',
            json={
                'name': 'new institution',
                'location': 'Toronto, ON, CA',
                'email': 'inst2@email.com'
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_institution'])

    def test_404_add_institution_failed(self):
        res = self.client().post('/api/institutions/200',
            json={
                'name': 'new institution',
                'location': 'Toronto, ON, CA',
                'email': 'inst2@email.com'
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')

    # add musician
    def test_add_musician(self):
        res = self.client().post('/api/musicians',
            json={
                'name': 'new musician',
                'genre': 'Jazz',
                'instrument': 'Trumpet',
                'email': 'musician2@email.com'
            },
            headers=get_headers(musician_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_musician'])

    def test_404_add_musician_failed(self):
        res = self.client().post('/api/musicians/200',
            json={
                'name': 'new musician',
                'genre': 'Jazz',
                'instrument': 'Trumpet',
                'email': 'musician2@email.com'
            },
            headers=get_headers(musician_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'page not found')

    # patch
    # update session
    def test_update_session(self):
        res = self.client().patch('/api/sessions/2',
            json={
                'institution_email': 'inst@email.com',
                'title': 'updated session title',
                'description': 'updated description...',
                'location': 'Montreal, QC, CA',
                'schedule': '2022-02-25 18:00:00',
                'imgURL': ''
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_update_session_failed(self):
        res = self.client().patch('/api/sessions/2000',
            json={
                'institution_email': 'inst@email.com',
                'title': 'updated session title',
                'description': 'updated description...',
                'location': 'Montreal, QC, CA',
                'schedule': '2022-02-25 18:00:00',
                'imgURL': ''
            },
            headers=get_headers(inst_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    # auth test
    def test_update_session_auth_failed(self):
        res = self.client().patch('/api/sessions/1',
            json={
                'institution_email': 'inst@email.com',
                'title': 'updated session title',
                'description': 'updated description...',
                'location': 'Montreal, QC, CA',
                'schedule': '2022-02-25 18:00:00',
                'imgURL': ''
            },
            headers=get_headers(musician_jwt)
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    # delete route
    def test_delete_session(self):
        res = self.client().delete('/api/sessions/1',
        headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_delete_session_failed(self):
        res = self.client().delete('/api/sessions/1000',
        headers=get_headers(inst_jwt))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable entity')

    # auth test
    def test_delete_session_auth_failed(self):
        res = self.client().delete('/api/sessions/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
