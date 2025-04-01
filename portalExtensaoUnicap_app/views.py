from django.shortcuts import render

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html')

def AdminPageView(request):
    return render(request, 'admin-cards.html')

<<<<<<< HEAD
def Create(request):
    return render(request, 'create.html')
=======
>>>>>>> 7bcc98fa5e5d1588a29ca0199ee75b802f71e1a8
