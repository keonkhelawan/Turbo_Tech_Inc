from App.database import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    courseCode = db.Column(db.String(20), nullable=False)
    competencyOutcome = db.Column(db.String(200), nullable=False)
    courseDescription = db.Column(db.String(300), nullable=False)
    

    def toDict(self):
        return {
            'course name': self.courseName,
            'course code': self.courseCode,
            'competency Outcome': self.competencyOutcome,
            'course description': self.courseDescription
        }