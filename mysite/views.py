from django.shortcuts import render
from django.shortcuts import render
from .models import Maincontent


def index(request):
    content_list=Maincontent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request,'mysite/content_list.html', context)
