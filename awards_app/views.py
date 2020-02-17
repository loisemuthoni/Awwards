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