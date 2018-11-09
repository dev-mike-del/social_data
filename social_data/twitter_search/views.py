from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Screen_Name_Form

def get_screen_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Screen_Name_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('../twitter_search/twitter_profile_data')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Screen_Name_Form()

    return render(request,
                  'twitter_search/twitter_search.html',
                  {'form': form})

def get_twitter_profile(request):
    return render(request,
                  'twitter_search/twitter_profile.html')
