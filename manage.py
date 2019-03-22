#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


    







def group(request):
    questions=Ask.objects.all()
    answers=  Ans.objects.all()
    content = []
    for question in questions :
        mylist = ['','',0,0,0,0,0]
        mylist[0] = question.name
        mylist[1] = question.content
        for answer in answers :
            if question.id == answer.Question_id.id :
                #could be for loop depends on integer neeed change at model
                if answer.rate == '1':
                    mylist[2] = mylist[2] + 1  
                    
                if answer.rate == '2':
                    mylist[3] = mylist[3] + 1  
                    
                if answer.rate == '3':
                    mylist[4] = mylist[4] + 1  
                    
                if answer.rate == '4':
                    mylist[5] = mylist[5] + 1  
                    
                if answer.rate == '5':
                    mylist[6] = mylist[6] + 1 
        content.append(mylist)

    context = {'data': content}
    return render(request,'test.html',context)



