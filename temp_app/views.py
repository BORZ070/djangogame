from django.shortcuts import render

def temp_views(request):
    return render(request, 'temp.html')
