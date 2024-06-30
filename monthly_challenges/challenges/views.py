from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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



def index(request):
    months = list(monthly_challenges.keys())
    list_items=""
    for month in months:
        capitalize_month=month.capitalize()
        #Just jump back to urls.py and search for the one accepting args and gets the path
        month_path=reverse('month-challenge',args=[month]) 
        list_items+=f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
    response_data=f"<ol>{list_items}</ol>"   
    return HttpResponse(response_data)






# def monthly_challenge_by_number(request,month):
#     # A list of keys, dictionary are default ordered. First key in the dictionary will be first element in list. 
#     try :
#         challenge_text=monthly_challenges[list(monthly_challenges.keys())[month-1]]
#     except :
#         return HttpResponseNotFound("Error,Month not Present..!!")
#     return HttpResponse(challenge_text)

def monthly_challenge_by_number(request,month):
    months=list(monthly_challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month=months[month-1]
    redirect_path=reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)




#The second argument must be written same as identifier written in urls.py. This is also called Keyword argument
def monthly_challenge(request,month):
    try :
        challenge_text=monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        return render(request,'challenges/challenge.html')
        # return HttpResponse(response_data)
    except :
        return HttpResponseNotFound("Error,Month not Present..!!") 
    