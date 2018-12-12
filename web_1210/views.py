from django.http import HttpResponse
from django.shortcuts import render

def root(request):
    name = request.GET.get('name', 'guest')
    return HttpResponse('Hi!{}'.format(name))

def hello(request, name):
    return HttpResponse('Hi,{}'.format(name))

def s(request, number):
    return HttpResponse(number ** 2)

def l(request, number1, number2):
    # if number1 >= number2:
    #     _list = reversed(range(number2, number1+1))
    # else:
    #     _list = range(number1, number2+1)

    #_list = range(10, 0, -1) 由大到小排列 
    if number1 >number2:
        step = -1
    else:
        step = 1   
    # step = -1 if number > number2 else 1
    _list = range(number1, number2+step, step)
    return render(request, 'l.html', {'list': _list})
