from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


 
def index(request):
    return render(request, 'polls/index.html')
     
def add(request):
    if request.GET:
        a = request.GET['a']
        b = request.GET['b']
        print(request)
        print(request.GET.get('a'))
        a = int(a)
        b = int(b)

        print(1111111111)
        sum = str(a+b)
        print(sum)

    if request.POST:
        print(22222222222222)
        print(request.POST)
        print(request.POST.get('a'))   #两种获取按钮值的方法
        print(request.POST.get('b'))
        print(request.POST['a'])
        print(request.POST['b'])
        sum=1
    return HttpResponse(sum)

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)