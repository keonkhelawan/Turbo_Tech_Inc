def list_jobs(job_requirements, user_skills):
    
    list_of_jobs = job_requirements.split("; ")
    
    skill_found = False
    skills_count = 0
    jobs_count = len(list_of_jobs)
    
    for each_job in list_of_jobs:
        for each_skill in user_skills:
            
            if (each_skill == each_job):
                skill_found = True
                
        if (skill_found):
            skills_count = skills_count + 1
            skill_found = False
            
    if (skills_count == jobs_count):
        return ("qualified")
    else:
        return ("not qualified")