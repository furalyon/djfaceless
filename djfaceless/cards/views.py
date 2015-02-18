from django.shortcuts import render

def browse(request):
    return render(request, 'cards/browse.html', {

    })