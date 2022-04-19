from App.database import db

class Job(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  position = db.Column(db.String(100), nullable=False)
  competencies = db.Column(db.String(200), nullable=False)
  industry = db.Column(db.String(100), nullable=False)
  subCategory = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(300), nullable=False)

  def toDict(self):
    return{
      'Job Position': self.position,
      'competencies': self.competencies,
      'industry': self.industry,
      'Sub Category': self.subCategory,
      'Job Description': self.description
    }