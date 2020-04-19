from django.shortcuts import render


# Create your views here.

def dashboards(request):
    context = {}
    return render(request, 'dashboards/dashboards.html', context)
