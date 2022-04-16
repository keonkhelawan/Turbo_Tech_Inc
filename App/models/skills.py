from App.database import db

class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseCode = db.Column(db.String(20), nullable=False)
    courseSkills = db.Column(db.String(200), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def toDict(self):
        return{
        'course code': self.courseCode,
        'course skills': self.courseSkills
    }