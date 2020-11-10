from django.shortcuts import render


def traveller(request):
    return render (request, 'index.html')
