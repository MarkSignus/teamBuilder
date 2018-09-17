from django.shortcuts import render

def conditions(request):
    return render(request, 'conditions/conditions.html')