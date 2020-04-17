from django.shortcuts import render

# Create your views here.

def articles(request):
    if request == 'POST':
        pass
    else:
        context = {}
        return render(request, 'articles/articles.html', context)
