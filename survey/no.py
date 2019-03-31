target = {'question': [a,b,c,d,e] }
    
                            dictionary rate   {'a':a ,'b':b , 'c':c ,'d':d 'e':e} 
            ['question_1': ['a',4],['b',6] ['c',2] ['d',3] ['e',5] ]
            
    rates = {}
    for question in questions :
        for answer in answers :
            if question.id answer.Question_id.id :
                        Rate answer.rate






 questions=Ask.objects.all()
    answers=  Ans.objects.all()
    names = []
    mydict = {'names' : names}    
    for question in questions :
        mylist = ['',0,0,0,0,0]
        mylist[0] = question.name
        names = question.name
        for answer in answers :
            if question.id == answer.Question_id.id :
                #could be for loop depends on integer neeed change at model
                if answer.rate == '1':
                    mylist[1] = mylist[1] + 1  
                    
                if answer.rate == '2':
                    mylist[2] = mylist[2] + 1  
                    
                if answer.rate == '3':
                    mylist[3] = mylist[3] + 1  
                    
                if answer.rate == '4':
                    mylist[4] = mylist[4] + 1  
                    
                if answer.rate == '5':
                    mylist[5] = mylist[5] + 1  
                    
        new = {mylist[0] : mylist}
        mydict.update({'names':names})
        mydict.update(new)

    context = mydict
    return HttpResponse(mydict['names'])




 questions=Ask.objects.all()
    answers=  Ans.objects.all()
    mydict = {}

    for question in questions :
        mylist = ['',0,0,0,0,0]
        mylist[0] = question.name
        for answer in answers :
            if question.id == answer.Question_id.id :
                #could be for loop depends on integer neeed change at model
                if answer.rate == '1':
                    mylist[1] = mylist[1] + 1  
                    break;
                if answer.rate == '2':
                    mylist[2] = mylist[2] + 1  
                    break;
                if answer.rate == '3':
                    mylist[3] = mylist[3] + 1  
                    break;
                if answer.rate == '4':
                    mylist[4] = mylist[4] + 1  
                    break;
                if answer.rate == '5':
                    mylist[5] = mylist[5] + 1  
                    break;
        new = {mylist[0] : mylist}
        mydict.update(new)

    context = mydict
    return HttpResponse(mydict)