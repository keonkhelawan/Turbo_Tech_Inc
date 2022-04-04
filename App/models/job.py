from App.database import db

class Job(db.Model):
  jobId = db.Column(db.Integer, primary_key=True)
  position = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(300), nullable=False)
  requirements = db.Column(db.String(200), nullable=False)
  industry = db.Column(db.String(100), nullable=False)
  subCategory = db.Column(db.String(100), nullable=False)

  def toDict(self):
    return{
      'Job Position': self.position,
      'Job Description': self.description,
      'Job Requirements': self.requirements,
      'Industry': self.industry,
      'Sub Category': self.subCategory
    }