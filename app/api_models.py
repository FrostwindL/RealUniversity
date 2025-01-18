from flask_restx import fields
from .extensions import api

student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String,
    "course": fields.String,
    "year": fields.String,
    "contact": fields.String,
    "email": fields.String
})

course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
    "fullname": fields.String
})

subject_model = api.model("Subject", {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "course": fields.List(fields.Nested(course_model)),
    "year": fields.String,
    "units": fields.String
})

student_input_model = api.model("StudentInput",{
    "name": fields.String,
    "course_id": fields.Integer,
    "year": fields.String,
    "contact": fields.String,
    "email": fields.String
})