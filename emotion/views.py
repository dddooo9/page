from django.shortcuts import render

# Create your views here.
def happy(request):
    return render(request, 'emotion/happy.html')


def sad(request):
    return render(request, 'emotion/sad.html')


def tired(request):
    return render(request, 'emotion/tired.html')


def angry(request):
    return render(request, 'emotion/angry.html')


def everyimg(request):
    return render(request, 'emotion/everyimg.html')