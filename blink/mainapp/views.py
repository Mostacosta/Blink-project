from django.shortcuts import render
from .models import home_cover,project,project_image
from django.shortcuts import get_object_or_404
# Create your views here.

def hero_section_view (request):
    hero = get_object_or_404(home_cover,pk=1)
    title=hero.title.split(" ")
    first_word=title[0]
    rest_word=""
    for x in range(1,len(title)):
        rest_word+=title[x]
    projects=project.objects.all()
    colors=["bg-white","bg-yellow","bg-orange","bg-blue","bg-mauve","bg-black"]
    if len(colors)<len(projects):
        diffrence=len(projects)-len(colors)
        for x in range(0,diffrence):
                colors.append(colors[x])

    zipped_list=zip(projects,colors)
    return render(request,'index.html',{'hero':hero,'projects':projects,"firstword":first_word,"restword":rest_word,"colors":colors,'zip':zipped_list})

def project_details(request,pk):
    the_project=get_object_or_404(project,pk=pk)
    images = project_image.objects.filter(project_images=the_project)
    stories=the_project.stories.split("*%")
    if stories == None :
        stories=the_project.stories
    return render(request, 'project_details.html', {'project':the_project,'images':images,'stories':stories})

