from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import MainContent
from .models import Notices


def index(request):
    content_list=MainContent.objects.order_by('-pub_date')

    context = {'content_list': content_list}

    return render(request,'mysite/content_list.html', context)

def detail(request, content_id):

    content_list = get_object_or_404(MainContent, pk=content_id,)
    context = {'content_list': content_list}
    return render(request, 'mysite/content_detail.html', context)

def Notices(request):
    notices = Notices.objects.order_by('-pub_date')

    context = {'Notices': notices}

    return render(request, 'pages/notices.html', context)