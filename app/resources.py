from flask_restx import Resource, Namespace

from .api_models import course_model, student_model, subject_model, student_input_model
from .extensions import db
from .models import Course, Student, Subject

ns = Namespace("RealUniversity")

@ns.route("/test")
class Test(Resource):
    def get(self):
        return{"Testing": "Server Active"}
    
@ns.route("/courses")
class CourseListAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

@ns.route("/courses/<int:id>")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        course = Course.query.get(id)
        return course
    
@ns.route("/students")
class StudentListAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def post(self):
        student = Student(name=ns.payload["name"], course_id=ns.payload["course_id"], year=ns.payload["year"], contact=ns.payload["contact"], email=ns.payload["email"])
        db.session.add(student)
        db.session.commit()
        return student, 201
    
@ns.route("/students/<int:id>")
class StudentAPI(Resource):
    @ns.marshal_with(student_model)
    def get(self, id):
        student = Student.query.get(id)
        return student
    
    
@ns.route("/subjects")
class SubjectListAPI(Resource):
    @ns.marshal_list_with(subject_model)
    def get(self):
        return Subject.query.all()

@ns.route("/subjects/<int:id>")
class SubjectAPI(Resource):
    @ns.marshal_with(subject_model)
    def get(self, id):
        subject = Subject.query.get(id)
        return subject
    


#@ns.route("/subjects/year/<string:year>/course/<string:course>")
#class SubjectAPI(Resource):
#    @ns.marshal_list_with(subject_model)
 #   def get(self, year, course):
 #       subject = Subject.query.filter_by(year, course)
 #       return subject