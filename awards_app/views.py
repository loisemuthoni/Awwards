from django.shortcuts import render
from .models import Project,Review

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