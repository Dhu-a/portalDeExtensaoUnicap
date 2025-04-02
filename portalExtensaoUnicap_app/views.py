from django.shortcuts import render

# Create your views here.

def PortalExtensaoView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
def AdminPageView(request):
    return render(request, 'admin-cards.html',{'current_page':'admin-cards'})
def AdminTable(request):
    return render(request, 'admin-table.html',{'current_page':'admin-table'})
def Create(request):
    return render(request, 'create.html',{'current_page':'create'})
