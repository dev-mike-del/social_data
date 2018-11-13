from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import Screen_Name_Form

from .search_twitter_profile import search_twitter_profile
from .search_twitter_profile_followers import search_twitter_profile_followers
from .search_twitter_profile_timeline import search_twitter_profile_timeline

def get_screen_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Screen_Name_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            request.session['screen_name'] = form.cleaned_data['screen_name']
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('twitter_search:twitter_profile_data'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Screen_Name_Form()

    return render(request,
                  'twitter_search/twitter_search.html',
                  {'form': form})

def get_twitter_profile(request):
    # Get data from request.session
    screen_name = request.session.get('screen_name')
    # API function
    api_profile = search_twitter_profile(screen_name)
    api_followers = search_twitter_profile_followers(screen_name)
    api_timeline = search_twitter_profile_timeline(screen_name)
    return render(request,
                  'twitter_search/twitter_profile.html',
                  context = {"api_profile":api_profile,
                             "api_followers":api_followers,
                             "api_timeline":api_timeline,})

