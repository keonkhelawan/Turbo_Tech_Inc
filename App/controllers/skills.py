def make_skill_list(user_skills):
    split_skills = []
    skill_in_list = False
    
    for each in user_skills:
        each_skill = each.split("; ")
        
        for every in each_skill:
            for every_skill in split_skills:
                
                if(every_skill == every):
                    skill_in_list = True
                    
            if(skill_in_list):
                skill_in_list = False
            else:
                split_skills.append(every)
                skill_in_list = False
    
    return(split_skills)