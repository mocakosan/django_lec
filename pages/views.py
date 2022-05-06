from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def notices(request):

  return render(request, 'pages/notices.html')

def services(request):

  return render(request, 'pages/services.html')


