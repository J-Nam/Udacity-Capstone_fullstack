import os
from flask import Flask, request, abort, jsonify, render_template, send_from_directory, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json
import datetime
from six.moves.urllib.parse import urlencode
# importing models
from models import setup_db, db, Session, Institution, Musician

# importing auth
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    # routes
    # verifiation
    @app.route('/api/verification/<string:registerType>/<string:email>')
    @cross_origin(headers=['Content-Type','Authorization'])
    def verification(registerType, email):
        if registerType == "institution":
            try:
                inst = Institution.query.filter_by(email=email).all()
                if len(inst) == 0:
                    return {
                        "success": False
                    }
                else:
                    return {
                        "success": True
                    }
            except Exception:
                abort(404)
        else:
            try:
                musician = Musician.query.filter_by(email=email).all()
                if len(musician) == 0:
                    return {
                      "success": False
                    }
                else:
                    return {
                      "success": True
                    }
            except Exception:
                abort(404)

    # get
    @app.route('/api/sessions/<string:email>', methods=['GET'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('get:sessions')
    # get all sessions
    def get_sessions(payload, email):
        isInstitution = False
        try:
            sessions = Session.query.all()
            formatted_sessions = [s.format() for s in sessions]
            query = Institution.query.filter_by(email=email).all()
        except Exception:
            abort(404)
        if len(sessions) == 0:
            formatted_sessions == 'no data'
        if len(query) != 0:
            isInstitution = True
        else:
            try:
                query_m = Musician.query.filter_by(email=email).all()
                if len(query_m) == 0:
                    abort(404)
            except Exception:
                abort(404)
        return {
            "success": True,
            "sessions": formatted_sessions,
            "isInstitution": isInstitution
        }

    # get session info for update
    @app.route('/api/session/<int:session_id>', methods=['GET'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('get:sessions')
    def get_session(payload, session_id):
        try:
            session = Session.query.get(session_id)
            formatted_session = session.format()
        except Exception:
            abort(404)

        return {
            "success": True,
            "session": formatted_session
        }

    # get all institutions
    @app.route('/api/institutions', methods=['GET'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('get:institutions')
    def get_institutions(payload):
        try:
            institutions = Institution.query.all()
            formatted_institutions = [i.format() for i in institutions]
        except Exception:
            abort(404)

        if len(institutions) == 0:
            formatted_institutions = "no data"

        return {
            "success": True,
            "institutions": formatted_institutions
        }

    # get all musicians
    @app.route('/api/musicians', methods=['GET'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('get:musicians')
    def get_musicians(payload):
        try:
            musicians = Musician.query.all()
            formatted_musicians = [m.format() for m in musicians]
        except Exception:
            abort(404)

        if len(musicians) == 0:
            formatted_musicians = "no data"

        return {
            "success": True,
            "musicians": formatted_musicians
        }

    # post
    # add a new session
    @app.route('/api/sessions', methods=['POST'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('post:sessions')
    def create_sessions(payload):
        try:
            print('create sessions')
            formValue = request.data
            f_dict = json.loads(formValue)
            # unpack
            institution_email = f_dict['institution_email']
            location = f_dict['location']
            schedule = f_dict['schedule']
            title = f_dict['title']
            description = f_dict['description']
            imgURL = f_dict['imgURL']
            created_at = datetime.datetime.now()

            new_session = Session(
              institution_email=institution_email,
              title=title,
              description=description,
              location=location,
              schedule=schedule,
              imgURL=imgURL,
              created_at=created_at
            )
            new_session.insert()
            formatted_new_session = new_session.format()
        except Exception:
            abort(422)

        return {
            "success": True,
            "new_session": formatted_new_session
        }

    # add new institution
    @app.route('/api/institutions', methods=['POST'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('post:institutions')
    def create_institutions(payload):
        try:
            print('create institution')
            formValue = request.data
            f_dict = json.loads(formValue)
            # unpack
            name = f_dict['name']
            location = f_dict['location']
            email = f_dict['email']
            created_at = datetime.datetime.now()

            new_institution = Institution(
              name=name,
              location=location,
              email=email,
              created_at=created_at
            )
            new_institution.insert()

            formatted_new_institution = new_institution.format()

        except Exception:
            abort(422)

        return {
            "success": True,
            "new_institution": formatted_new_institution
        }

    # add new musician
    @app.route('/api/musicians', methods=['POST'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('post:musicians')
    def create_musicians(payload):
        try:
            print('create musicians')
            formValue = request.data
            f_dict = json.loads(formValue)
            # unpack
            name = f_dict['name']
            genre = f_dict['genre']
            instrument = f_dict['instrument']
            email = f_dict['email']
            created_at = datetime.datetime.now()

            new_musician = Musician(
              name=name,
              genre=genre,
              instrument=instrument,
              email=email,
              created_at=created_at
            )
            new_musician.insert()

            formatted_new_musician = new_musician.format()

        except Exception:
            abort(422)

        return {
            "success": True,
            "new_musician": formatted_new_musician
        }

    # delete
    @app.route("/api/sessions/<int:session_id>", methods=['DELETE'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('delete:sessions')
    def delete_session(payload, session_id):
        try:
            session = Session.query.get(session_id)
            session.delete()
        except Exception:
            abort(422)

        return {
            "success": True
        }

    # update
    @app.route("/api/sessions/<int:session_id>", methods=['PATCH'])
    @cross_origin(headers=['Content-Type','Authorization'])
    @requires_auth('patch:sessions')
    def update_session(payload, session_id):
        try:
            formValue = request.data
            f_dict = json.loads(formValue)
            # unpack
            location = f_dict['location']
            schedule = f_dict['schedule']
            title = f_dict['title']
            description = f_dict['description']
            imgURL = f_dict['imgURL']

            session = Session.query.get(session_id)
            session.location = location
            session.schedule = schedule
            session.title = title
            session.description = description
            session.imgURL = imgURL

            session.update()
        except Exception:
            abort(422)

        return {
            "success": True
        }

    # error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "page not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable_entity(e):
        return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable entity"
        }), 422

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({
          "success": False,
          "error": 500,
          "message": "server_error"
        }), 500

    @app.errorhandler(AuthError)
    def handle_auth_error(err):
        response = jsonify(err.error)
        response.status_code = err.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
