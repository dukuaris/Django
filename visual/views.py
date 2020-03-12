from django.shortcuts import render

def visual(requests):
    return render(requests, 'visual/welcome.html')

def gapminder(requests):
    return render(requests, 'visual/gapminder.html')

def multipleoutputs(requests):
    return render(requests, 'visual/multipleoutputs.html')

def interactions(requests):
    return render(requests, 'visual/interactions.html')

def stockprice(requests):
    return render(requests, 'visual/stockprice.html')
