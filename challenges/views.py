from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def index(request):
    
    response_data = """
        <ul>
            <li><a href="/challenges/january">January</a></li>
            <li><a href="/challenges/february">February</a></li>
            <li><a href="/challenges/march">March</a></li>
        </ul>
    """
    
    return HttpResponse(response_data)

def monthly_challenge_by_number(request,month):

    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    
    return HttpResponseRedirect(redirect_path)


# dynamic view route
def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month.lower()]
        return HttpResponse("<h1>{}</h1>".format(challenge_text))
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")