from django.shortcuts import render


#перша сторінка
def home(request):
    return render(request, 'html/index.html')

