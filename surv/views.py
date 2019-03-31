from django.shortcuts import render, redirect
from .models import Ask, Ans
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from collections import OrderedDict

from .fusioncharts import FusionCharts
import regex as re


# Create your views here.
def index(request):
    questions = Ask.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'index.html', context)


def test(request):
    questions = Ask.objects.all()
    Answers = Ans.objects.all()

    context = {
        'questions': questions,
        'answers': Answers
    }

    return render(request, 'test.html', context)


def testall(request):
    Answers = Ans.objects.all()

    context = {

        'answers': Answers
    }

    return render(request, "testall.html", context)


def ans(request):
    questions = Ask.objects.all()
    answers = Ans.objects.all()

    context = {
        'questions': questions,
        'answers': answers
    }
    return render(request, 'Ans.html', context)


def login_check(request):
    if request.user.is_superuser == 0:
       #   return HttpResponse(request.user.is_superuser)
        return redirect('ans')


    else:
      #  return HttpResponse(request.user.is_superuser)

        # return HttpResponse("admin page")
        return index(request)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('ans')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/registration.html', context)


def create(request):
    print(request.POST)
    title = request.GET['name']
    content = request.GET['content']
    question_details = Ask(name=title, content=content, is_visible=True)
    question_details.save()
    return redirect('/myadmin')


def add_question(request):
    return render(request, 'add_question.html')


def delete(request, id):
    questions = Ask.objects.get(pk=id)
    questions.is_visible = False
    questions.save()
    return redirect('/myadmin')


def answer(request):
    rate = int(request.POST.get('rate'))
    user_id = int(request.POST.get('user_id'))
    user = User.objects.get(pk=user_id)
    question_id = int(request.POST.get('question_id'))
    question = Ask.objects.get(pk=question_id)
    done = True
    user_answer = Ans(user_id=user, done=done, rate=rate, Question_id=question)
    user_answer.save()

    return redirect('ans')


def group(request):
    questions = Ask.objects.all()
    answers = Ans.objects.all()
    mydict = {}
    for question in questions:
        mylist = ['', 0, 0, 0, 0, 0, '', 0.0]
        for answer in answers:
            if question.id == answer.Question_id.id:
                mylist[0] = question.name
                mylist[6] = question.content
                # could be for loop depends on integer neeed change at model
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
        if mylist[0] != '':
            key = mylist[0]
            # del mylist[0]
            avg = mylist[1:6]
            sum = 0
            for i in range(5):
                sum = sum + mylist[i + 1] * i + 1
            if sum / 5 > 5:
                mylist[7] = 5;
            else:
                mylist[7] = sum / 5
            new = {key: mylist}
            mydict.update(new)

    context = {
        'questions': questions,
        'mydict': mydict
    }

    return render(request, 'test.html', context)
    # return HttpResponse(mydict)


def count(request):
    questions = Ask.objects.all()
    answers = Ans.objects.all()
    content = {}
    for question in questions:
        # could be for loop depends on integer neeed change at model
        anscount = Ans.objects.filter(Question_id=question.id).count()

        if anscount != 0:
            ques = question.name

        content.update({ques: anscount})

    context = {
        'mydict': content
    }
    return render(request, 'group.html', context)


def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            # The data is passed as a string in the `dataSource` as parameter.
                            """{  
                                   "chart": {  
                                      "caption":"Harry\'s SuperMart",
                                      "subCaption":"Top 5 stores in last month by revenue",
                                      "numberPrefix":"$",
                                      "theme":"ocean"
                                   },
                                   "data": [  
                                        {"label":"Bakersfield Central", "value":"880000"},
                                        {"label":"Garden Groove harbour", "value":"730000"},
                                        {"label":"Los Angeles Topanga", "value":"590000"},
                                        {"label":"Compton-Rancho Dom", "value":"520000"},
                                        {"label":"Daly City Serramonte", "value":"330000"}
                                    ]
                                }""")

    # returning complete JavaScript and HTML code,
    # which is used to generate chart in the browsers.
    return render(request, 'chart.html', {'output': column2d.render()})


def home(request):
    return render(request, 'home.html')





def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    chartData["Venezuela"] = 290
    chartData["Saudi"] = 260
    chartData["Canada"] = 180
    chartData["Iran"] = 140
    chartData["Russia"] = 115
    chartData["UAE"] = 100
    chartData["US"] = 30
    chartData["China"] = 30

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", dataSource)
    fff = {'k': {1: {'output': column2D.render(), 'chartTitle': 'Simple Chart Using Array'},
                 2: {'output': column2D.render(), 'chartTitle': 'Simple Chart Using Array'},
                 'range': [1, 2]
                 }
           }
    return render(request, 'charts.html', fff)







