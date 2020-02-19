from django.shortcuts import render
from .models import Project,Review
from .forms import ProjectUploadForm,ProfileUpdateForm, ReviewForm
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer


# Create your views here.
# Create your views here.
def index(request,**kwargs):
    projects=Project.objects.all()[::-1]
    proj_upload=ProjectUploadForm(request.POST, request.FILES)
    if proj_upload.is_valid():
        projo=proj_upload.save(commit=False)
        projo.user=request.user
        projo.save()
        return HttpResponseRedirect(request.path_info)
    else:
        proj_upload=ProjectUploadForm()
    context={
        'projects':projects,
        'proj_upload':proj_upload,
    }
    return render(request, 'index.html', locals())

def myProfile(request,**kwargs):
    current_user=request.user
    prof_update=ProfileUpdateForm(request.POST)
    user_posts=Project.objects.filter(user=current_user.id)
    if prof_update.is_valid():
        profile=prof_update.save(commit=False)
        profile.user=current_user
        profile.save()
        return HttpResponseRedirect(request.path_info)
    else:
        prof_update=ProfileUpdateForm()
    context={
        'current_user':current_user,
        'prof_update':prof_update,
        'user_posts':user_posts,
    }
    return render(request, 'profile.html', locals())

def details(request, id):
    current_site=Project.single_project(id)
    current_user=request.user
    proj_reviews=Review.objects.filter(project=current_site)
    review_form=ReviewForm(request.POST)
    if review_form.is_valid():
        review=review_form.save(commit=False)
        review.user=current_user
        review.project=current_site
        review.save()
        return HttpResponseRedirect(request.path_info)
    else:
        review_form=ReviewForm()
    context={
        'current_user':current_user,
        'current_site':current_site,
        'review_form':review_form,
        'proj_reviews':proj_reviews,
    }
    return render(request, 'proj_details.html',locals())

def search_title(request):
    if request.method == "GET":
        search_term=request.GET.get('search', None)
        got_projects=Project.objects.filter(title__icontains=search_term)[::-1]
        context ={
            'got_projects':got_projects,
        }
        return render(request, 'results.html', locals())
    else:
        message="Looking for something, type it and hit search"
        return render(request, 'results.html', {'message':message})       
"""awards_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include 
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awards_app.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page":'/'}),
]
class Profile_list(APIView):
    def get(self, request, format=None):
        all_profile=Profile.objects.all()
        serializers=ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

class Project_list(APIView):
    def get(self,request,format=None):
        all_projects=Project.objects.all()
        serializers=ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)


