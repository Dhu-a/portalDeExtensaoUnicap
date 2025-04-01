from django.shortcuts import render

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'base.html')