from django.shortcuts import render

# Landing page


def index(request):
    return render(request, 'pages/index.html')
