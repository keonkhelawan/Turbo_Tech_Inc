from main import app
from App.database import db
from App.models import Job, Course

# initialize jobs database
job_data = open('./App/job_files.csv')

# headings in file
job_heading_line = job_data.readline()

while True:
    jobData = job_data.readline()

    if not jobData:
        break

    jobInfo = jobData.split(",")
    
    job_list = Job(
                    id = jobInfo[0],
                    position = jobInfo[1],
                    competencies = jobInfo[2],
                    industry = jobInfo[3],
                    subCategory = jobInfo[4],
                    description = jobInfo[5]
                  )

    db.session.add(job_list)
    db.session.commit()              

job_data.close()


# initialize course database
course_data = open('./App/course_files.csv')

# headings in file
course_heading_line = course_data.readline()

while True:
    courseData = course_data.readline()

    if not courseData:
        break

    courseInfo = courseData.split(",")
    
    course_list = Course(
                    courseName = courseInfo[0],
                    courseCode = courseInfo[1],
                    competencyOutcome = courseInfo[2],
                    courseDescription = courseInfo[3]
                  )

    db.session.add(course_list)
    db.session.commit()

course_data.close()    