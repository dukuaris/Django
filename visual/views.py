from django.shortcuts import render

def visual(requests):
    return render(requests, 'visual/welcome.html')
