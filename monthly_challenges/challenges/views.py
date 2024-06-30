from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
'''This function is executed by DJango when an incoming request is forwarded to it'''
def january(request):
    return HttpResponse("Eat no meat for the entire month..!!") #Can be a html file

def february(request):
    return HttpResponse("Walk for at least 20  everyday..!!") #Can be a html file


#The second argument must be written same as identifier written in urls.py. This is also called Keyword argument
def monthly_challenge(request,month):
    challenge_text=None
    if month == 'january':
        challenge_text="Eat no meat for the entire month..!!"   
    elif month == 'february':
        challenge_text="Celebrate Your Holiday..!!"    
    elif month == 'march':
        challenge_text="Enjoy your vacation..!!"
    else :
        return HttpResponseNotFound("Error,Month not Present..!!") #Can be a html file
    return HttpResponse(challenge_text)