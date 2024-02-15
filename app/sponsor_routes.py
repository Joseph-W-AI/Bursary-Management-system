# resources.py
from flask import request
from flask_restful import Resource
from models import db, StudentDetails, Bursary
from serializer import StudentDetailsSchema, BursarySchema
from marshmallow import ValidationError

class AddBursary(Resource):
    def post(self):
        schema = BursarySchema()
        try:
            data = schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        new_bursary = Bursary(**data)
        db.session.add(new_bursary)
        db.session.commit()
        return {"message": "Bursary added successfully."}, 201

class ViewApplications(Resource):
    def get(self, sponsor_id):
        schema = BursarySchema(many=True)
        applications = Bursary.query.filter_by(sponsor_id=sponsor_id)
        result = schema.dump(applications)
        return result, 200

class AwardBursary(Resource):
    def post(self, application_id):
        application = Bursary.query.get(application_id)
        if application:
            application.awarded = True
            db.session.commit()
            return {"message": "Bursary awarded successfully."}, 200
        return {"message": "Application not found."}, 404

class ViewStudents(Resource):
    def get(self):
        schema = StudentDetailsSchema(many=True)
        students = StudentDetails.query.all()
        result = schema.dump(students)
        return result, 200

class RejectRequest(Resource):
    def post(self, application_id):
        application = Bursary.query.get(application_id)
        if application:
            application.rejected = True
            db.session.commit()
            return {"message": "Request rejected successfully."}, 200
        return {"message": "Application not found."}, 404