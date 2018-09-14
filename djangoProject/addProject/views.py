from django.shortcuts import render

def addProject(request):
    return render(request, 'addProject/addProject.html')
