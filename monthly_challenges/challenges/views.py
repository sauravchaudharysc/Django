from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.
'''This function is executed by DJango when an incoming request is forwarded to it'''
def january(request):
    return HttpResponse("Eat no meat for the entire month..!!") #Can be a html file

def february(request):
    return HttpResponse("Walk for at least 20  everyday..!!") #Can be a html file



monthly_challenges = {
    "january": "Dry January (No alcohol)",
    "february": "Fitness Challenge (Daily exercise)",
    "march": "Reading Challenge (Read a book a week)",
    "april": "Meditation Challenge (Daily meditation)",
    "may": "Healthy Eating Challenge (Eat more vegetables)",
    "june": "Hydration Challenge (Drink 8 glasses of water a day)",
    "july": "Outdoor Activity Challenge (Spend time outside daily)",
    "august": "Skill Development Challenge (Learn a new skill)",
    "september": "Sleep Improvement Challenge (Get 8 hours of sleep)",
    "october": "Decluttering Challenge (Organize and declutter your space)",
    "november": "Gratitude Challenge (Write down things you are grateful for)",
    "december": "Acts of Kindness Challenge (Do a kind act every day)"
}

def monthly_challenge_by_number(request,month):
    challenge_text=None
    if month == 1:
        challenge_text="Eat no meat for the entire month..!!"   
    elif month == 2:
        challenge_text="Celebrate Your Holiday..!!"    
    elif month == 3:
        challenge_text="Enjoy your vacation..!!"
    else :
        return HttpResponseNotFound("Error,Month not Present..!!") #Can be a html file
    return HttpResponse(challenge_text)




#The second argument must be written same as identifier written in urls.py. This is also called Keyword argument
def monthly_challenge(request,month):
    print("Saurav ",month)
    try :
        print(monthly_challenge)
        challenge_text=monthly_challenges[month]
    except :
        return HttpResponseNotFound("Error,Month not Present..!!") 
    return HttpResponse(challenge_text)