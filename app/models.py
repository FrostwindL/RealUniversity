from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    fullname = db.Column(db.String(50), unique=True)
    students = db.relationship("Student", back_populates="course")
    subjects = db.relationship("Subject", back_populates="course")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    course_id = db.Column(db.ForeignKey("course.id"))
    course = db.relationship("Course", back_populates="students")
    year = db.Column(db.String(3))
    contact = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    course_id = db.Column(db.ForeignKey("course.id"))
    course = db.relationship("Course")
    year = db.Column(db.String(3))
    units = db.Column(db.Integer)