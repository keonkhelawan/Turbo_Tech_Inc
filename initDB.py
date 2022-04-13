from main import app
from App.database import db
from App.models import Job

data = open('./App/job_files.csv')

# headings in file
line = data.readline()

while True:
    jobData = data.readline()

    if not jobData:
        break

    jobInfo = jobData.split(",")
    
    job_list = Job(
                    jobId = jobInfo[0],
                    position = jobInfo[1],
                    industry = jobInfo[3],
                    subCategory = jobInfo[4],
                    requirements = jobInfo[2],
                    description = jobInfo[5]
                    
                    
                  )

    db.session.add(job_list)
    db.session.commit()              
