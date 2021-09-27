from django.shortcuts import render
import random
from .forms import Getinput
# Create your views here.

def pass_gen(request):
    
    small_abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    capital_abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    nums=['1','2','3','4','5','6','7','8','8','9','0']
    symbols_str = ['~','!','@','#','$','%','^','&','*','+','<','>','/','?']

    list_of_char = [capital_abc,small_abc,nums,symbols_str]

    all_char=[]

    context = { 'form' : Getinput()}


    if request.method == 'POST':

        form = Getinput(request.POST)
        if form.is_valid():
            range = form.cleaned_data.get('range')
            Choices = form.cleaned_data.get('Choices')
            length_pw=int(range)
            try:
                for i in Choices:
                    all_char = all_char + list_of_char[int(i)-1]
        
                pass_char="".join(random.sample(all_char,length_pw))

                context = {
                    'form' : Getinput(),
                    'pass_char' : pass_char,
                }
                return render(request, 'passgen.html',context)
            except:
                context = {
                    'form' : Getinput(),
                    'error' : 'Bad entry:Try again',
                    'pass_char' : pass_char,
                }
                return render(request, 'passgen.html',context)
    else:
        form = Getinput
    return render(request, 'passgen.html',context)