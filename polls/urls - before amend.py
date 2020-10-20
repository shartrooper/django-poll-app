from django.urls import path

from . import views

# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail')
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
"""
Since polls are in their own URLconf (polls/urls.py),
they can be placed under “/polls/”, or under “/fun_polls/”,
or under “/content/polls/”, or any other path root, and the app will still work.

path() argument: route¶

route is a string that contains a URL pattern.
When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list,
comparing the requested URL against each pattern until it finds one that matches.

Patterns don’t search GET and POST parameters, or the domain name.
For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/.
In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

path() argument: view¶

When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument
and any “captured” values from the route as keyword arguments. We’ll give an example of this in a bit.

path() argument: kwargs¶

Arbitrary keyword arguments can be passed in a dictionary to the target view. We aren’t going to use this feature of Django in the tutorial.

path() argument: name¶

Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates.
This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

"""

"""
When somebody requests a page from your website – say, “/polls/34/”, Django will load the mysite.urls
Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses
the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text
– "34/" – to the ‘polls.urls’ URLconf for further processing. There it matches '<int:question_id>/', resulting in a call to the detail() view like so:

detail(request=<HttpRequest object>, question_id=34)

The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The :question_id> part of the string defines the name that will be used to identify the matched pattern, and the <int: part is a converter that determines what patterns should match this part of the URL path.
"""

