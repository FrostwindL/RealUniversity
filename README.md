SIA101 Final output
Submitted by Team Stwopeed (Kalaw Darcy, Omana Carlo

RealUniversity Online Pre-Registration

The RealUniversity API allows users to submit pre registration and view available course subjects and registered students.

Base URL https:/RealUniversity
Authentication : none required for this API.

Endpoints
1. Get list of available Courses
    • URL: /courses
    • Method: GET
Example Response
{
	“id”: 0,
	“name”: “BSCS”;
	“fullname”: “Bachelor of Science in Computer Science”
}

2. Get specific Course
    • URL: /courses/{id}
    • Method: GET

3. Get list of available Subjects
    • URL: /subjects
    • Method: GET
Example Response
{
	“id”: 0,
	“name”: “GEC”;
	“description”: “Purposive Communication”
	“course”: [
	{
		“id”: 0,
		“name”: “BSCS”
		“fullname”: “Bachelor of Science in Computer Science”
	}
	“year”: “1st”
	“units”: “3”
}

4. Get specific Subject
    • URL: /subjects/{id}
    • Method: GET

5. Submit pre enrollement
    • URL: /students
    • Method: POST
Request Body
{
	“name”: “Lastname Firstname”;
	“course_id”: 0,
	“year”: “2nd”
	“contact”: “1234567890”
	“email”: “Enrolling_Student@gmail.com”
}

6. Get list of students
    • URL: /students
    • Method: GET
