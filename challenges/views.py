from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Do the duggie all night and all day",
    "may":"Look at your toes like you want to lick them with your fingers",
    "june":"Eat chicken wings once a week",
    "july":"Eat frogs once",
    "august":"Get apple",
    "september":"Put a rose on a forehead",
    "october":"rock socks",
    "november":"Be gone until November",
    "december":"Juggle on a ball"
    }


'''
# static view routes
def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk at least 20 minutes every day!")
'''

'''

def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

# dynamic view route
def monthly_challenge(request,month):
    challenge_text = None
    
    if month == 'january':
        challenge_text = "Eat no meat for the entire month!"
    elif month == 'february':
        challenge_text = "Walk at least 20 minutes every day!"
    elif month == 'march':
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    
    return HttpResponse(challenge_text)

'''

def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

# dynamic view route
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")