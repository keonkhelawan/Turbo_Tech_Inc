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