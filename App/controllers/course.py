def capital_letter(text_data):
    text_list = text_data.split(" ")
    new_letters = ""
    final_course = ""
    
    if (len(text_list) != 2):
        return ('error')
    elif ( (len(text_list[0]) != 4) or (len(text_list[1]) != 4) ):
        return ('error')
    else:
        for each in text_list[0]:
            if ( (ord(each) >= 97) and (ord(each) <= 122) ):
                each = ord(each) - 32
                new_letters = new_letters + (chr(each))
            else:
                new_letters = new_letters + each
               
            final_course = new_letters + " " + text_list[1]
            
        return (final_course)





def course_code_splitting(job_requirements, user_courses):
    
    # split job_requirements string
    split_courses = job_requirements.split("; ")
    
    # declare variables
    required_course_count = 0
    user_course_count = 0
    orToggle = False
    
    # iterate through each job requirement
    for each in split_courses:
        # add 1 for each required course in job_requirements(optional course requirements not affected)
        required_course_count = required_course_count + 1
        
        # split up optional job requirements for further comparisons
        optional_course = each.split(" or ")
        
        # iterate through each optional job requirement and compare all user courses
        for eachOption in optional_course:
            for every in user_courses:
                if (every == eachOption):
                    
                    # toggle "true" after any of the optinal job requirements are met
                    # this is used so that only 1 optional job requirement is catered for
                    if (orToggle == False):
                        user_course_count = user_course_count + 1
                        orToggle = True

        # toggle back to "false" so that each job requirement in "split_courses" is catered for 
        orToggle = False   
    

    if (required_course_count == user_course_count):
        return("qualified")
        
    else:
        return("not qualified")           