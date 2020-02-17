from . import views
from django.conf.urls import url


urlpatterns=[
    url(r'^$', views.index, name='homepage'),
    url(r'^profile/$', views.myProfile, name='profile'),
    url(r'^search/$', views.search_title, name='search_title'),
    url(r'^details/(\d+)$', views.details, name='details'),
    url(r'^api/profile/$', views.Profile_list.as_view()),
    url(r'^api/projects/$', views.Project_list.as_view()),
]
