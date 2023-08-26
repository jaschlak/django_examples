from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


monthly_challenges = {
    "january":"Get more money",
    "february":"Walk at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Do the duggie all night and all day",
    "may":"Look at your toes like you want to lick them with your fingers",
    "june":"Try to get better at Roblox Studio",
    "july":"Eat frogs once",
    "august":"Become a youtuber",
    "september":"Put a rose on a forehead",
    "october":"Try to do more stuff!",
    "november":"Be gone until November",
    "december":"Juggle on a ball",
    "flembuary": None
    }

def index(request):
    
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
            "months": months
        })

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
        #response_date = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text,
            })
    except:
        raise Http404()