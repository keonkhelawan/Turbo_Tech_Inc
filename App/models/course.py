from App.database import db

class Course(db.Model):
    courseId = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(20), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def toDict(self):
        return {
            'course id': self.courseId,
            'course code': self.courseCode,
            'userid': self.userId,
        }