from App.database import db

class course(db.Model):
    courseId = db.column(db.Integer, primary_key=True)
    courseCode = db.column(db.String(20), nullable=False)
    userId = db.column(db.Integer, db.ForeignKey('user.id'), nullable=False)