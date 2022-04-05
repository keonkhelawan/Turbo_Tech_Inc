from main import app
from App.database import db
from App.models import Job

data = open('./App/jobs.txt')

# headings
line = data.readline()

while True:
    jobData = data.readline()

    if not jobData:
        break

    jobInfo = jobData.split(",")
    
    job_list = Job(
                    jobId = jobInfo[0],
                    position = jobInfo[1],
                    description = jobInfo[5],
                    requirements = jobInfo[2],
                    industry = jobInfo[3],
                    subCategory = jobInfo[4]
                  )

    db.session.add(job_list)
    db.session.commit()              
