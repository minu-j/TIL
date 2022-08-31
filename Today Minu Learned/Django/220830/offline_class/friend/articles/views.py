import imp
from multiprocessing import context
from operator import truediv
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    print('인대리!')
    nums = [1, 5, 32, 54, 5, 6, 324, 384, 55, 45, 6]
    foods = ['피자', '피킨', '햄버거']
    pick = random.choice(nums)

    context = {
        'name' : 'alex',
        'foods' : foods,
        'address' : {
            'city' : 'seoul'
        },
        'pick' : pick
    }


    return render(request, 'index.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print('캐치에 도달해따')
    # print('============')
    # print(request)
    # print(type(request))
    # print(request.GET)
    # print(request.GET.get('message'))

    context = {
        'myMessage' : request.GET.get('message')
    }

    return render(request, 'catch.html', context)\

def greeting(request, age, word):
    result = False
    if word == word[::-1]:
        result = True
    context = {
        'age' : age,
        'result' : result,
        'word' : word,
    }
    return render(request, 'greeting.html', context)