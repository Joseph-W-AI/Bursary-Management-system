from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from admin_routes import VerifyStudent, ApproveStudent, AwardScore, ViewAppliedBursaries
from sponsor_routes import AddBursary, ViewApplications, AwardBursary, ViewStudents, RejectRequest
from applicant_routes import SignUp, AddContactDetails, AddFamilyInformation, AddSiblingInformation, AddInstitutionInformation, AddPersonalDetails, AddDeclarations, AddEducationFundingHistory, ReceiveBursary
# Initialize Flask app
def create_app():
    app = Flask(__name__)
    api = Api(app) 
    from models import db  # Importing db from models

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bursary.db'  # Use your own database URI
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Use your own secret key

    # Initialize extensions
    db.init_app(app)  # Initializing db with the Flask app
    migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)
    CORS(app)

    # Import blueprints after initializing extensions to avoid circular import issues

    
    #from admin_routes import admin_bp
    #from sponsor_routes import sponsor_bp
    #from applicant_routes import applicant_bp
    # Register blueprints
    
    
    #app.register_blueprint(admin_bp)
    #admin_routes
    api.add_resource(VerifyStudent, '/verify-student/<int:student_id>')
    api.add_resource(ApproveStudent, '/approve-student/<int:student_id>')
    api.add_resource(AwardScore, '/award-score/<int:student_id>')
    api.add_resource(ViewAppliedBursaries, '/view_applied_bursaries')
    #sponsor_routes
    api.add_resource(AddBursary, '/add-bursary')
    api.add_resource(ViewApplications, '/view-applications/<int:sponsor_id>')
    api.add_resource(AwardBursary, '/award-bursary/<int:application_id>')
    api.add_resource(ViewStudents, '/view-students')
    api.add_resource(RejectRequest, '/reject-request/<int:application_id>')
    #applicant route
    api.add_resource(SignUp, '/sign-up')
    api.add_resource(AddContactDetails, '/add-contact-details/<int:user_id>')
    api.add_resource(AddFamilyInformation, '/add-family-information/<int:student_id>')
    api.add_resource(AddSiblingInformation, '/add-sibling-information/<int:student_id>')
    api.add_resource(AddInstitutionInformation, '/add-institution-information/<int:student_id>')
    api.add_resource(AddPersonalDetails, '/add-personal-details/<int:student_id>')
    api.add_resource(AddDeclarations, '/add-declarations/<int:student_id>')
    api.add_resource(AddEducationFundingHistory, '/add-education-funding-history/<int:student_id>')
    api.add_resource(ReceiveBursary, '/receive-bursary/<int:student_id>')

    return app 
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)