from flask import jsonify
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from setup_db import db

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        result = directors_schema.dump(all_directors)
        return result, 200

@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did:int):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200

        except Exception as e:
            return str(e), 404

@director_ns.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@director_ns.route('/test_db', methods=['GET'])
def test_db():
    result = db.session.execute(
        '''
        SELECT 1;
        '''
    ).scalar()
    return jsonify({'result': result})
